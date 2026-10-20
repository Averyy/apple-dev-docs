# NSRegularExpression.MatchingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSMatchingOptions : NSUInteger;
```

## Topics

### Constants
- [static var reportProgress: NSRegularExpression.MatchingOptions](./matchingoptions/reportprogress.md)
  Call the Block periodically during long-running match operations. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md). See [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
- [static var reportCompletion: NSRegularExpression.MatchingOptions](./matchingoptions/reportcompletion.md)
  Call the Block once after the completion of any matching. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md). See [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
- [static var anchored: NSRegularExpression.MatchingOptions](./matchingoptions/anchored.md)
  Specifies that matches are limited to those at the start of the search range. See [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
- [static var withTransparentBounds: NSRegularExpression.MatchingOptions](./matchingoptions/withtransparentbounds.md)
  Specifies that matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
- [static var withoutAnchoringBounds: NSRegularExpression.MatchingOptions](./matchingoptions/withoutanchoringbounds.md)
  Specifies that `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
### Initializers
- [init(rawValue: UInt)](./matchingoptions/init%28rawvalue%29.md)

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
- [NSRegularExpression.Options](./options-swift.struct.md)
  These constants define the regular expression options. These constants are used by the property [`options`](./options-swift.property.md), [`regularExpressionWithPattern:options:error:`](./regularexpressionwithpattern_options_error_.md), and [`init(pattern:options:)`](./init%28pattern,options%29.md).
- [NSRegularExpression.MatchingFlags](./matchingflags.md)
  Set by the Block as the matching progresses, completes, or fails. Used by the method [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingoptions)*