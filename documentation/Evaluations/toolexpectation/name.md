# name

**Framework**: Evaluations  
**Kind**: property

The name of the tool that the evaluation expects the model to call.

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
var name: String { get }
```

#### Discussion

This is only valid for single expectations. Accessing this on an [`anyOrder(_:)`](toolexpectation/anyorder(_:).md) group is a programming error.

## See Also

- [var arguments: [ArgumentMatcher]](toolexpectation/arguments.md)
  The argument matchers to validate against the tool call.
- [var isAnyOrderGroup: Bool](toolexpectation/isanyordergroup.md)
  A Boolean value that indicates whether this expectation represents a group of expectations that can be satisfied in any order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/name)*