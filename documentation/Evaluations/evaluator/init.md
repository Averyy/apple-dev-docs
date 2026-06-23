# init(_:)

**Framework**: Evaluations  
**Kind**: init

Creates an evaluator with the given evaluation closure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ evaluate: nonisolated(nonsending) @escaping (Input, ModelSubject<Input.ExpectedValue>) async throws -> Metric)
```

## Parameters

- `evaluate`: A closure that receives the input and subject, and returns a [`Metric`](metric.md) with a result value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluator/init(_:))*