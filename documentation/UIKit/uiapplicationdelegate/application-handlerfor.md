# application(_:handlerFor:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for an intent handler capable of handling the specified intent.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, handlerFor intent: INIntent) -> Any?
```

#### Return Value

An instance of a type capable of handling the specified intent; otherwise, `nil` if your app doesn’t handle the intent. Return an instance of a type that conforms to the handling intents protocol for the same type as the provided intent.

#### Discussion

> ❗ **Important**:  The system only invokes this method in apps that support multiple scenes. For more information, see [`Specifying the scenes your app supports`](specifying-the-scenes-your-app-supports.md).

Siri invokes this method on the main queue when it wants to process one of your app’s supported intents. To indicate the intents that your app supports, populate the [`INIntentsSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/INIntentsSupported) array in your app target’s `Info.plist` file.

In your delegate’s implementation of this method, check the `intent` parameter’s type and return a custom object that adopts the corresponding handling protocol. For example, if `intent` is an instance of [`INPlayMediaIntent`](https://developer.apple.com/documentation/Intents/INPlayMediaIntent), return an object that adopts [`INPlayMediaIntentHandling`](https://developer.apple.com/documentation/Intents/INPlayMediaIntentHandling). Only use the provided intent to determine the handler to return; don’t use it to initialize the handler and don’t store a reference to it. SiriKit updates the intent throughout the request to incorporate information the requester provides. For more information, see [`Dispatching intents to handlers`](https://developer.apple.com/documentation/SiriKit/dispatching-intents-to-handlers).

For information about handling intents, see [`Resolving and Handling Intents`](https://developer.apple.com/documentation/SiriKit/resolving-and-handling-intents).

## Parameters

- `application`: The shared app object.
- `intent`: The intent object that represents the request coming from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:handlerfor:))*