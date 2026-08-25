# ordered

**Framework**: Evaluations  
**Kind**: property

Tool call steps that must be satisfied in sequential order.

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
var ordered: [ToolExpectation]
```

#### Discussion

Each entry is either a single [`ToolExpectation`](toolexpectation.md) or an [`anyOrder(_:)`](toolexpectation/anyorder(_:).md) group where multiple tools must all be called at that position (in any relative order).

## See Also

- [var unordered: [ToolExpectation]](trajectoryexpectation/unordered.md)
  Tool calls that must occur at some point, regardless of position.
- [var disallowed: [ToolExpectation]](trajectoryexpectation/disallowed.md)
  Tools that the model must NOT call.
- [var allowsAdditionalCalls: Bool](trajectoryexpectation/allowsadditionalcalls.md)
  A Boolean value that indicates whether to allow tool calls that don’t match any expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/ordered)*