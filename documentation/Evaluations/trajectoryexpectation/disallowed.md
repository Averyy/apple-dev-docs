# disallowed

**Framework**: Evaluations  
**Kind**: property

Tools that the model must NOT call.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var disallowed: [ToolExpectation]
```

#### Discussion

If a disallowed expectation includes argument matchers, only calls matching those specific arguments trigger a failure — the model can still call the tool with different arguments.

## See Also

- [var ordered: [ToolExpectation]](trajectoryexpectation/ordered.md)
  Tool call steps that must be satisfied in sequential order.
- [var unordered: [ToolExpectation]](trajectoryexpectation/unordered.md)
  Tool calls that must occur at some point, regardless of position.
- [var allowsAdditionalCalls: Bool](trajectoryexpectation/allowsadditionalcalls.md)
  A Boolean value that indicates whether to allow tool calls that don’t match any expectation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/disallowed)*