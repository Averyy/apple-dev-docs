# anyOrder(_:)

**Framework**: Evaluations  
**Kind**: method

Creates a group of expectations that must all be satisfied at the same sequential position, but can occur in any relative order.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func anyOrder(_ expectations: [ToolExpectation]) -> ToolExpectation
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

#### Discussion

Only valid within the `ordered` array of a [`TrajectoryExpectation`](trajectoryexpectation.md).

## Parameters

- `expectations`: The expectations that must all be satisfied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/toolexpectation/anyorder(_:))*