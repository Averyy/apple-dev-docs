# application(_:handleWatchKitExtensionRequest:reply:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to respond to a request from a paired watchOS app.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, handleWatchKitExtensionRequest userInfo: [AnyHashable : Any]?) async -> [AnyHashable : Any]?
```

#### Discussion

If your iOS app and watchOS app coordinate efforts to perform certain tasks, implement this method and use it to respond to requests from the watchOS app. After finishing the request, execute the provided `reply` block (if any) to return the results.

Because this method is likely to be called while your app is in the background, call the [`beginBackgroundTask(withName:expirationHandler:)`](uiapplication/beginbackgroundtask(withname:expirationhandler:).md) method at the start of your implementation and the [`endBackgroundTask(_:)`](uiapplication/endbackgroundtask(_:).md) method after you have processed the reply and executed the `reply` block. Starting a background task ensures that your app is not suspended before it has a chance to send its reply.

## Parameters

- `application`: Your singleton app object.
- `userInfo`: A dictionary provided by the watchOS app with the request information. Use the data in this dictionary to process the request from the watchOS app.
- `reply`: A block to execute with the results of the request. This block has no return value and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handlewatchkitextensionrequest:reply:))*