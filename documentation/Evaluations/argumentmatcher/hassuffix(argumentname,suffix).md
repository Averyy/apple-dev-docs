# ArgumentMatcher.hasSuffix(argumentName:suffix:)

**Framework**: Evaluations  
**Kind**: case  
**Role**: Case

A value that indicates that the argument must be present and its string value must end with the specified suffix.

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
case hasSuffix(argumentName: String, suffix: String)
```

## Parameters

- `argumentName`: The name of the argument to validate.
- `suffix`: The string the argument’s value must end with.

## See Also

### String matching
- [case pattern(argumentName: String, regex: String)](./pattern%28argumentname,regex%29.md)
  A value that indicates that the argument must be present and its string value must match the specified regex pattern.
- [case contains(argumentName: String, substring: String)](./contains%28argumentname,substring%29.md)
  A value that indicates that the argument must be present and its string value must contain the specified substring.
- [case hasPrefix(argumentName: String, prefix: String)](./hasprefix%28argumentname,prefix%29.md)
  A value that indicates that the argument must be present and its string value must start with the specified prefix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/hassuffix(argumentname:suffix:))*