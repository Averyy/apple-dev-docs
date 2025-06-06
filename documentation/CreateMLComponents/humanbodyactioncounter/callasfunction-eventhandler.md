# callAsFunction(_:eventHandler:)

**Framework**: Create ML Components  
**Kind**: method

Performs the transformation on an input sequence.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
func callAsFunction<S>(_ input: S, eventHandler: EventHandler? = nil) async throws -> Self.OutputSequence where S : TemporalSequence, Self.Input == S.Feature
```

#### Return Value

An async sequence produced by applying the transformation to the input.

## Parameters

- `input`: The input temporal sequence.
- `eventHandler`: An event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/callasfunction(_:eventhandler:))*