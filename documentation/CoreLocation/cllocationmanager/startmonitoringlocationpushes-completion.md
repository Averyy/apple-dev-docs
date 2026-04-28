# startMonitoringLocationPushes(completion:)

**Framework**: Core Location  
**Kind**: method

Starts monitoring for the delivery of Apple Push Notification service (APNs) location pushes, and provides a device-specific token for sending pushes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func startMonitoringLocationPushes() async throws -> Data
```

## Mentions

- [Creating a location push service extension](creating-a-location-push-service-extension.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func startMonitoringLocationPushes() async throws -> Data
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This function requests an Apple Push Notification service (APNs) token that the system uses to launch your Location Push Service Extension and deliver pushes. Devices need an Internet connection to receive the token. Your completion block receives the token if the call succeeds, otherwise it receives error information. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

To use location push notifications, your app must have the `com.apple.developer.location.push` entitlement. For more information about implementing location pushes in your app, see [`Creating a location push service extension`](creating-a-location-push-service-extension.md).

## Parameters

- `completion`: The completion handler to call after you start monitoring location pushes. The completion handler takes the following parameters: - **`token`**: A globally unique token that identifies this device to APNs. Send this `token` to the server that you use to generate location pushes. Your server passes this `token` — unmodified — back to APNs when sending pushes. APNs device tokens are of variable length. Don’t hard-code their size. If an error occurs, `token` is `nil`.
- **`error`**: If your app is unable to register for location pushes, the system sets this parameter to an error object that contains information about why it failed; otherwise it’s `nil`. The error type is [`CLLocationPushServiceError`](cllocationpushserviceerror-swift.struct.md).

## See Also

- [func stopMonitoringLocationPushes()](cllocationmanager/stopmonitoringlocationpushes.md)
  Stops monitoring for Apple Push Notification service (APNs) location pushes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringlocationpushes(completion:))*