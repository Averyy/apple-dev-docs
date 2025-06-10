# Conversation.Capabilities

**Framework**: LiveCommunicationKit  
**Kind**: struct

A type that describes capabilities of a conversation.

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

#### Overview

Configure conversation capabilites as part of a [`Conversation.Update`](conversation/update.md).

## Topics

### Capabilities
- [static let merging: Conversation.Capabilities](conversation/capabilities/merging.md)
  The conversation can merge with another conversation to create a new conversation.
- [static let pausing: Conversation.Capabilities](conversation/capabilities/pausing.md)
  The conversation is active and can be temporarily paused.
- [static let playingTones: Conversation.Capabilities](conversation/capabilities/playingtones.md)
  The conversation supports playing tone sequences.
- [static let unmerging: Conversation.Capabilities](conversation/capabilities/unmerging.md)
  The conversation is the result of merging two conversations and can be separated into the original conversations.
- [static let video: Conversation.Capabilities](conversation/capabilities/video.md)
  The conversation sends or displays video streams.
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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Conversation.Update](conversation/update.md)
  A type that describes new, changed, or deleted capabilities and attributes of a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/capabilities)*