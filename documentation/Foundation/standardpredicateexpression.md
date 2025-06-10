# StandardPredicateExpression

**Framework**: Foundation  
**Kind**: protocol

A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.

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
protocol StandardPredicateExpression<Output> : PredicateExpression, Decodable, Encodable, Sendable
```

#### Overview

Don’t declare new types that conform to the `StandardPredicateExpression` protocol.  Only the types provided by Foundation are valid conforming types.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PredicateExpression](predicateexpression.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [PredicateExpressions.Arithmetic](predicateexpressions/arithmetic.md)
- [PredicateExpressions.ClosedRange](predicateexpressions/closedrange.md)
- [PredicateExpressions.CollectionContainsCollection](predicateexpressions/collectioncontainscollection.md)
- [PredicateExpressions.CollectionIndexSubscript](predicateexpressions/collectionindexsubscript.md)
- [PredicateExpressions.CollectionRangeSubscript](predicateexpressions/collectionrangesubscript.md)
- [PredicateExpressions.Comparison](predicateexpressions/comparison.md)
- [PredicateExpressions.Conditional](predicateexpressions/conditional.md)
- [PredicateExpressions.ConditionalCast](predicateexpressions/conditionalcast.md)
- [PredicateExpressions.Conjunction](predicateexpressions/conjunction.md)
- [PredicateExpressions.DictionaryKeyDefaultValueSubscript](predicateexpressions/dictionarykeydefaultvaluesubscript.md)
- [PredicateExpressions.DictionaryKeySubscript](predicateexpressions/dictionarykeysubscript.md)
- [PredicateExpressions.Disjunction](predicateexpressions/disjunction.md)
- [PredicateExpressions.Equal](predicateexpressions/equal.md)
- [PredicateExpressions.ExpressionEvaluate](predicateexpressions/expressionevaluate.md)
- [PredicateExpressions.Filter](predicateexpressions/filter.md)
- [PredicateExpressions.FloatDivision](predicateexpressions/floatdivision.md)
- [PredicateExpressions.ForceCast](predicateexpressions/forcecast.md)
- [PredicateExpressions.ForcedUnwrap](predicateexpressions/forcedunwrap.md)
- [PredicateExpressions.IntDivision](predicateexpressions/intdivision.md)
- [PredicateExpressions.IntRemainder](predicateexpressions/intremainder.md)
- [PredicateExpressions.KeyPath](predicateexpressions/keypath.md)
- [PredicateExpressions.Negation](predicateexpressions/negation.md)
- [PredicateExpressions.NilCoalesce](predicateexpressions/nilcoalesce.md)
- [PredicateExpressions.NilLiteral](predicateexpressions/nilliteral.md)
- [PredicateExpressions.NotEqual](predicateexpressions/notequal.md)
- [PredicateExpressions.OptionalFlatMap](predicateexpressions/optionalflatmap.md)
- [PredicateExpressions.PredicateEvaluate](predicateexpressions/predicateevaluate.md)
- [PredicateExpressions.Range](predicateexpressions/range.md)
- [PredicateExpressions.RangeExpressionContains](predicateexpressions/rangeexpressioncontains.md)
- [PredicateExpressions.SequenceAllSatisfy](predicateexpressions/sequenceallsatisfy.md)
- [PredicateExpressions.SequenceContains](predicateexpressions/sequencecontains.md)
- [PredicateExpressions.SequenceContainsWhere](predicateexpressions/sequencecontainswhere.md)
- [PredicateExpressions.SequenceMaximum](predicateexpressions/sequencemaximum.md)
- [PredicateExpressions.SequenceMinimum](predicateexpressions/sequenceminimum.md)
- [PredicateExpressions.SequenceStartsWith](predicateexpressions/sequencestartswith.md)
- [PredicateExpressions.StringCaseInsensitiveCompare](predicateexpressions/stringcaseinsensitivecompare.md)
- [PredicateExpressions.StringContainsRegex](predicateexpressions/stringcontainsregex.md)
- [PredicateExpressions.StringLocalizedCompare](predicateexpressions/stringlocalizedcompare.md)
- [PredicateExpressions.StringLocalizedStandardContains](predicateexpressions/stringlocalizedstandardcontains.md)
- [PredicateExpressions.TypeCheck](predicateexpressions/typecheck.md)
- [PredicateExpressions.UnaryMinus](predicateexpressions/unaryminus.md)
- [PredicateExpressions.Value](predicateexpressions/value.md)
- [PredicateExpressions.Variable](predicateexpressions/variable.md)

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
- [class NSCompoundPredicate](nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/standardpredicateexpression)*