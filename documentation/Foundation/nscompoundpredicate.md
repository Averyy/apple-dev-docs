# NSCompoundPredicate

**Framework**: Foundation  
**Kind**: class

A specialized predicate that evaluates logical combinations of other predicates.

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
class NSCompoundPredicate
```

#### Overview

Use [`NSCompoundPredicate`](nscompoundpredicate.md) to create an `AND` or `OR` compound predicate of one or more other predicates, or the `NOT` of a single predicate. For the logical `AND` and `OR` operations:

- An `AND` predicate with no subpredicates evaluates to [`true`](https://developer.apple.com/documentation/swift/true).
- An `OR` predicate with no subpredicates evaluates to [`false`](https://developer.apple.com/documentation/swift/false).
- A compound predicate with one or more subpredicates evaluates to the truth of its subpredicates.

## Topics

### Creating Compound Predicates
- [init(andPredicateWithSubpredicates: [NSPredicate])](nscompoundpredicate/init(andpredicatewithsubpredicates:).md)
  Returns a new predicate that you form using an AND operation on the predicates in a specified array.
- [init(notPredicateWithSubpredicate: NSPredicate)](nscompoundpredicate/init(notpredicatewithsubpredicate:).md)
  Returns a new predicate that you form using a NOT operation on a specified predicate.
- [init(orPredicateWithSubpredicates: [NSPredicate])](nscompoundpredicate/init(orpredicatewithsubpredicates:).md)
  Returns a new predicate that you form using an OR operation on the predicates in a specified array.
- [init(type: NSCompoundPredicate.LogicalType, subpredicates: [NSPredicate])](nscompoundpredicate/init(type:subpredicates:).md)
  Returns the receiver that a specified type initializes using predicates from a specified array.
- [init?(coder: NSCoder)](nscompoundpredicate/init(coder:).md)
  Creates a predicate by decoding from the coder you specify.
### Getting Information About a Compound Predicate
- [var compoundPredicateType: NSCompoundPredicate.LogicalType](nscompoundpredicate/compoundpredicatetype.md)
  The predicate type for the receiver.
- [var subpredicates: [Any]](nscompoundpredicate/subpredicates.md)
  The receiver’s subpredicates.
- [NSCompoundPredicate.LogicalType](nscompoundpredicate/logicaltype.md)
  Constants that describe the possible types of a compound predicate.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class NSComparisonPredicate](nscomparisonpredicate.md)
  A specialized predicate for comparing expressions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscompoundpredicate)*