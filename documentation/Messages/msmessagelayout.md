# MSMessageLayout

**Framework**: Messages  
**Kind**: class  
**Role**: Class

An abstract base class that defines the appearance of [`MSMessage`](./msmessage.md) objects in the conversation transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSMessageLayout
```

```objc
@interface MSMessageLayout : NSObject
```

## Overview

You do not subclass `MSMessageLayout` or create instances of it directly. Instead, instantiate the provided concrete subclass, the [`MSMessageTemplateLayout`](./msmessagetemplatelayout.md) class.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [MSMessageLiveLayout](./msmessagelivelayout.md)
- [MSMessageTemplateLayout](./msmessagetemplatelayout.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Interactive messages
- [class MSMessage](./msmessage.md)
  A custom message object.
- [class MSSession](./mssession.md)
  A session object used to create and update messages.
- [class MSMessageTemplateLayout](./msmessagetemplatelayout.md)
  A template-based layout for custom messages.
- [class MSMessageLiveLayout](./msmessagelivelayout.md)
  A layout that provides a custom, interactive view inside the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagelayout)*