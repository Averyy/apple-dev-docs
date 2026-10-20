# unordered

**Framework**: Evaluations  
**Kind**: property  
**Role**: Instance Property

Tool calls that must occur at some point, regardless of position.

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
var unordered: [ToolExpectation]
```

## See Also

### Combining expectations
- [var ordered: [ToolExpectation]](./ordered.md)
  Tool call steps that must be satisfied in sequential order.
- [var disallowed: [ToolExpectation]](./disallowed.md)
  Tools that the model must NOT call.
- [var allowsAdditionalCalls: Bool](./allowsadditionalcalls.md)
  A Boolean value that indicates whether to allow tool calls that don’t match any expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/unordered)*