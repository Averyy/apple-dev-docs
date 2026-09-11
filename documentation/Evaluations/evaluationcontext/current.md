# current

**Framework**: Evaluations  
**Kind**: property

The current evaluation context within the active test scope.

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
static var current: EvaluationContext { get }
```

#### Discussion

Accessing this property outside an evaluation scope triggers a fatal error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationcontext/current)*