# ArgumentMatcher.pattern(argumentName:regex:)

**Framework**: Evaluations  
**Kind**: case

A value that indicates that the argument must be present and its string value must match the specified regex pattern.

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
case pattern(argumentName: String, regex: String)
```

## Parameters

- `argumentName`: The name of the argument to validate.
- `regex`: The regular expression the argument’s string value must match.

## See Also

- [case contains(argumentName: String, substring: String)](argumentmatcher/contains(argumentname:substring:).md)
  A value that indicates that the argument must be present and its string value must contain the specified substring.
- [case hasPrefix(argumentName: String, prefix: String)](argumentmatcher/hasprefix(argumentname:prefix:).md)
  A value that indicates that the argument must be present and its string value must start with the specified prefix.
- [case hasSuffix(argumentName: String, suffix: String)](argumentmatcher/hassuffix(argumentname:suffix:).md)
  A value that indicates that the argument must be present and its string value must end with the specified suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/pattern(argumentname:regex:))*