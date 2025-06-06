# OSLogMessageComponent

**Framework**: OSLog  
**Kind**: class

The message arguments for a particular entry.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class OSLogMessageComponent
```

#### Overview

There is one component for each placeholder in the formatString plus one component for any text after the last placeholder.

## Topics

### Reading the Argument
- [var argument: OSLogMessageComponent.Argument](oslogmessagecomponent/argument-swift.property.md)
  The argument passed into the message component.
- [OSLogMessageComponent.Argument](oslogmessagecomponent/argument-swift.enum.md)
  An object representing data that corresponds to an argument in a message payload.
- [var argumentCategory: OSLogMessageComponent.ArgumentCategory](oslogmessagecomponent/argumentcategory-swift.property.md)
  The type of argument that corresponds to the placeholder.
- [OSLogMessageComponent.ArgumentCategory](oslogmessagecomponent/argumentcategory-swift.enum.md)
  The data type corresponding to the argument provided in a message payload.
### Reading the Message Component
- [var formatSubstring: String](oslogmessagecomponent/formatsubstring.md)
  The text immediately preceding a placeholder.
- [var placeholder: String](oslogmessagecomponent/placeholder.md)
  The placeholder text for the message component.
### Accessing the Argument
- [var argumentDataValue: Data?](oslogmessagecomponent/argumentdatavalue.md)
  The argument formatted as a sequence of bytes.
- [var argumentDoubleValue: Double](oslogmessagecomponent/argumentdoublevalue.md)
  The argument formatted as a double.
- [var argumentInt64Value: Int64](oslogmessagecomponent/argumentint64value.md)
  The argument formatted as a signed 64-bit integer.
- [var argumentNumberValue: NSNumber?](oslogmessagecomponent/argumentnumbervalue.md)
  The argument formatted as a number.
- [var argumentStringValue: String?](oslogmessagecomponent/argumentstringvalue.md)
  The argument formatted as a string.
- [var argumentUInt64Value: UInt64](oslogmessagecomponent/argumentuint64value.md)
  The argument formatted as an unsigned 64-bit integer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class OSLogPosition](oslogposition.md)
  A representation of a point in a sequence of entries in the unified logging system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogmessagecomponent)*