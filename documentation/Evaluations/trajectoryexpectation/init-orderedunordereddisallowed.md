# init(ordered:unordered:disallowed:)

**Framework**: Evaluations  
**Kind**: init

Creates a trajectory expectation with ordered and unordered requirements, plus specific tools that the agent must not call.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(ordered: [ToolExpectation] = [], unordered: [ToolExpectation] = [], disallowed: [ToolExpectation])
```

#### Discussion

Additional tool calls beyond the expected ones are always allowed when using disallowed expectations — the disallowed list targets specific tools while permitting everything else. To disallow *all* unexpected calls instead, use [`init(ordered:unordered:allowsAdditionalToolCalls:)`](trajectoryexpectation/init(ordered:unordered:allowsadditionaltoolcalls:).md) with `allowsAdditionalToolCalls: false`.

## Parameters

- `ordered`: Steps that must be satisfied in sequential order.
- `unordered`: Tool calls that must occur at some point, regardless of position.
- `disallowed`: Tools that the agent must not call.

## See Also

- [init(ordered: [ToolExpectation], unordered: [ToolExpectation], allowsAdditionalToolCalls: Bool)](trajectoryexpectation/init(ordered:unordered:allowsadditionaltoolcalls:).md)
  Creates a trajectory expectation with ordered and unordered requirements, and controls whether unmatched tool calls are permitted.
- [init(unordered: [ToolExpectation])](trajectoryexpectation/init(unordered:).md)
  Creates a trajectory expectation with only unordered requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/init(ordered:unordered:disallowed:))*