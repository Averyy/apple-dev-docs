# NSComparisonPredicate.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSComparisonPredicateOptions : NSUInteger;
```

#### Overview

The system supports these options for `LIKE`, as well as all of the equality/comparison operators.

## Topics

### Constants
- [static var caseInsensitive: NSComparisonPredicate.Options](./options-swift.struct/caseinsensitive.md)
  A case-insensitive predicate.
- [static var diacriticInsensitive: NSComparisonPredicate.Options](./options-swift.struct/diacriticinsensitive.md)
  A diacritic-insensitive predicate.
- [static var normalized: NSComparisonPredicate.Options](./options-swift.struct/normalized.md)
  A predicate that indicates you’ve preprocessed the strings to compare.
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

### Getting Information About a Comparison Predicate
- [var comparisonPredicateModifier: NSComparisonPredicate.Modifier](./comparisonpredicatemodifier.md)
  The comparison predicate modifier for the receiver.
- [NSComparisonPredicate.Modifier](./modifier.md)
  Constants that describe the possible types of modifier for a comparison predicate.
- [var customSelector: Selector?](./customselector.md)
  The selector for the receiver.
- [var rightExpression: NSExpression](./rightexpression.md)
  The right expression for the receiver.
- [var leftExpression: NSExpression](./leftexpression.md)
  The left expression for the receiver.
- [var options: NSComparisonPredicate.Options](./options-swift.property.md)
  The options to use for the receiver.
- [var predicateOperatorType: NSComparisonPredicate.Operator](./predicateoperatortype.md)
  The predicate type for the receiver.
- [NSComparisonPredicate.Operator](./operator.md)
  Defines the type of comparison for a comparison predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct)*