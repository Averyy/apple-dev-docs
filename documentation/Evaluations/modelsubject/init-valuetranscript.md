# init(value:transcript:)

**Framework**: Evaluations  
**Kind**: init

Creates a model subject with a value and optional transcript.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(value: Value, transcript: StructuredTranscript? = nil)
```

## Parameters

- `value`: The typed value produced by the model.
- `transcript`: The structured transcript from the model session. Required for tool call evaluations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/modelsubject/init(value:transcript:))*