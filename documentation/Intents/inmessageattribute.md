# INMessageAttribute

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate an attribute of a message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INMessageAttribute
```

```c
enum INMessageAttribute : NSInteger;
```

## Topics

### Constants
- [INMessageAttribute.unknown](./inmessageattribute/unknown.md)
  No known attribute.
- [INMessageAttribute.read](./inmessageattribute/read.md)
  The message is marked as read.
- [INMessageAttribute.unread](./inmessageattribute/unread.md)
  The message is marked as unread.
- [INMessageAttribute.flagged](./inmessageattribute/flagged.md)
  The message has been flagged.
- [INMessageAttribute.unflagged](./inmessageattribute/unflagged.md)
  The message has not been flagged.
- [INMessageAttribute.played](./inmessageattribute/played.md)
  The message has been played.
### Initializers
- [init?(rawValue: Int)](./inmessageattribute/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing Message Information
- [class INMessage](./inmessage.md)
  An object that describes a sent or received message.
- [struct INMessageAttributeOptions](./inmessageattributeoptions.md)
  Constants that indicate a message search filter.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessageattribute)*