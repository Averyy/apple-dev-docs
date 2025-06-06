# PredicateExpressions

**Framework**: Foundation  
**Kind**: enum

The expressions that make up a predicate.

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
@frozen
enum PredicateExpressions
```

#### Overview

Don’t use this type directly.  When you call the `Predicate(_:)` macro in your code, the  expansion of that macro produces these values.

## Topics

### Structures
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
- [PredicateExpressions.PredicateRegex](predicateexpressions/predicateregex.md)
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
- [PredicateExpressions.VariableID](predicateexpressions/variableid.md)
### Type Methods
- [static func build_Arg<T>(T) -> PredicateExpressions.Value<T>](predicateexpressions/build_arg(_:)-2e8wt.md)
- [static func build_Arg<T>(T) -> T](predicateexpressions/build_arg(_:)-4nz6o.md)
- [static func build_Arg(some RegexComponent) -> PredicateExpressions.Value<PredicateExpressions.PredicateRegex>](predicateexpressions/build_arg(_:)-8jd6q.md)
- [static func build_Arithmetic<LHS, RHS>(lhs: LHS, rhs: RHS, op: PredicateExpressions.ArithmeticOperator) -> PredicateExpressions.Arithmetic<LHS, RHS>](predicateexpressions/build_arithmetic(lhs:rhs:op:).md)
- [static func build_ClosedRange<LHS, RHS>(lower: LHS, upper: RHS) -> PredicateExpressions.ClosedRange<LHS, RHS>](predicateexpressions/build_closedrange(lower:upper:).md)
- [static func build_Comparison<LHS, RHS>(lhs: LHS, rhs: RHS, op: PredicateExpressions.ComparisonOperator) -> PredicateExpressions.Comparison<LHS, RHS>](predicateexpressions/build_comparison(lhs:rhs:op:).md)
- [static func build_Conditional<Test, If, Else>(Test, If, Else) -> PredicateExpressions.Conditional<Test, If, Else>](predicateexpressions/build_conditional(_:_:_:).md)
- [static func build_Conjunction<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.Conjunction<LHS, RHS>](predicateexpressions/build_conjunction(lhs:rhs:).md)
- [static func build_Disjunction<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.Disjunction<LHS, RHS>](predicateexpressions/build_disjunction(lhs:rhs:).md)
- [static func build_Division<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.FloatDivision<LHS, RHS>](predicateexpressions/build_division(lhs:rhs:)-5mg1h.md)
- [static func build_Division<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.IntDivision<LHS, RHS>](predicateexpressions/build_division(lhs:rhs:)-958g1.md)
- [static func build_Equal<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.Equal<LHS, RHS>](predicateexpressions/build_equal(lhs:rhs:).md)
- [static func build_ForcedUnwrap<Inner, Wrapped>(Inner) -> PredicateExpressions.ForcedUnwrap<Inner, Wrapped>](predicateexpressions/build_forcedunwrap(_:).md)
- [static func build_KeyPath<Root, Value>(root: Root, keyPath: any KeyPath<Root.Output, Value> & Sendable) -> PredicateExpressions.KeyPath<Root, Value>](predicateexpressions/build_keypath(root:keypath:).md)
- [static func build_Negation<T>(T) -> PredicateExpressions.Negation<T>](predicateexpressions/build_negation(_:).md)
- [static func build_NilCoalesce<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.NilCoalesce<LHS, RHS>](predicateexpressions/build_nilcoalesce(lhs:rhs:).md)
- [static func build_NilLiteral<Wrapped>() -> PredicateExpressions.NilLiteral<Wrapped>](predicateexpressions/build_nilliteral.md)
- [static func build_NotEqual<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.NotEqual<LHS, RHS>](predicateexpressions/build_notequal(lhs:rhs:).md)
- [static func build_Range<LHS, RHS>(lower: LHS, upper: RHS) -> PredicateExpressions.Range<LHS, RHS>](predicateexpressions/build_range(lower:upper:).md)
- [static func build_Remainder<LHS, RHS>(lhs: LHS, rhs: RHS) -> PredicateExpressions.IntRemainder<LHS, RHS>](predicateexpressions/build_remainder(lhs:rhs:).md)
- [static func build_UnaryMinus<T>(T) -> PredicateExpressions.UnaryMinus<T>](predicateexpressions/build_unaryminus(_:).md)
- [static func build_allSatisfy<LHS, RHS>(LHS, (PredicateExpressions.Variable<LHS.Output.Element>) -> RHS) -> PredicateExpressions.SequenceAllSatisfy<LHS, RHS>](predicateexpressions/build_allsatisfy(_:_:).md)
- [static func build_caseInsensitiveCompare<Root, Other>(Root, Other) -> PredicateExpressions.StringCaseInsensitiveCompare<Root, Other>](predicateexpressions/build_caseinsensitivecompare(_:_:).md)
- [static func build_contains<Base, Other>(Base, Other) -> PredicateExpressions.CollectionContainsCollection<Base, Other>](predicateexpressions/build_contains(_:_:)-18oc3.md)
- [static func build_contains<LHS, RHS>(LHS, RHS) -> PredicateExpressions.SequenceContains<LHS, RHS>](predicateexpressions/build_contains(_:_:)-9bwzx.md)
- [static func build_contains<Subject, Regex>(Subject, Regex) -> PredicateExpressions.StringContainsRegex<Subject, Regex>](predicateexpressions/build_contains(_:_:)-9ferb.md)
- [static func build_contains<RangeExpression, Element>(RangeExpression, Element) -> PredicateExpressions.RangeExpressionContains<RangeExpression, Element>](predicateexpressions/build_contains(_:_:)-9ulrw.md)
- [static func build_contains<LHS, RHS>(LHS, where: (PredicateExpressions.Variable<LHS.Output.Element>) -> RHS) -> PredicateExpressions.SequenceContainsWhere<LHS, RHS>](predicateexpressions/build_contains(_:where:).md)
- [static func build_evaluate<Transformation, each Input, Output>(Transformation, repeat each Input) -> PredicateExpressions.ExpressionEvaluate<Transformation, repeat each Input, Output>](predicateexpressions/build_evaluate(_:_:)-33oeu.md)
- [static func build_evaluate<Condition, each Input>(Condition, repeat each Input) -> PredicateExpressions.PredicateEvaluate<Condition, repeat each Input>](predicateexpressions/build_evaluate(_:_:)-6h1h.md)
- [static func build_filter<LHS, RHS>(LHS, (PredicateExpressions.Variable<LHS.Output.Element>) -> RHS) -> PredicateExpressions.Filter<LHS, RHS>](predicateexpressions/build_filter(_:_:).md)
- [static func build_flatMap<LHS, RHS, Wrapped, Result>(LHS, (PredicateExpressions.Variable<Wrapped>) -> RHS) -> PredicateExpressions.OptionalFlatMap<LHS, Wrapped, RHS, Result>](predicateexpressions/build_flatmap(_:_:)-7d3x7.md)
- [static func build_flatMap<LHS, RHS, Wrapped, Result>(LHS, (PredicateExpressions.Variable<Wrapped>) -> RHS) -> PredicateExpressions.OptionalFlatMap<LHS, Wrapped, RHS, Result>](predicateexpressions/build_flatmap(_:_:)-kcbs.md)
- [static func build_localizedCompare<Root, Other>(Root, Other) -> PredicateExpressions.StringLocalizedCompare<Root, Other>](predicateexpressions/build_localizedcompare(_:_:).md)
- [static func build_localizedStandardContains<Root, Other>(Root, Other) -> PredicateExpressions.StringLocalizedStandardContains<Root, Other>](predicateexpressions/build_localizedstandardcontains(_:_:).md)
- [static func build_max<Elements>(Elements) -> PredicateExpressions.SequenceMaximum<Elements>](predicateexpressions/build_max(_:).md)
- [static func build_min<Elements>(Elements) -> PredicateExpressions.SequenceMinimum<Elements>](predicateexpressions/build_min(_:).md)
- [static func build_starts<Base, Prefix>(Base, with: Prefix) -> PredicateExpressions.SequenceStartsWith<Base, Prefix>](predicateexpressions/build_starts(_:with:).md)
- [static func build_subscript<Wrapped, Key, Value>(Wrapped, Key) -> PredicateExpressions.DictionaryKeySubscript<Wrapped, Key, Value>](predicateexpressions/build_subscript(_:_:)-61z8t.md)
- [static func build_subscript<Wrapped, Range>(Wrapped, Range) -> PredicateExpressions.CollectionRangeSubscript<Wrapped, Range>](predicateexpressions/build_subscript(_:_:)-8f5bl.md)
- [static func build_subscript<Wrapped, Index>(Wrapped, Index) -> PredicateExpressions.CollectionIndexSubscript<Wrapped, Index>](predicateexpressions/build_subscript(_:_:)-are7.md)
- [static func build_subscript<Wrapped, Key, Default>(Wrapped, Key, default: Default) -> PredicateExpressions.DictionaryKeyDefaultValueSubscript<Wrapped, Key, Default>](predicateexpressions/build_subscript(_:_:default:).md)
### Enumerations
- [PredicateExpressions.ArithmeticOperator](predicateexpressions/arithmeticoperator.md)
- [PredicateExpressions.ComparisonOperator](predicateexpressions/comparisonoperator.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/predicateexpressions)*