# init(unordered:)

**Framework**: Evaluations  
**Kind**: init

Creates a trajectory expectation with only unordered requirements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(unordered: [ToolExpectation])
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Discussion

Additional calls are always allowed for unordered-only expectations.

## Parameters

- `unordered`: Tool calls that must occur at some point, regardless of position.

## See Also

- [init(ordered: [ToolExpectation], unordered: [ToolExpectation], allowsAdditionalToolCalls: Bool)](trajectoryexpectation/init(ordered:unordered:allowsadditionaltoolcalls:).md)
  Creates a trajectory expectation with ordered and unordered requirements, and controls whether unmatched tool calls are permitted.
- [init(ordered: [ToolExpectation], unordered: [ToolExpectation], disallowed: [ToolExpectation])](trajectoryexpectation/init(ordered:unordered:disallowed:).md)
  Creates a trajectory expectation with ordered and unordered requirements, plus specific tools that the agent must not call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/init(unordered:))*