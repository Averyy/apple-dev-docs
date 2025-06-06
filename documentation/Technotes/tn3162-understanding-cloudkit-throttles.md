# TN3162: Understanding CloudKit throttles

**Framework**: Technotes

Learn how to identify and handle CloudKit throttles.

#### Overview

The CloudKit infrastructure is shared by all apps and services. The resources are finite, and so high utilization from one app can negatively affect others. To avoid this kind of impact and optimize the overall experience, CloudKit implements a number of limits and controls on incoming traffic, which are known as .

CloudKit can enforce throttles when it deems necessary on any app or service that uses the [`CloudKit`](https://developer.apple.com/documentation/CloudKit) framework, [`CloudKit Web Services`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html), [`CloudKit JS`](https://developer.apple.com/documentation/CloudKitJS), [`NSPersistentCloudKitContainer`](https://developer.apple.com/documentation/CoreData/NSPersistentCloudKitContainer), and [`NSUbiquitousKeyValueStore`](https://developer.apple.com/documentation/Foundation/NSUbiquitousKeyValueStore). This technote discusses how to identify CloudKit throttles with representative error messages and how to handle them.

#### Identify Cloudkit Throttles

The CloudKit server throttles a request from an app in the following cases:

- The app issues many CloudKit requests in a short time frame, and hits the rate limit.
- The app uses CloudKit in an inappropriate pattern, such as simultaneously triggering recurring spikes in request rates from many devices.

When the CloudKit server enforces throttles, it returns an error with a `retryAfter` value, which indicates how long the app should wait before retrying the request. For apps that use the CloudKit framework, the error is converted to [`serviceUnavailable`](https://developer.apple.com/documentation/CloudKit/CKError/serviceUnavailable), with information shown in the following example:

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

CloudKit on the device side can work with the server to enforce throttles as well. This prevents CloudKit requests from being sent to the server, and saves networking and server resources. When an app hits this kind of throttle, its CloudKit operation ([`CKOperation`](https://developer.apple.com/documentation/CloudKit/CKOperation)) gets a [`requestRateLimited`](https://developer.apple.com/documentation/CloudKit/CKError/requestRateLimited) error, as shown in the following example:

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
- Handle errors for every CloudKit operation. When hitting a `.requestRateLimited` or `.serviceUnavailable` error, retrieve the [`CKErrorRetryAfterKey`](https://developer.apple.com/documentation/CloudKit/CKErrorRetryAfterKey) value from the [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary, and use it as the number of seconds to wait before retrying the operation.
- For operations that are not critical for the current launch session, schedule them as background tasks using the [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks) framework to have the system run the operations when it determines appropriate.

> **Note**: Apps that use [`CKSyncEngine`](https://developer.apple.com/documentation/CloudKit/CKSyncEngine-5sie5), which is a part of the CloudKit framework, don’t need to handle the errors. When hitting a throttle,  `CKSyncEngine` respects it and automatically re-schedules the synchronization tasks after the `retry-after` time.

Similarly, apps that use CloudKit Web Services or CloudKit JS need to gracefully handle the throttle error the CloudKit server returns, and honor the `retry-after` time.

Apps that use `NSPersistentCloudKitContainer` and `NSUbiquitousKeyValueStore` automatically recover when the throttles expire. If they get throttled frequently, consider re-designing their architecture and workflow to avoid hitting the request rate limit.

A retried request is not guaranteed to succeed. It may be throttled again, with a new `retry-after` time, for the same reason. If your CloudKit requests keep getting throttled, even though your app doesn’t have a lot of CloudKit traffic, and the device, networking, and [`system status`](https://developer.apple.comhttps://www.apple.com/support/systemstatus/) are all in a good state, consider [`Provide actionable feedback`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Provide-actionable-feedback.md).

#### Revision History

-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3162-understanding-cloudkit-throttles)*