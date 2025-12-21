# applied(to:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Predicts cumulative human body action counts from a sequence of human body pose windows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func applied<S>(to input: S, eventHandler: EventHandler? = nil) async throws -> HumanBodyActionCounter.OutputSequence where S : TemporalSequence, S.Feature == [Pose]
```

#### Return Value

An async sequence of cumulative human body action counts.

## Parameters

- `input`: An async sequence of human body pose windows.
- `eventHandler`: An event handler.

## See Also

- [HumanBodyActionCounter.CumulativeSumSequence](humanbodyactioncounter/cumulativesumsequence.md)
  Cumulative human body action count sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/applied(to:eventhandler:))*