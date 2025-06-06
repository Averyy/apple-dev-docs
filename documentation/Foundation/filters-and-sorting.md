# Filters and Sorting

**Framework**: Foundation

Use predicates, expressions, and sort descriptors to examine elements in collections and other services.

## Topics

### Filltering
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
- [class NSCompoundPredicate](nscompoundpredicate.md)
  A specialized predicate that evaluates logical combinations of other predicates.
### Sorting
- [class NSSortDescriptor](nssortdescriptor.md)
  An immutable description of how to order a collection of objects according to a property common to all the objects.
- [enum ComparisonResult](comparisonresult.md)
  Constants that indicate sort order.
- [struct SortDescriptor](sortdescriptor.md)
  A serializable description of how to sort numerics and strings.
- [protocol SortComparator](sortcomparator.md)
  A comparison algorithm for a specified type.
- [struct ComparableComparator](comparablecomparator.md)
  A comparator that compares types according to their conformance to the comparable protocol.
- [struct KeyPathComparator](keypathcomparator.md)
  A comparator that uses another sort comparator to provide the comparison of values at a key path.
- [enum SortOrder](sortorder.md)
  The orderings that you can perform sorts with.

## See Also

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md)
  Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md)
  Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filters-and-sorting)*