# didReceiveLocationPushPayload(_:completion:)

**Framework**: Core Location  
**Kind**: method  
**Required**: Yes

Delivers a location push notification for your app extension to process.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
func didReceiveLocationPushPayload(_ payload: [String : Any]) async
```

## Mentions

- [Creating a location push service extension](creating-a-location-push-service-extension.md)

#### Discussion

> ❗ **Important**:  You can implement this delegate method as a synchronous method that takes a completion handler, as shown on this page, or as an asynchronous method that has the following declaration: ```swift
func didReceiveLocationPushPayload(_ payload: [String : Any]) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

When the system receives a location push notification that targets your app, it runs your app extension and calls this method. Use your implementation of this method to request the device’s current location and do something with that information. For example, a location-sharing app might send the location back to a server to update the person’s current location.

When you add a location push service app extension to your project, the Xcode template includes an implementation of this method for you to modify. The template uses this method to store the completion block and initialize a [`CLLocationManager`](cllocationmanager.md) instance. Process the result of your location query in the [`CLLocationManagerDelegate`](cllocationmanagerdelegate.md) methods.

> ❗ **Important**:  Protecting user privacy is important when handling location data. End-to-end encryption provides enhanced security if your app moves location data off the user’s device, including transmitting it to a server or to another user. For more information, see [`Protecting the User’s Privacy`](https://developer.apple.com/documentation/UIKit/protecting-the-user-s-privacy).

Store the completion block and call it after you finish processing the location request. Also call the completion block when the system calls [`serviceExtensionWillTerminate()`](cllocationpushserviceextension/serviceextensionwillterminate().md).

## Parameters

- `payload`: The payload containing the location push.
- `completion`: Execute this block as quickly as possible after you finish the location-related task. If you take too long to execute this block, the system calls the   method as a warning. If you still don’t call the block in a timely manner, the system terminates your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceextension/didreceivelocationpushpayload(_:completion:))*