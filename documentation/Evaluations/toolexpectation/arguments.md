# arguments

**Framework**: Evaluations  
**Kind**: property

The argument matchers to validate against the tool call.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var arguments: [ArgumentMatcher] { get }
```

#### Discussion

Returns an empty array for [`anyOrder(_:)`](toolexpectation/anyorder(_:).md) groups.

## See Also

- [var name: String](toolexpectation/name.md)
  The name of the tool that the evaluation expects the model to call.
- [var isAnyOrderGroup: Bool](toolexpectation/isanyordergroup.md)
  A Boolean value that indicates whether this expectation represents a group of expectations that can be satisfied in any order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/arguments)*