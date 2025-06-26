# FadeCommand.FadeDirection

**Framework**: Immersive Media Support  
**Kind**: enum

A value representing the direction of the fade command.

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
  A value representing fading in of the video frames from a ‘color’ requested.
- [FadeCommand.FadeDirection.out](fadecommand/fadedirection/out.md)
  A value representing fading out of the video frames to a ‘color’ requested.
### Initializers
- [init?(intValue: Int)](fadecommand/fadedirection/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(stringValue: String)](fadecommand/fadedirection/init(stringvalue:).md)
  Creates a new instance from the given string.
- [init(from: any Decoder) throws](fadecommand/fadedirection/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var intValue: Int?](fadecommand/fadedirection/intvalue.md)
  The value to use in an integer-indexed collection (e.g. an int-keyed dictionary).
- [var stringValue: String](fadecommand/fadedirection/stringvalue.md)
  The string to use in a named collection (e.g. a string-keyed dictionary).
- [var hashValue: Int](fadecommand/fadedirection/hashvalue.md)
  The hash value.
### Operators
- [static func == (FadeCommand.FadeDirection, FadeCommand.FadeDirection) -> Bool](fadecommand/fadedirection/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Methods
- [func encode(to: any Encoder) throws](fadecommand/fadedirection/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](fadecommand/fadedirection/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CodingKey Implementations](fadecommand/fadedirection/codingkey-implementations.md)
- [Equatable Implementations](fadecommand/fadedirection/equatable-implementations.md)

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand/fadedirection)*