# init(ordered:unordered:disallowed:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a trajectory expectation with ordered and unordered requirements, plus specific tools that the model must not call.

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
init(ordered: [ToolExpectation] = [], unordered: [ToolExpectation] = [], disallowed: [ToolExpectation])
```

#### Discussion

Using disallowed expectations always allows additional tool calls; the disallowed list targets specific tools while permitting everything else. To disallow *all* unexpected calls instead, use [`init(ordered:unordered:allowsAdditionalToolCalls:)`](./init%28ordered,unordered,allowsadditionaltoolcalls%29.md) with `allowsAdditionalToolCalls: false`.

## Parameters

- `ordered`: Steps that must be satisfied in sequential order.
- `unordered`: Tool calls that must occur at some point, regardless of position.
- `disallowed`: Tools that the model must not call.

## See Also

### Creating multi-tool expectations
- [init(ordered: [ToolExpectation], unordered: [ToolExpectation], allowsAdditionalToolCalls: Bool)](./init%28ordered,unordered,allowsadditionaltoolcalls%29.md)
  Creates a trajectory expectation with ordered and unordered requirements, and controls whether unmatched tool calls are permitted.
- [init(unordered: [ToolExpectation])](./init%28unordered%29.md)
  Creates a trajectory expectation with only unordered requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/init(ordered:unordered:disallowed:))*