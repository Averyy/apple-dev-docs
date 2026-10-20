# MSMessagesAppPresentationContext

**Framework**: Messages  
**Kind**: enum  
**Role**: Enumeration

Presentation contexts describing where your iMessage app appears.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum MSMessagesAppPresentationContext
```

```c
enum MSMessagesAppPresentationContext : NSUInteger;
```

## Topics

### Presentation Contexts
- [MSMessagesAppPresentationContext.media](./msmessagesapppresentationcontext/media.md)
  A constant that indicates the iMessage app appears inside the Stickers app throughout iOS including in Messages, FaceTime, the emoji keyboard, and Markup.
- [MSMessagesAppPresentationContext.messages](./msmessagesapppresentationcontext/messages.md)
  A constant that indicates the iMessage app appears in Messages in the list of iMessage apps that appears when you press the plus button.
### Initializers
- [init?(rawValue: UInt)](./msmessagesapppresentationcontext/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Presentation Styles and Contexts
- [var presentationStyle: MSMessagesAppPresentationStyle](./msmessagesappviewcontroller/presentationstyle.md)
  The extension’s current presentation style.
- [func requestPresentationStyle(MSMessagesAppPresentationStyle)](./msmessagesappviewcontroller/requestpresentationstyle%28_%29.md)
  Asks the extension’s user interface to transition to the provided style.
- [func willTransition(to: MSMessagesAppPresentationStyle)](./msmessagesappviewcontroller/willtransition%28to%29.md)
  Tells the view controller that the extension is about to transition to a new presentation style.
- [func didTransition(to: MSMessagesAppPresentationStyle)](./msmessagesappviewcontroller/didtransition%28to%29.md)
  Tells the view controller that the extension has transitioned to a new presentation style.
- [enum MSMessagesAppPresentationStyle](./msmessagesapppresentationstyle.md)
  Presentation styles that describe your iMessage app’s appearance.
- [var presentationContext: MSMessagesAppPresentationContext](./msmessagesappviewcontroller/presentationcontext.md)
  The context describing where your iMessage app is presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapppresentationcontext)*