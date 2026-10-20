# NSRegularExpression.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

These constants define the regular expression options. These constants are used by the property [`options`](./options-swift.property.md), [`regularExpressionWithPattern:options:error:`](./regularexpressionwithpattern_options_error_.md), and [`init(pattern:options:)`](./init%28pattern,options%29.md).

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

```c
enum NSRegularExpressionOptions : NSUInteger;
```

## Topics

### Constants
- [static var caseInsensitive: NSRegularExpression.Options](./options-swift.struct/caseinsensitive.md)
  Match letters in the pattern independent of case.
- [static var allowCommentsAndWhitespace: NSRegularExpression.Options](./options-swift.struct/allowcommentsandwhitespace.md)
  Ignore whitespace and #-prefixed comments in the pattern.
- [static var ignoreMetacharacters: NSRegularExpression.Options](./options-swift.struct/ignoremetacharacters.md)
  Treat the entire pattern as a literal string.
- [static var dotMatchesLineSeparators: NSRegularExpression.Options](./options-swift.struct/dotmatcheslineseparators.md)
  Allow `.` to match any character, including line separators.
- [static var anchorsMatchLines: NSRegularExpression.Options](./options-swift.struct/anchorsmatchlines.md)
  Allow `^` and `$` to match the start and end of lines.
- [static var useUnixLineSeparators: NSRegularExpression.Options](./options-swift.struct/useunixlineseparators.md)
  Treat only `\n` as a line separator (otherwise, all standard line separators are used).
- [static var useUnicodeWordBoundaries: NSRegularExpression.Options](./options-swift.struct/useunicodewordboundaries.md)
  Use Unicode `TR#29` to specify word boundaries (otherwise, traditional regular expression word boundaries are used).
### Initializers
- [init(rawValue: UInt)](./options-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NSRegularExpression.MatchingFlags](./matchingflags.md)
  Set by the Block as the matching progresses, completes, or fails. Used by the method [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md).
- [NSRegularExpression.MatchingOptions](./matchingoptions.md)
  The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/options-swift.struct)*