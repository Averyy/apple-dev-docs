# NSComparisonPredicate

**Framework**: Foundation  
**Kind**: class

A specialized predicate for comparing expressions.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSComparisonPredicate
```

#### Overview

Use comparison predicates to compare the results of two expressions. You create a comparison predicate with an operator, a left expression, and a right expression, and use instances of the [`NSExpression`](nsexpression.md) class to represent those expressions. When you evaluate the predicate, it returns a `BOOL` value as the result of invoking the operator with the results of evaluating the expressions.

## Topics

### Creating Comparison Predicates
- [Displaying searchable content by using a search controller](../UIKit/displaying-searchable-content-by-using-a-search-controller.md)
  Create a user interface with searchable content in a table view.
- [init(leftExpression: NSExpression, rightExpression: NSExpression, customSelector: Selector)](nscomparisonpredicate/init(leftexpression:rightexpression:customselector:).md)
  Creates a predicate that you form by combining specified left and right expressions using a specified selector.
- [init(leftExpression: NSExpression, rightExpression: NSExpression, modifier: NSComparisonPredicate.Modifier, type: NSComparisonPredicate.Operator, options: NSComparisonPredicate.Options)](nscomparisonpredicate/init(leftexpression:rightexpression:modifier:type:options:).md)
  Creates a predicate to a specified type that you form by combining specified left and right expressions using a specified modifier and options.
- [init?(coder: NSCoder)](nscomparisonpredicate/init(coder:).md)
  Creates a predicate by decoding from the coder you specify.
### Getting Information About a Comparison Predicate
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
- [NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct.md)
  Constants that describe the possible types of string comparison for comparison predicates.
- [var predicateOperatorType: NSComparisonPredicate.Operator](nscomparisonpredicate/predicateoperatortype.md)
  The predicate type for the receiver.
- [NSComparisonPredicate.Operator](nscomparisonpredicate/operator.md)
  Defines the type of comparison for a comparison predicate.

## Relationships

### Inherits From
- [NSPredicate](nspredicate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)

## See Also

- [struct Predicate](predicate.md)
  A logical condition used to test a set of input values for searching or filtering.
- [struct PredicateError](predicateerror.md)
  An error thrown while evaluating a predicate.
- [struct PredicateCodableConfiguration](predicatecodableconfiguration.md)
  A specification of the expected types and key paths found in an archived predicate.
- [protocol PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md)
  A type that provides the expected key paths found in an archived predicate.
- [protocol PredicateExpression](predicateexpression.md)
  A component expression that makes up part of a predicate.
- [protocol StandardPredicateExpression](standardpredicateexpression.md)
  A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [enum PredicateExpressions](predicateexpressions.md)
  The expressions that make up a predicate.
- [struct PredicateBindings](predicatebindings.md)
  A mapping from a predicates’s input variables to their values.
- [class NSPredicate](nspredicate.md)
  A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [class NSExpression](nsexpression.md)
  An expression for use in a comparison predicate.
- [class NSCompoundPredicate](nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate)*