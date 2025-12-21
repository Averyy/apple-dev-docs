# ignoreMetacharacters

**Framework**: Foundation  
**Kind**: property

Treat the entire pattern as a literal string.

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
static var ignoreMetacharacters: NSRegularExpression.Options { get }
```

## See Also

- [static var caseInsensitive: NSRegularExpression.Options](nsregularexpression/options-swift.struct/caseinsensitive.md)
  Match letters in the pattern independent of case.
- [static var allowCommentsAndWhitespace: NSRegularExpression.Options](nsregularexpression/options-swift.struct/allowcommentsandwhitespace.md)
  Ignore whitespace and #-prefixed comments in the pattern.
- [static var dotMatchesLineSeparators: NSRegularExpression.Options](nsregularexpression/options-swift.struct/dotmatcheslineseparators.md)
  Allow `.` to match any character, including line separators.
- [static var anchorsMatchLines: NSRegularExpression.Options](nsregularexpression/options-swift.struct/anchorsmatchlines.md)
  Allow `^` and `$` to match the start and end of lines.
- [static var useUnixLineSeparators: NSRegularExpression.Options](nsregularexpression/options-swift.struct/useunixlineseparators.md)
  Treat only `\n` as a line separator (otherwise, all standard line separators are used).
- [static var useUnicodeWordBoundaries: NSRegularExpression.Options](nsregularexpression/options-swift.struct/useunicodewordboundaries.md)
  Use Unicode `TR#29` to specify word boundaries (otherwise, traditional regular expression word boundaries are used).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.struct/ignoremetacharacters)*