# INMessageAttributeOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants that indicate a message search filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
struct INMessageAttributeOptions
```

```c
enum INMessageAttributeOptions : NSUInteger;
```

## Topics

### Constants
- [static var read: INMessageAttributeOptions](./inmessageattributeoptions/read.md)
  A read message.
- [static var unread: INMessageAttributeOptions](./inmessageattributeoptions/unread.md)
  An unread message.
- [static var flagged: INMessageAttributeOptions](./inmessageattributeoptions/flagged.md)
  A flagged message.
- [static var unflagged: INMessageAttributeOptions](./inmessageattributeoptions/unflagged.md)
  An unflagged message.
- [static var played: INMessageAttributeOptions](./inmessageattributeoptions/played.md)
  A played message.
### Initializers
- [init(rawValue: UInt)](./inmessageattributeoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Managing Message Information
- [class INMessage](./inmessage.md)
  An object that describes a sent or received message.
- [enum INMessageAttribute](./inmessageattribute.md)
  Constants that indicate an attribute of a message.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessageattributeoptions)*