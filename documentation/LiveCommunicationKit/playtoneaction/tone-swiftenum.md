# PlayToneAction.Tone

**Framework**: LiveCommunicationKit  
**Kind**: enum

The types of tones that may be played.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
enum Tone
```

## Topics

### Enumeration Cases
- [PlayToneAction.Tone.hardPause](playtoneaction/tone-swift.enum/hardpause.md)
  Indicates that the user included digits after a hard pause in their dial string. A hard pause is indicated by a semicolon (;) and waits for further user interaction before dialing the additional digits.
- [PlayToneAction.Tone.single](playtoneaction/tone-swift.enum/single.md)
  Indicates that the user tapped a digit on the in-call keypad.
- [PlayToneAction.Tone.softPause](playtoneaction/tone-swift.enum/softpause.md)
  Indicates that the user included digits after a soft pause in their dial string. A soft pause is indicated by a comma (,) and waits a few seconds before dialing the additional digits.
### Initializers
- [init?(rawValue: Int)](playtoneaction/tone-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: Int](playtoneaction/tone-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [PlayToneAction.Tone.RawValue](playtoneaction/tone-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](playtoneaction/tone-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](playtoneaction/tone-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/playtoneaction/tone-swift.enum)*