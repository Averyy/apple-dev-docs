# INIntentHandlerProviding

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The interface for dispatching intents to the custom objects that handle those intents.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INIntentHandlerProviding : NSObjectProtocol
```

```objc
@protocol INIntentHandlerProviding <NSObject>
```

#### Overview

The `INIntentHandlerProviding` protocol defines the method for routing SiriKit requests to the appropriate objects of your Intents extension. The method in this protocol acts as a dispatcher, returning an object capable of resolving, confirming, and handling a specific intent object. This protocol is adopted by the [`INExtension`](./inextension.md) class and you must provide a custom implementation.

When you add an Intents extension to your project, Xcode automatically creates a default [`INExtension`](./inextension.md) subclass that adopts this protocol. Modify the [`handler(for:)`](./inintenthandlerproviding/handler%28for%29.md) method in that subclass and use it to create your handler objects. You can use the same class to handle multiple intents or you can use different classes for each intent.

## Topics

### Providing Handlers for Intents
- [func handler(for: INIntent) -> Any?](./inintenthandlerproviding/handler%28for%29.md)
  Returns the object capable of handling the specified intent in an extension.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [INExtension](./inextension.md)

## See Also

### Intents App Extension
- [Creating an Intents App Extension](../SiriKit/creating-an-intents-app-extension.md)
  Add and configure an Intents app extension in your Xcode project.
- [Structuring Your Code to Support App Extensions](../SiriKit/structuring-your-code-to-support-app-extensions.md)
  Move your back-end services to a private framework so your app and app extensions can use them.
- [class INExtension](./inextension.md)
  The entry point for an Intents extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenthandlerproviding)*