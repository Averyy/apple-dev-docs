# NSRegularExpression.MatchingFlags

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Set by the Block as the matching progresses, completes, or fails. Used by the method [`enumerateMatches(in:options:range:using:)`](./enumeratematches%28in,options,range,using%29.md).

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
struct MatchingFlags
```

```c
enum NSMatchingFlags : NSUInteger;
```

## Topics

### Constants
- [static var progress: NSRegularExpression.MatchingFlags](./matchingflags/progress.md)
  Set when the Block is called to report progress during a long-running match operation.
- [static var completed: NSRegularExpression.MatchingFlags](./matchingflags/completed.md)
  Set when the Block is called after matching has completed.
- [static var hitEnd: NSRegularExpression.MatchingFlags](./matchingflags/hitend.md)
  Set when the current match operation reached the end of the search range.
- [static var requiredEnd: NSRegularExpression.MatchingFlags](./matchingflags/requiredend.md)
  Set when the current match depended on the location of the end of the search range.
- [static var internalError: NSRegularExpression.MatchingFlags](./matchingflags/internalerror.md)
  Set when matching failed due to an internal error.
### Initializers
- [init(rawValue: UInt)](./matchingflags/init%28rawvalue%29.md)

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
- [NSRegularExpression.MatchingOptions](./matchingoptions.md)
  The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingflags)*