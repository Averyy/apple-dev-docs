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
- Handle errors for every CloudKit operation. When hitting a `.requestRateLimited` or `.serviceUnavailable` error, retrieve the [`CKErrorRetryAfterKey`](https://developer.apple.com/documentation/CloudKit/CKErrorRetryAfterKey) value from the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary, and use it as the number of seconds to wait before retrying the operation.
- For operations that are not critical for the current launch session, schedule them as background tasks using the [`Background Tasks`](https://developer.apple.com/documentation/BackgroundTasks) framework to have the system run the operations when it determines appropriate.

> **Note**: Apps that use [`CKSyncEngine`](https://developer.apple.com/documentation/CloudKit/CKSyncEngine-5sie5), which is a part of the CloudKit framework, don’t need to handle the errors. When hitting a throttle,  `CKSyncEngine` respects it and automatically re-schedules the synchronization tasks after the `retry-after` time.

Similarly, apps that use CloudKit Web Services or CloudKit JS need to gracefully handle the throttle error the CloudKit server returns, and honor the `retry-after` time.

Apps that use `NSPersistentCloudKitContainer` and `NSUbiquitousKeyValueStore` automatically recover when the throttles expire. If they get throttled frequently, consider re-designing their architecture and workflow to avoid hitting the request rate limit.

A retried request is not guaranteed to succeed. It may be throttled again, with a new `retry-after` time, for the same reason. If your CloudKit requests keep getting throttled, even though your app doesn’t have a lot of CloudKit traffic, and the device, networking, and [`system status`](https://developer.apple.comhttps://www.apple.com/support/systemstatus/) are all in a good state, consider [`Provide actionable feedback`](tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer#Provide-actionable-feedback.md).

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3162-understanding-cloudkit-throttles)*