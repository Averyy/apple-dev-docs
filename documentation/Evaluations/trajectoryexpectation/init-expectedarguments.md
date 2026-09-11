# init(expected:arguments:)

**Framework**: Evaluations  
**Kind**: init

Creates a trajectory expectation for a single expected tool call.

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
init(expected toolName: String, arguments: [ArgumentMatcher] = [])
```

## Parameters

- `toolName`: The name of the tool expected to be called.
- `arguments`: The argument matchers to validate.

## See Also

- [struct ToolExpectation](toolexpectation.md)
  A specification for an expected tool call, or a group of expectations that can be satisfied in any order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation/init(expected:arguments:))*