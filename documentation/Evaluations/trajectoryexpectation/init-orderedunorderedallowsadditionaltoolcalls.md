# init(ordered:unordered:allowsAdditionalToolCalls:)

**Framework**: Evaluations  
**Kind**: init

Creates a trajectory expectation with ordered and unordered requirements, and controls whether unmatched tool calls are permitted.

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
init(ordered: [ToolExpectation] = [], unordered: [ToolExpectation] = [], allowsAdditionalToolCalls: Bool = true)
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Discussion

Use this initializer when you want to control the blanket policy for unexpected tool calls. To forbid specific tools instead, use [`init(ordered:unordered:disallowed:)`](trajectoryexpectation/init(ordered:unordered:disallowed:).md).

## Parameters

- `ordered`: Steps that must be satisfied in sequential order.
- `unordered`: Tool calls that must occur at some point, regardless of position.
- `allowsAdditionalToolCalls`: A Boolean value indicating whether to allow tool calls that don’t match any expectation; defaults to `true`

## See Also

- [init(ordered: [ToolExpectation], unordered: [ToolExpectation], disallowed: [ToolExpectation])](trajectoryexpectation/init(ordered:unordered:disallowed:).md)
  Creates a trajectory expectation with ordered and unordered requirements, plus specific tools that the model must not call.
- [init(unordered: [ToolExpectation])](trajectoryexpectation/init(unordered:).md)
  Creates a trajectory expectation with only unordered requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/init(ordered:unordered:allowsadditionaltoolcalls:))*