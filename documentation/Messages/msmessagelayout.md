# MSMessageLayout

**Framework**: Messages  
**Kind**: class

An abstract base class that defines the appearance of [`MSMessage`](msmessage.md) objects in the conversation transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSMessageLayout
```

#### Overview

You do not subclass `MSMessageLayout` or create instances of it directly. Instead, instantiate the provided concrete subclass, the [`MSMessageTemplateLayout`](msmessagetemplatelayout.md) class.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [MSMessageLiveLayout](msmessagelivelayout.md)
- [MSMessageTemplateLayout](msmessagetemplatelayout.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MSMessage](msmessage.md)
  A custom message object.
- [class MSSession](mssession.md)
  A session object used to create and update messages.
- [class MSMessageTemplateLayout](msmessagetemplatelayout.md)
  A template-based layout for custom messages.
- [class MSMessageLiveLayout](msmessagelivelayout.md)
  A layout that provides a custom, interactive view inside the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagelayout)*