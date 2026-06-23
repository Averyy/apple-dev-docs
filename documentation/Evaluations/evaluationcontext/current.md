# current

**Framework**: Evaluations  
**Kind**: property

The current evaluation context within the active test scope.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var current: EvaluationContext { get }
```

#### Discussion

Accessing this property outside an evaluation scope triggers a fatal error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationcontext/current)*