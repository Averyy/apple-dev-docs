# PlayToneAction.Tone

**Framework**: LiveCommunicationKit  
**Kind**: enum

Values that describe keypad tones.

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

### Keypad tones
- [PlayToneAction.Tone.hardPause](playtoneaction/tone-swift.enum/hardpause.md)
  A person entered a hard pause.
- [PlayToneAction.Tone.single](playtoneaction/tone-swift.enum/single.md)
  A person entered a digit.
- [PlayToneAction.Tone.softPause](playtoneaction/tone-swift.enum/softpause.md)
  A person entered a soft pause.
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let digits: String](playtoneaction/digits.md)
  The digits tapped by the user into the keypad or included in the dial string.
- [let tone: PlayToneAction.Tone](playtoneaction/tone-swift.property.md)
  The keypad tone to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/playtoneaction/tone-swift.enum)*