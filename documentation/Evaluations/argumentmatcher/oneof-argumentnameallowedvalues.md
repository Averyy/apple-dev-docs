# ArgumentMatcher.oneOf(argumentName:allowedValues:)

**Framework**: Evaluations  
**Kind**: case

A value that indicates the argument must be present with a value that matches one of the allowed values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case oneOf(argumentName: String, allowedValues: [ArgumentValue])
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

## See Also

- [case range(argumentName: String, minimum: Double?, maximum: Double?)](argumentmatcher/range(argumentname:minimum:maximum:).md)
  A value that indicates that the argument must be present and its numeric value must be within the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/oneof(argumentname:allowedvalues:))*