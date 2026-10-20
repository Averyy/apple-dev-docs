# arguments

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

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

Returns an empty array for [`anyOrder(_:)`](./anyorder%28_%29.md) groups.

## See Also

### Accessing expectation details
- [var name: String](./name.md)
  The name of the tool that the evaluation expects the model to call.
- [var isAnyOrderGroup: Bool](./isanyordergroup.md)
  A Boolean value that indicates whether this expectation represents a group of expectations that can be satisfied in any order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/arguments)*