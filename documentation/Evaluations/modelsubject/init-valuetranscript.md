# init(value:transcript:)

**Framework**: Evaluations  
**Kind**: init

Creates a model subject with a value and optional transcript.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
init(value: Value, transcript: StructuredTranscript? = nil)
```

## Parameters

- `value`: The typed value produced by the model.
- `transcript`: The structured transcript from the model session. Required for tool call evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject/init(value:transcript:))*