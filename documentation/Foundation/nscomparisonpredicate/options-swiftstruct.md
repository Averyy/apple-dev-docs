# NSComparisonPredicate.Options

**Framework**: Foundation  
**Kind**: struct

Constants that describe the possible types of string comparison for comparison predicates.

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

#### Overview

The system supports these options for `LIKE`, as well as all of the equality/comparison operators.

## Topics

### Constants
- [static var caseInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/caseinsensitive.md)
  A case-insensitive predicate.
- [static var diacriticInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/diacriticinsensitive.md)
  A diacritic-insensitive predicate.
- [static var normalized: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/normalized.md)
  A predicate that indicates you’ve preprocessed the strings to compare.
- [static var caseInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/caseinsensitive.md)
  A case-insensitive predicate.
- [static var diacriticInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/diacriticinsensitive.md)
  A diacritic-insensitive predicate.
- [static var normalized: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/normalized.md)
  A predicate that indicates you’ve preprocessed the strings to compare.
### Initializers
- [init(rawValue: UInt)](nscomparisonpredicate/options-swift.struct/init(rawvalue:).md)

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

- [var comparisonPredicateModifier: NSComparisonPredicate.Modifier](nscomparisonpredicate/comparisonpredicatemodifier.md)
  The comparison predicate modifier for the receiver.
- [NSComparisonPredicate.Modifier](nscomparisonpredicate/modifier.md)
  Constants that describe the possible types of modifier for a comparison predicate.
- [var customSelector: Selector?](nscomparisonpredicate/customselector.md)
  The selector for the receiver.
- [var rightExpression: NSExpression](nscomparisonpredicate/rightexpression.md)
  The right expression for the receiver.
- [var leftExpression: NSExpression](nscomparisonpredicate/leftexpression.md)
  The left expression for the receiver.
- [var options: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.property.md)
  The options to use for the receiver.
- [var predicateOperatorType: NSComparisonPredicate.Operator](nscomparisonpredicate/predicateoperatortype.md)
  The predicate type for the receiver.
- [NSComparisonPredicate.Operator](nscomparisonpredicate/operator.md)
  Defines the type of comparison for a comparison predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct)*