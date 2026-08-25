# hasFailures

**Framework**: Evaluations  
**Kind**: property

Whether this represents any failure worth persisting.

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
var hasFailures: Bool { get }
```

#### Discussion

A clean run is all-zero, produced inference, and referenced no missing metrics. Used to decide whether to write the error summary when serializing — a clean run omits it entirely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluationrunerrors/hasfailures)*