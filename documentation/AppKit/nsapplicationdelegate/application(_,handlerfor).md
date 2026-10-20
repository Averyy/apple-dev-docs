# application(_:handlerFor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an intent handler that’s capable of handling the specified intent.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
optional func application(_ application: NSApplication, handlerFor intent: INIntent) -> Any?
```

```objc
- (id) application:(NSApplication *) application handlerForIntent:(INIntent *) intent;
```

#### Return Value

An instance of a type capable of handling the specified intent, or `nil` if your app doesn’t handle the intent. Return an instance of a type that conforms to the protocol for handling intents of the same type as the provided `intent`.

#### Discussion

Siri invokes this method on the main queue when it wants to process one of your app’s supported intents. To indicate the intents that your app supports, populate the [`INIntentsSupported`](../../BundleResources/information-property-list/inintentssupported.md) array in your app target’s `Info.plist` file.

In your delegate’s implementation of this method, check the `intent` parameter’s type and return a custom object that adopts the corresponding handling protocol. For example, if `intent` is an instance of [`INPlayMediaIntent`](https://developer.apple.com/documentation/intents/inplaymediaintent), return an object that adopts [`INPlayMediaIntentHandling`](https://developer.apple.com/documentation/intents/inplaymediaintenthandling). Only use the provided intent to determine which handler to return; don’t use it to initialize the handler and don’t store a reference to it. SiriKit updates the intent throughout the request to incorporate information the user provides. For more information, see [Dispatching intents to handlers](../../SiriKit/dispatching-intents-to-handlers.md).

For information about handling intents, see [Resolving and Handling Intents](../../SiriKit/resolving-and-handling-intents.md).

## Parameters

- `application`: The shared app object.
- `intent`: The intent object that represents the request coming from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/application(_:handlerfor:))*