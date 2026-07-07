# EvaluatorError.failed(evaluatorType:reason:)

**Framework**: Evaluations  
**Kind**: case

The evaluator threw. `evaluatorType` is the failing evaluator’s concrete type name; `reason` is the thrown error’s `localizedDescription`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case failed(evaluatorType: String, reason: String)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluatorerror/failed(evaluatortype:reason:))*