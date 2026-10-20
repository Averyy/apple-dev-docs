# name

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

The name of the tool that the evaluation expects the model to call.

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
var name: String { get }
```

#### Discussion

This is only valid for single expectations. Accessing this on an [`anyOrder(_:)`](./anyorder%28_%29.md) group is a programming error.

## See Also

### Accessing expectation details
- [var arguments: [ArgumentMatcher]](./arguments.md)
  The argument matchers to validate against the tool call.
- [var isAnyOrderGroup: Bool](./isanyordergroup.md)
  A Boolean value that indicates whether this expectation represents a group of expectations that can be satisfied in any order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/name)*