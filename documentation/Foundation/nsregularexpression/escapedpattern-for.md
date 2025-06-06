# escapedPattern(for:)

**Framework**: Foundation  
**Kind**: method

Returns a string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func escapedPattern(for string: String) -> String
```

#### Return Value

The escaped string.

#### Discussion

Returns a string by adding backslash escapes as necessary to the given string, to escape any characters that would otherwise be treated as pattern metacharacters. You typically use this method to match on a particular string within a larger pattern.

For example, the string `"(N/A)"` contains the pattern metacharacters `(`, `/`, and `)`. The result of adding backslash escapes to this string is `"\\(N\\/A\\)"`.

## Parameters

- `string`: The string.

## See Also

- [class func escapedTemplate(for: String) -> String](nsregularexpression/escapedtemplate(for:).md)
  Returns a template string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/escapedpattern(for:))*