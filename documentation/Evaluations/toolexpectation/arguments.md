# arguments

**Framework**: Evaluations  
**Kind**: property

The argument matchers to validate against the tool call.

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