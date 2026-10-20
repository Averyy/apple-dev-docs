# ArgumentMatcher.oneOf(argumentName:allowedValues:)

**Framework**: Evaluations  
**Kind**: case  
**Role**: Case

A value that indicates the argument must be present with a value that matches one of the allowed values.

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
case oneOf(argumentName: String, allowedValues: [ArgumentValue])
```

## Mentions

- [Evaluating tool-calling behavior](../evaluating-tool-calling-behavior.md)

## Parameters

- `argumentName`: The name of the argument to validate.
- `allowedValues`: The set of values the argument must match one of.

## See Also

### Set and range matching
- [case range(argumentName: String, minimum: Double?, maximum: Double?)](./range%28argumentname,minimum,maximum%29.md)
  A value that indicates that the argument must be present and its numeric value must be within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/oneof(argumentname:allowedvalues:))*