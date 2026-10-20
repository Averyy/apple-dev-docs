# reportCompletion

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Call the Block once after the completion of any matching. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](../enumeratematches%28in,options,range,using%29.md). See [`enumerateMatches(in:options:range:using:)`](../enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.

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
static var reportCompletion: NSRegularExpression.MatchingOptions { get }
```

```c
NSMatchingReportCompletion
```

## See Also

### Constants
- [static var reportProgress: NSRegularExpression.MatchingOptions](./reportprogress.md)
  Call the Block periodically during long-running match operations. This option has no effect for methods other than [`enumerateMatches(in:options:range:using:)`](../enumeratematches%28in,options,range,using%29.md). See [`enumerateMatches(in:options:range:using:)`](../enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
- [static var anchored: NSRegularExpression.MatchingOptions](./anchored.md)
  Specifies that matches are limited to those at the start of the search range. See [`enumerateMatches(in:options:range:using:)`](../enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
- [static var withTransparentBounds: NSRegularExpression.MatchingOptions](./withtransparentbounds.md)
  Specifies that matching may examine parts of the string beyond the bounds of the search range, for purposes such as word boundary detection, lookahead, etc. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](../enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.
- [static var withoutAnchoringBounds: NSRegularExpression.MatchingOptions](./withoutanchoringbounds.md)
  Specifies that `^` and `$` will not automatically match the beginning and end of the search range, but will still match the beginning and end of the entire string. This constant has no effect if the search range contains the entire string. See [`enumerateMatches(in:options:range:using:)`](../enumeratematches%28in,options,range,using%29.md) for a description of the constant in context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingoptions/reportcompletion)*