# ArgumentMatcher.exact(argumentName:value:)

**Framework**: Evaluations  
**Kind**: case

A value that indicates that the argument must be present with this exact key and value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
case exact(argumentName: String, value: ArgumentValue)
```

## Mentions

- [Evaluating tool-calling behavior](evaluating-tool-calling-behavior.md)

## Parameters

- `argumentName`: The name of the argument to validate.
- `value`: The exact value the argument must equal.

## See Also

- [ArgumentMatcher.keyOnly(argumentName:)](argumentmatcher/keyonly(argumentname:).md)
  A value that indicates that the argument must be present with this key and no specific value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/exact(argumentname:value:))*