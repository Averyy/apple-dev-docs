# ArgumentMatcher.range(argumentName:minimum:maximum:)

**Framework**: Evaluations  
**Kind**: case

A value that indicates that the argument must be present and its numeric value must be within the specified range.

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
case range(argumentName: String, minimum: Double?, maximum: Double?)
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

## Parameters

- `argumentName`: The name of the argument to validate.
- `minimum`: The lower bound of the allowed range, or `nil` for no lower bound.
- `maximum`: The upper bound of the allowed range, or `nil` for no upper bound.

## See Also

- [case oneOf(argumentName: String, allowedValues: [ArgumentValue])](argumentmatcher/oneof(argumentname:allowedvalues:).md)
  A value that indicates the argument must be present with a value that matches one of the allowed values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/range(argumentname:minimum:maximum:))*