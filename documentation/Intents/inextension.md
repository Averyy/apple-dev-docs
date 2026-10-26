# INExtension

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The entry point for an Intents extension.

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
class INExtension
```

```objc
@interface INExtension : NSObject
```

## Mentions

- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)

#### Overview

The [`INExtension`](./inextension.md) class is the principal class of your Intents extension, which provides information to SiriKit. Your extension object acts like a dispatcher, providing SiriKit with the objects it needs to resolve and handle requests. This class defines no methods of its own, but it adopts the [`INIntentHandlerProviding`](./inintenthandlerproviding.md) protocol, which contains the main method you must implement.

You do not create instances of this class directly. When the system needs your Intents extension to handle a request, it automatically instantiates the class specified in the `NSExtensionPrincipalClass` key of the extension’s `Info.plist` file. All you have to do is provide the implementation for that class.

Your extension object must be able to return handler objects for all of the intents that your app supports. The Intents framework supports the following types of intents:

- VoIP calling intents support audio and video calls to another user of your app.
- Workout intents support the starting and stopping of workouts.
- Message intents support the sending of message data to specific users.
- Payment intents support financial transactions between users.
- Photo intents support the searching and displaying of photos.
- Ride-booking intents support the booking and management of user transportation from Siri or Maps.
- CarPlay intents support the changing of settings in automobiles that support CarPlay.
- Restaurant reservation intents support the creating and viewing of restaurant reservations in Maps.

For more information about implementing your extension’s main dispatching method, see [`INIntentHandlerProviding`](./inintenthandlerproviding.md). For information about how to implement this class in your Intents extension, see [SiriKit Programming Guide](https://developer.apple.com/library/archive/documentation/Intents/Conceptual/SiriIntegrationGuide/index.html#//apple_ref/doc/uid/TP40016875).

## Topics

### Constants
- [IntentsVersionNumber](./intentsversionnumber.md)
- [IntentsVersionString](./intentsversionstring.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentHandlerProviding](./inintenthandlerproviding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Intents App Extension
- [Creating an Intents App Extension](../SiriKit/creating-an-intents-app-extension.md)
  Add and configure an Intents app extension in your Xcode project.
- [Structuring Your Code to Support App Extensions](../SiriKit/structuring-your-code-to-support-app-extensions.md)
  Move your back-end services to a private framework so your app and app extensions can use them.
- [protocol INIntentHandlerProviding](./inintenthandlerproviding.md)
  The interface for dispatching intents to the custom objects that handle those intents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inextension)*