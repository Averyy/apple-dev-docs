# FadeCommand.FadeDirection

**Framework**: Immersive Media Support  
**Kind**: enum

The direction of the fade command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum FadeDirection
```

## Topics

### Enumeration Cases
- [FadeCommand.FadeDirection.in](fadecommand/fadedirection/in.md)
  Represents fading in of the video frames from a ‘color’ requested.
- [FadeCommand.FadeDirection.out](fadecommand/fadedirection/out.md)
  Represents fading out of the video frames to a ‘color’ requested.
### Initializers
- [init?(intValue: Int)](fadecommand/fadedirection/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(rawValue: String)](fadecommand/fadedirection/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init?(stringValue: String)](fadecommand/fadedirection/init(stringvalue:).md)
  Creates a new instance from the given string.
### Instance Properties
- [var intValue: Int?](fadecommand/fadedirection/intvalue.md)
  The value to use in an integer-indexed collection (e.g. an int-keyed dictionary).
- [var rawValue: String](fadecommand/fadedirection/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [var stringValue: String](fadecommand/fadedirection/stringvalue.md)
  The string to use in a named collection (e.g. a string-keyed dictionary).
### Type Aliases
- [FadeCommand.FadeDirection.RawValue](fadecommand/fadedirection/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [CodingKey Implementations](fadecommand/fadedirection/codingkey-implementations.md)
- [Equatable Implementations](fadecommand/fadedirection/equatable-implementations.md)
- [RawRepresentable Implementations](fadecommand/fadedirection/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CodingKey](../Swift/CodingKey.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FadeCommand.FadeType](fadecommand/fadetype-swift.enum.md)
  An enum listing the available fade types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/fadedirection)*