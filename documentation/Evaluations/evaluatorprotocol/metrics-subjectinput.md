# metrics(subject:input:)

**Framework**: Evaluations  
**Kind**: method  
**Required**: Yes

Computes metrics for the given subject, given the input sample.

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
(nonsending) func metrics(subject: Self.Subject, input: Self.Input) async throws -> [Metric]
```

#### Return Value

An array of metrics this evaluator produces.

## Parameters

- `subject`: The subject of evaluation, which the evaluation’s `subject(from:)` method produces.
- `input`: The input sample that contains the expected value and other context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorprotocol/metrics(subject:input:))*