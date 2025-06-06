# PredicateBindings

**Framework**: Foundation  
**Kind**: struct

A mapping from a predicates’s input variables to their values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct PredicateBindings
```

#### Overview

If you define a custom predicate expression type, you must propagate the predicate’s bindings to its subexpressions.

If you define a custom predicate type, you must create an instance of this structure, populate it with the predicate’s variables, and propagate it throughout the expression tree.

## Topics

### Initializers
- [init<each T>(repeat (PredicateExpressions.Variable<each T>, each T))](predicatebindings/init(_:).md)
### Instance Methods
- [func binding<T>(PredicateExpressions.Variable<T>, to: T) -> PredicateBindings](predicatebindings/binding(_:to:).md)
### Subscripts
- [subscript<T>(PredicateExpressions.Variable<T>) -> T?](predicatebindings/subscript(_:).md)

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
- [class NSPredicate](nspredicate.md)
  A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [class NSExpression](nsexpression.md)
  An expression for use in a comparison predicate.
- [class NSComparisonPredicate](nscomparisonpredicate.md)
  A specialized predicate for comparing expressions.
- [class NSCompoundPredicate](nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicatebindings)*