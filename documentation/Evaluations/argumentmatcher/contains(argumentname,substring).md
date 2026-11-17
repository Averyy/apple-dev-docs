# ArgumentMatcher.contains(argumentName:substring:)

**Framework**: Evaluations  
**Kind**: case  
**Role**: Case

A value that indicates that the argument must be present and its string value must contain the specified substring.

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
case contains(argumentName: String, substring: String)
```

## Discussion

If the argument is an array, the matcher is satisfied when any string element contains the substring. Elements that aren’t strings are ignored.

```swift
.contains(argumentName: "subject", substring: "Lunch")             // "Lunch plans" matches
.contains(argumentName: "recipients", substring: "alice@")         // ["alice@example.com", "bob@example.com"] matches
```

## Parameters

- `argumentName`: The name of the argument to validate.
- `substring`: The substring the argument’s string value, or one of its string elements if the argument is an array, must contain.

## See Also

### String matching
- [case pattern(argumentName: String, regex: String)](./pattern%28argumentname,regex%29.md)
  A value that indicates that the argument must be present and its string value must match the specified regex pattern.
- [case hasPrefix(argumentName: String, prefix: String)](./hasprefix%28argumentname,prefix%29.md)
  A value that indicates that the argument must be present and its string value must start with the specified prefix.
- [case hasSuffix(argumentName: String, suffix: String)](./hassuffix%28argumentname,suffix%29.md)
  A value that indicates that the argument must be present and its string value must end with the specified suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/argumentmatcher/contains(argumentname:substring:))*