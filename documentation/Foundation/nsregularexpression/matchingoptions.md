# NSRegularExpression.MatchingOptions

**Framework**: Foundation  
**Kind**: struct

The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.

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
struct MatchingOptions
```

## Topics

### Constants
- [static var reportProgress: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/reportprogress.md)
  Call the Block periodically during long-running match operations. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md). See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var reportCompletion: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/reportcompletion.md)
  Call the Block once after the completion of any matching. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md). See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var anchored: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/anchored.md)
  Specifies that matches are limited to those at the start of the search range. See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var withTransparentBounds: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/withtransparentbounds.md)
  Specifies that matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var withoutAnchoringBounds: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/withoutanchoringbounds.md)
  Specifies that `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var reportProgress: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/reportprogress.md)
  Call the Block periodically during long-running match operations. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md). See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var reportCompletion: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/reportcompletion.md)
  Call the Block once after the completion of any matching. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md). See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var anchored: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/anchored.md)
  Specifies that matches are limited to those at the start of the search range. See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var withTransparentBounds: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/withtransparentbounds.md)
  Specifies that matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
- [static var withoutAnchoringBounds: NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions/withoutanchoringbounds.md)
  Specifies that `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md) for a description of the constant in context.
### Initializers
- [init(rawValue: UInt)](nsregularexpression/matchingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSRegularExpression.Options](nsregularexpression/options-swift.struct.md)
  These constants define the regular expression options. These constants are used by the property [`options`](nsregularexpression/options-swift.property.md), [`regularExpressionWithPattern:options:error:`](nsregularexpression/regularexpressionwithpattern:options:error:.md), and [`init(pattern:options:)`](nsregularexpression/init(pattern:options:).md).
- [NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags.md)
  Set by the Block as the matching progresses, completes, or fails. Used by the method [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingoptions)*