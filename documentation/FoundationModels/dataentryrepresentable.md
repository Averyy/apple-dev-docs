# DataEntryRepresentable

**Framework**: Foundation Models  
**Kind**: protocol

A type that a model can produce and represent as a top-level transcript entry.

**Availability**:
- iOS 27.2+ (Beta)
- iPadOS 27.2+ (Beta)
- Mac Catalyst 27.2+ (Beta)
- macOS 27.2+ (Beta)
- visionOS 27.2+ (Beta)
- watchOS 27.2+ (Beta)

## Declaration

```swift
protocol DataEntryRepresentable : Sendable
```

#### Overview

Conform to this protocol to describe how a value serializes into — and deserializes back from — a [`Transcript.DataEntry`](transcript/dataentry.md).

[`transcriptRepresentation`](dataentryrepresentable/transcriptrepresentation.md) is non-throwing: any fallible encoding should be surfaced from the conformer’s own initializer, where the developer is already deciding what input to accept. [`init(_:)`](dataentryrepresentable/init(_:).md) is throwing because the wire representation may come from a persisted transcript, from over the network, or from any source the conformer doesn’t control, and could be malformed. The asymmetry mirrors Foundation’s `String.init(data:encoding:)` (failable) and `String.utf8` (total).

## Topics

### Initializers
- [init(Transcript.DataEntry) throws](dataentryrepresentable/init(_:).md)
  Rehydrate this type from its transcript representation.
### Instance Properties
- [var transcriptRepresentation: Transcript.DataEntry](dataentryrepresentable/transcriptrepresentation.md)
  How this type appears when recorded in a session transcript.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/dataentryrepresentable)*