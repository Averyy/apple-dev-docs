# Conversation.Capabilities

**Framework**: LiveCommunicationKit  
**Kind**: struct

Used to configure a `Conversation` as part of a `Conversation.Update`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
struct Capabilities
```

## Topics

### Initializers
- [init(rawValue: Int)](conversation/capabilities/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [var rawValue: Int](conversation/capabilities/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [Conversation.Capabilities.ArrayLiteralElement](conversation/capabilities/arrayliteralelement.md)
  The type of the elements of an array literal.
- [Conversation.Capabilities.Element](conversation/capabilities/element.md)
  The element type of the option set.
- [Conversation.Capabilities.RawValue](conversation/capabilities/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let merging: Conversation.Capabilities](conversation/capabilities/merging.md)
  The conversation can be merged with another conversation, creating a single conversation that is displayed to the user.
- [static let pausing: Conversation.Capabilities](conversation/capabilities/pausing.md)
  The conversation can be temporarily paused including stopping all microphone, camera, and speaker interaction.
- [static let playingTones: Conversation.Capabilities](conversation/capabilities/playingtones.md)
  The conversation supports playing tone sequences.
- [static let unmerging: Conversation.Capabilities](conversation/capabilities/unmerging.md)
  Once merged, a conversation can be unmerged and reconfigured to act as a separate conversation.
- [static let video: Conversation.Capabilities](conversation/capabilities/video.md)
  The conversation includes video streams to be displayed to or sent from the user.
### Default Implementations
- [Equatable Implementations](conversation/capabilities/equatable-implementations.md)
- [OptionSet Implementations](conversation/capabilities/optionset-implementations.md)
- [RawRepresentable Implementations](conversation/capabilities/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](conversation/capabilities/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/capabilities)*