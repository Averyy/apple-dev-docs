# ArgumentMatcher.hasSuffix(argumentName:suffix:)

**Framework**: Evaluations  
**Kind**: case

A value that indicates that the argument must be present and its string value must end with the specified suffix.

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
case hasSuffix(argumentName: String, suffix: String)
```

## Parameters

- `argumentName`: The name of the argument to validate.
- `suffix`: The string the argument’s value must end with.

## See Also

- [case pattern(argumentName: String, regex: String)](argumentmatcher/pattern(argumentname:regex:).md)
  A value that indicates that the argument must be present and its string value must match the specified regex pattern.
- [case contains(argumentName: String, substring: String)](argumentmatcher/contains(argumentname:substring:).md)
  A value that indicates that the argument must be present and its string value must contain the specified substring.
- [case hasPrefix(argumentName: String, prefix: String)](argumentmatcher/hasprefix(argumentname:prefix:).md)
  A value that indicates that the argument must be present and its string value must start with the specified prefix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/hassuffix(argumentname:suffix:))*