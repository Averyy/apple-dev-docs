# stringByReplacingMatches(in:options:range:withTemplate:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new string containing matching regular expressions replaced with the template string.

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
func stringByReplacingMatches(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange, withTemplate templ: String) -> String
```

```objc
- (NSString *) stringByReplacingMatchesInString:(NSString *) string options:(NSMatchingOptions) options range:(NSRange) range withTemplate:(NSString *) templ;
```

#### Return Value

A string with matching regular expressions replaced by the template string.

#### Discussion

See [Flag Options](../nsregularexpression.md#Flag-Options) for the format of `templ`.

## Parameters

- `string`: The string to search for values within.
- `options`: The matching options to use. See [`NSRegularExpression.MatchingOptions`](./matchingoptions.md) for possible values.
- `range`: The range of the string to search.
- `templ`: The substitution template used when replacing matching instances.

## See Also

### Replacing Strings Using Regular Expressions
- [func replaceMatches(in: NSMutableString, options: NSRegularExpression.MatchingOptions, range: NSRange, withTemplate: String) -> Int](./replacematches%28in,options,range,withtemplate%29.md)
  Replaces regular expression matches within the mutable string using the template string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/stringbyreplacingmatches(in:options:range:withtemplate:))*