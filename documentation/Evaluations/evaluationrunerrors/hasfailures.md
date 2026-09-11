# hasFailures

**Framework**: Evaluations  
**Kind**: property

Whether this represents any failure worth persisting.

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
var hasFailures: Bool { get }
```

#### Discussion

A clean run is all-zero, produced inference, and referenced no missing metrics. Used to decide whether to write the error summary when serializing — a clean run omits it entirely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationrunerrors/hasfailures)*