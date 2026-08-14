# TN3162: Understanding CloudKit throttles

**Framework**: Technotes

Learn how to identify and handle CloudKit throttles.

#### Overview

The CloudKit infrastructure is shared by all apps and services. The resources are finite, and so high utilization from one app can negatively affect others. To avoid this kind of impact and optimize the overall experience, CloudKit implements a number of limits and controls on incoming traffic, which are known as *throttles*.

CloudKit can enforce throttles when it deems necessary on any app or service that uses the [`CloudKit`](https://developer.apple.com/documentation/cloudkit) framework, [`CloudKit Web Services`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html), [`CloudKit JS`](https://developer.apple.com/documentation/cloudkitjs), [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer), and [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore). This technote discusses how to identify CloudKit throttles with representative error messages and how to handle them.

#### Identify Cloudkit Throttles

The CloudKit server throttles a request from an app in the following cases:

- The app issues many CloudKit requests in a short time frame, and hits the rate limit.
- The app uses CloudKit in an inappropriate pattern, such as simultaneously triggering recurring spikes in request rates from many devices.

When the CloudKit server enforces throttles, it returns an error with a `retryAfter` value, which indicates how long the app should wait before retrying the request. For apps that use the CloudKit framework, the error is converted to [`serviceUnavailable`](https://developer.apple.com/documentation/cloudkit/ckerror/serviceunavailable), with information shown in the following example:

```None
[
    "CKErrorShouldThrottleClient": 1, 
    "RequestUUID": B59F1738-B330-4F27-A2AE-3C95572BC9F4, 
    "NSLocalizedDescription": Request failed with http status code 503, 
    "CKRetryAfter": 30, 
    "CKErrorDescription": Request failed with http status code 503, 
    "NSDebugDescription": CKInternalErrorDomain: 2022, 
    "NSUnderlyingError": <CKError 0x60000040c060: "Service Unavailable" (2022); 
        "Request failed with http status code 503"; 
        uuid = B59F1738-B330-4F27-A2AE-3C95572BC9F4; 
        Retry after 30.0 seconds>
]
```

For apps that use CloudKit Web Services or CloudKit JS, the error is conveyed in a server response with a body like the following example:

```None
{
    "reason": "Database throttled, retry later",
    "retryAfter": 110207,
    "serverErrorCode": "THROTTLED",
    "error_code": "THROTTLED",
    "messageForDeveloper": "Database throttled, retry later",
    "uuid": wsThrottles_000029fa-7fd4-4eac-a5de-970942d10b7f
}
```

CloudKit on the device side can work with the server to enforce throttles as well. This prevents CloudKit requests from being sent to the server, and saves networking and server resources. When an app hits this kind of throttle, its CloudKit operation ([`CKOperation`](https://developer.apple.com/documentation/cloudkit/ckoperation)) gets a [`requestRateLimited`](https://developer.apple.com/documentation/cloudkit/ckerror/requestratelimited) error, as shown in the following example:

```None
<CKError 0x600003ba77b0: "Request Rate Limited" (7/2008); 
"This operation has been rate limited due to an earlier error: Request failed with http status code 503"; 
Retry after 51.6 seconds>
```

Use these example messages to determine if your app hits CloudKit throttles. If you use the CloudKit framework, check if any CloudKit operation returns an `.serviceUnavailable` or `.requestRateLimited` error.  For CloudKit Web Services or CloudKit JS, check if any response from the CloudKit server contains the `THROTTLED` error. Apps that use `NSPersistentCloudKitContainer` and `NSUbiquitousKeyValueStore` don’t perform CloudKit operations directly, so you need to look into a sysdiagnose. To capture and analyze a sysdiagnose, see [`Capture and analyze a sysdiagnose`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Capture-and-analyze-a-sysdiagnose.md)

> **Note**: The system on a device can throttle CloudKit requests for other reasons. For example, when the battery level on an iPhone or Apple Watch runs low, iOS or watchOS may decide to defer a CloudKit operation, and this kind of throttle expires only after the battery returns to a high level. For more information, see [`Understand system throttles`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Understand-system-throttles.md).

#### Handle Cloudkit Throttles

CloudKit throttles are implemented to balance the use of CloudKit resources and achieve the best overall user experience of the service. When an app hits throttles, CloudKit stops accepting its requests until the throttles expire. There is no API for an app to configure the expiration time.

The best strategy to handle CloudKit throttles is to avoid them in the first place, and respect the `retryAfter` time if they happen. For apps that use the CloudKit framework, consider the following:

- Minimize the number of CloudKit operations and avoid doing many operations in a short time frame.
- Handle errors for every CloudKit operation. When hitting a `.requestRateLimited` or `.serviceUnavailable` error, retrieve the [`CKErrorRetryAfterKey`](https://developer.apple.com/documentation/cloudkit/ckerrorretryafterkey) value from the [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/userinfo) dictionary, and use it as the number of seconds to wait before retrying the operation.
- For operations that are not critical for the current launch session, schedule them as background tasks using the [`Background Tasks`](https://developer.apple.com/documentation/backgroundtasks) framework to have the system run the operations when it determines appropriate.

> **Note**: Apps that use [`CKSyncEngine`](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5), which is a part of the CloudKit framework, don’t need to handle the errors. When hitting a throttle,  `CKSyncEngine` respects it and automatically re-schedules the synchronization tasks after the `retry-after` time.

Similarly, apps that use CloudKit Web Services or CloudKit JS need to gracefully handle the throttle error the CloudKit server returns, and honor the `retry-after` time.

Apps that use `NSPersistentCloudKitContainer` and `NSUbiquitousKeyValueStore` automatically recover when the throttles expire. If they get throttled frequently, consider re-designing their architecture and workflow to avoid hitting the request rate limit.

A retried request is not guaranteed to succeed. It may be throttled again, with a new `retry-after` time, for the same reason. If your CloudKit requests keep getting throttled, even though your app doesn’t have a lot of CloudKit traffic, and the device, networking, and [`system status`](https://developer.apple.comhttps://www.apple.com/support/systemstatus/) are all in a good state, consider [`Provide actionable feedback`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Provide-actionable-feedback.md).

#### Revision History

- **2024-02-20** First published.

## See Also

- [TN3163: Understanding the synchronization of NSPersistentCloudKitContainer](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer.md)
  Explore the details inside the synchronization of `NSPersistentCloudKitContainer` by capturing and analyzing a sysdiagnose.
- [TN3164: Debugging the synchronization of NSPersistentCloudKitContainer](tn3164-debugging-the-synchronization-of-nspersistentcloudkitcontainer.md)
  Identify and resolve synchronization issues when working with `NSPersistentCloudKitContainer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3162-understanding-cloudkit-throttles)*