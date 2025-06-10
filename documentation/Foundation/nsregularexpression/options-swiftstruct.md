# NSRegularExpression.Options

**Framework**: Foundation  
**Kind**: struct

These constants define the regular expression options. These constants are used by the property [`options`](nsregularexpression/options-swift.property.md), [`regularExpressionWithPattern:options:error:`](nsregularexpression/regularexpressionwithpattern:options:error:.md), and [`init(pattern:options:)`](nsregularexpression/init(pattern:options:).md).

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
struct Options
```

## Topics

### Constants
- [static var caseInsensitive: NSRegularExpression.Options](nsregularexpression/options-swift.struct/caseinsensitive.md)
  Match letters in the pattern independent of case.
- [static var allowCommentsAndWhitespace: NSRegularExpression.Options](nsregularexpression/options-swift.struct/allowcommentsandwhitespace.md)
  Ignore whitespace and #-prefixed comments in the pattern.
- [static var ignoreMetacharacters: NSRegularExpression.Options](nsregularexpression/options-swift.struct/ignoremetacharacters.md)
  Treat the entire pattern as a literal string.
- [static var dotMatchesLineSeparators: NSRegularExpression.Options](nsregularexpression/options-swift.struct/dotmatcheslineseparators.md)
  Allow `.` to match any character, including line separators.
- [static var anchorsMatchLines: NSRegularExpression.Options](nsregularexpression/options-swift.struct/anchorsmatchlines.md)
  Allow `^` and `$` to match the start and end of lines.
- [static var useUnixLineSeparators: NSRegularExpression.Options](nsregularexpression/options-swift.struct/useunixlineseparators.md)
  Treat only `\n` as a line separator (otherwise, all standard line separators are used).
- [static var useUnicodeWordBoundaries: NSRegularExpression.Options](nsregularexpression/options-swift.struct/useunicodewordboundaries.md)
  Use Unicode `TR#29` to specify word boundaries (otherwise, traditional regular expression word boundaries are used).
- [static var caseInsensitive: NSRegularExpression.Options](nsregularexpression/options-swift.struct/caseinsensitive.md)
  Match letters in the pattern independent of case.
- [static var allowCommentsAndWhitespace: NSRegularExpression.Options](nsregularexpression/options-swift.struct/allowcommentsandwhitespace.md)
  Ignore whitespace and #-prefixed comments in the pattern.
- [static var ignoreMetacharacters: NSRegularExpression.Options](nsregularexpression/options-swift.struct/ignoremetacharacters.md)
  Treat the entire pattern as a literal string.
- [static var dotMatchesLineSeparators: NSRegularExpression.Options](nsregularexpression/options-swift.struct/dotmatcheslineseparators.md)
  Allow `.` to match any character, including line separators.
- [static var anchorsMatchLines: NSRegularExpression.Options](nsregularexpression/options-swift.struct/anchorsmatchlines.md)
  Allow `^` and `$` to match the start and end of lines.
- [static var useUnixLineSeparators: NSRegularExpression.Options](nsregularexpression/options-swift.struct/useunixlineseparators.md)
  Treat only `\n` as a line separator (otherwise, all standard line separators are used).
- [static var useUnicodeWordBoundaries: NSRegularExpression.Options](nsregularexpression/options-swift.struct/useunicodewordboundaries.md)
  Use Unicode `TR#29` to specify word boundaries (otherwise, traditional regular expression word boundaries are used).
### Initializers
- [init(rawValue: UInt)](nsregularexpression/options-swift.struct/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags.md)
  Set by the Block as the matching progresses, completes, or fails. Used by the method [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md).
- [NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions.md)
  The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.struct)*