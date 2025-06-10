# NSRegularExpression.MatchingFlags

**Framework**: Foundation  
**Kind**: struct

Set by the Block as the matching progresses, completes, or fails. Used by the method [`enumerateMatches(in:options:range:using:)`](nsregularexpression/enumeratematches(in:options:range:using:).md).

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

## Topics

### Constants
- [static var progress: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/progress.md)
  Set when the Block is called to report progress during a long-running match operation.
- [static var completed: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/completed.md)
  Set when the Block is called after matching has completed.
- [static var hitEnd: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/hitend.md)
  Set when the current match operation reached the end of the search range.
- [static var requiredEnd: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/requiredend.md)
  Set when the current match depended on the location of the end of the search range.
- [static var internalError: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/internalerror.md)
  Set when matching failed due to an internal error.
- [static var progress: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/progress.md)
  Set when the Block is called to report progress during a long-running match operation.
- [static var completed: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/completed.md)
  Set when the Block is called after matching has completed.
- [static var hitEnd: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/hitend.md)
  Set when the current match operation reached the end of the search range.
- [static var requiredEnd: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/requiredend.md)
  Set when the current match depended on the location of the end of the search range.
- [static var internalError: NSRegularExpression.MatchingFlags](nsregularexpression/matchingflags/internalerror.md)
  Set when matching failed due to an internal error.
### Initializers
- [init(rawValue: UInt)](nsregularexpression/matchingflags/init(rawvalue:).md)

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

- [NSRegularExpression.Options](nsregularexpression/options-swift.struct.md)
  These constants define the regular expression options. These constants are used by the property [`options`](nsregularexpression/options-swift.property.md), [`regularExpressionWithPattern:options:error:`](nsregularexpression/regularexpressionwithpattern:options:error:.md), and [`init(pattern:options:)`](nsregularexpression/init(pattern:options:).md).
- [NSRegularExpression.MatchingOptions](nsregularexpression/matchingoptions.md)
  The matching options constants specify the reporting, completion and matching rules to the expression matching methods. These constants are used by all methods that search for, or replace values, using a regular expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsregularexpression/matchingflags)*