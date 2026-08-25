# allowsAdditionalCalls

**Framework**: Evaluations  
**Kind**: property

A Boolean value that indicates whether to allow tool calls that don’t match any expectation.

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
var allowsAdditionalCalls: Bool
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Discussion

When `false`, any unmatched tool call causes evaluation to fail. When `true` (the default), unmatched calls are ignored as long as all expectations are met.

## See Also

- [var ordered: [ToolExpectation]](trajectoryexpectation/ordered.md)
  Tool call steps that must be satisfied in sequential order.
- [var unordered: [ToolExpectation]](trajectoryexpectation/unordered.md)
  Tool calls that must occur at some point, regardless of position.
- [var disallowed: [ToolExpectation]](trajectoryexpectation/disallowed.md)
  Tools that the model must NOT call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/allowsadditionalcalls)*