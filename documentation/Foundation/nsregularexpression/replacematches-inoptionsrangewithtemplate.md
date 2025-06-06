# replaceMatches(in:options:range:withTemplate:)

**Framework**: Foundation  
**Kind**: method

Replaces regular expression matches within the mutable string using the template string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func replaceMatches(in string: NSMutableString, options: NSRegularExpression.MatchingOptions = [], range: NSRange, withTemplate templ: String) -> Int
```

#### Return Value

The number of matches.

#### Discussion

See [`Flag Options`](nsregularexpression#Flag-Options.md) for the format of `templ`.

## Parameters

- `string`: The mutable string to search and replace values within.
- `options`: The matching options to use. See   for possible values.
- `range`: The range of the string to search.
- `templ`: The substitution template used when replacing matching instances.

## See Also

- [func stringByReplacingMatches(in: String, options: NSRegularExpression.MatchingOptions, range: NSRange, withTemplate: String) -> String](nsregularexpression/stringbyreplacingmatches(in:options:range:withtemplate:).md)
  Returns a new string containing matching regular expressions replaced with the template string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/replacematches(in:options:range:withtemplate:))*