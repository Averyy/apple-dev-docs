# init(expected:arguments:)

**Framework**: Evaluations  
**Kind**: init

Creates a trajectory expectation for a single expected tool call.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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