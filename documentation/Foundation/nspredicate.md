# NSPredicate

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.

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
class NSPredicate
```

```objc
@interface NSPredicate : NSObject
```

## Overview

Predicates represent logical conditions, which you can use to filter collections of objects. Although it’s common to create predicates directly from instances of [`NSComparisonPredicate`](./nscomparisonpredicate.md), [`NSCompoundPredicate`](./nscompoundpredicate.md), and [`NSExpression`](./nsexpression.md), you often create predicates from a format string that the class methods parse on [`NSPredicate`](./nspredicate.md). Examples of predicate format strings include:

- Simple comparisons, such as `grade == "7"` or `firstName like "Juan"`
- Case- and diacritic-insensitive lookups, such as `name contains[cd] "stein"`
- Logical operations, such as `(firstName like "Mei") OR (lastName like "Chen")`
- Temporal range constraints, such as `date between {$YESTERDAY, $TOMORROW}`
- Relational conditions, such as `group.name like "work*"`
- Aggregate operations, such as `@sum.items.price < 1000`

For a complete syntax reference, refer to the [Predicate Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html#//apple_ref/doc/uid/TP40001789).

You can also create predicates that include variables using the [`evaluate(with:substitutionVariables:)`](./nspredicate/evaluate%28with,substitutionvariables%29.md) method so that you can predefine the predicate before substituting concrete values at runtime.

## Topics

### Creating a Predicate
- [init(format: String, argumentArray: [Any]?)](./nspredicate/init%28format,argumentarray%29.md)
  Creates a predicate by substituting the values in a specified array into a format string and parsing the result.
- [init(format: String, arguments: CVaListPointer)](./nspredicate/init%28format,arguments%29.md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init(format: String, any CVarArg...)](./nspredicate/init%28format,_%29.md)
  Creates a predicate by substituting the values in an argument list into a format string and parsing the result.
- [convenience init?<Input>(Predicate<Input>)](./nspredicate/init%28_%29.md)
  Creates a predicate by converting an existing predicate.
- [func withSubstitutionVariables([String : Any]) -> Self](./nspredicate/withsubstitutionvariables%28_%29.md)
  Returns a copy of the predicate and substitutes the predicates variables with specified values from a specified substitution variables dictionary.
- [init(value: Bool)](./nspredicate/init%28value%29.md)
  Creates and returns a predicate that always evaluates to a specified Boolean value.
- [init(block: (Any?, [String : Any]?) -> Bool)](./nspredicate/init%28block%29.md)
  Creates a predicate that evaluates using a specified block object and bindings dictionary.
- [init?(fromMetadataQueryString: String)](./nspredicate/init%28frommetadataquerystring%29.md)
  Creates a predicate with a metadata query string.
- [+ predicateWithFormat:](./nspredicate/predicatewithformat_.md)
  Creates and returns a new predicate formed by creating a new string with a specified format and parsing the result.
### Evaluating a Predicate
- [func evaluate(with: Any?) -> Bool](./nspredicate/evaluate%28with%29.md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies.
- [func evaluate(with: Any?, substitutionVariables: [String : Any]?) -> Bool](./nspredicate/evaluate%28with,substitutionvariables%29.md)
  Returns a Boolean value that indicates whether the specified object matches the conditions that the predicate specifies after substituting in the values from a specified variables dictionary.
- [func allowEvaluation()](./nspredicate/allowevaluation%28%29.md)
  Forces a securely decoded predicate to allow evaluation.
### Getting a String Representation
- [var predicateFormat: String](./nspredicate/predicateformat.md)
  The predicate’s format string.
### Initializers
- [init?(coder: NSCoder)](./nspredicate/init%28coder%29.md)
### Instance Methods
- [func allowEvaluation(validator: any NSPredicateValidating) throws](./nspredicate/allowevaluation%28validator%29.md)
### Instance Variables
- [reserved](./nspredicate/reserved.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSComparisonPredicate](./nscomparisonpredicate.md)
- [NSCompoundPredicate](./nscompoundpredicate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Filltering
- [struct Predicate](./predicate.md)
  A logical condition used to test a set of input values for searching or filtering.
- [struct PredicateError](./predicateerror.md)
  An error thrown while evaluating a predicate.
- [struct PredicateCodableConfiguration](./predicatecodableconfiguration.md)
  A specification of the expected types and key paths found in an archived predicate.
- [protocol PredicateCodableKeyPathProviding](./predicatecodablekeypathproviding.md)
  A type that provides the expected key paths found in an archived predicate.
- [protocol PredicateExpression](./predicateexpression.md)
  A component expression that makes up part of a predicate.
- [protocol StandardPredicateExpression](./standardpredicateexpression.md)
  A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [enum PredicateExpressions](./predicateexpressions.md)
  The expressions that make up a predicate.
- [struct PredicateBindings](./predicatebindings.md)
  A mapping from a predicates’s input variables to their values.
- [class NSExpression](./nsexpression.md)
  An expression for use in a comparison predicate.
- [class NSComparisonPredicate](./nscomparisonpredicate.md)
  A specialized predicate for comparing expressions.
- [class NSCompoundPredicate](./nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspredicate)*