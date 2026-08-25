# ArgumentMatcher.contains(argumentName:substring:)

**Framework**: Evaluations  
**Kind**: case

A value that indicates that the argument must be present and its string value must contain the specified substring.

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
case contains(argumentName: String, substring: String)
```

## Parameters

- `argumentName`: The name of the argument to validate.
- `substring`: The substring the argument’s string value must contain.

## See Also

- [case pattern(argumentName: String, regex: String)](argumentmatcher/pattern(argumentname:regex:).md)
  A value that indicates that the argument must be present and its string value must match the specified regex pattern.
- [case hasPrefix(argumentName: String, prefix: String)](argumentmatcher/hasprefix(argumentname:prefix:).md)
  A value that indicates that the argument must be present and its string value must start with the specified prefix.
- [case hasSuffix(argumentName: String, suffix: String)](argumentmatcher/hassuffix(argumentname:suffix:).md)
  A value that indicates that the argument must be present and its string value must end with the specified suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/contains(argumentname:substring:))*