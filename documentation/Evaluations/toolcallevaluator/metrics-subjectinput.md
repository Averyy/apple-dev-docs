# metrics(subject:input:)

**Framework**: Evaluations  
**Kind**: method

Evaluates tool-call expectations against the actual transcript and returns scored metrics.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func metrics(subject: ModelSubject<Input.ExpectedValue>, input: Input) async throws -> [Metric]
```

#### Return Value

An array that contains the strict pass or fail metric and the partial score metric.

#### Discussion

Runs ordered, unordered, and disallowed expectation checks in a single pass and returns both a strict all-pass metric and a partial percentage-pass metric.

## Parameters

- `subject`: The model subject that contains the transcript of actual tool calls.
- `input`: The sample providing the expected tool call trajectory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolcallevaluator/metrics(subject:input:))*