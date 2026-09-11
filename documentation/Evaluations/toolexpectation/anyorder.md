# anyOrder(_:)

**Framework**: Evaluations  
**Kind**: method

Creates a group of expectations that must all be satisfied at the same sequential position, but can occur in any relative order.

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
static func anyOrder(_ expectations: [ToolExpectation]) -> ToolExpectation
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Discussion

You can only use this method within the `ordered` array of a [`TrajectoryExpectation`](trajectoryexpectation.md).

## Parameters

- `expectations`: The expectations that must all be satisfied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/anyorder(_:))*