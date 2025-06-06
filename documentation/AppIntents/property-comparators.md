# Property comparators

**Framework**: App Intents

Specify the type of comparison to perform during a property-matched query.

## Topics

### Equatable comparisons
- [class EqualToComparator](equaltocomparator.md)
  An object that determines whether the value of an equatable property is equal to the specified value.
- [class NotEqualToComparator](notequaltocomparator.md)
  An object that determines whether the value of an equatable property is not equal to the specified value.
- [class GreaterThanComparator](greaterthancomparator.md)
  An object that determines whether the value of a comparable property is greater than the specified value.
- [class GreaterThanOrEqualToComparator](greaterthanorequaltocomparator.md)
  An object that determines whether the value of a comparable property is greater than or equal to the specified value.
- [class LessThanComparator](lessthancomparator.md)
  An object that determines whether the value of a comparable property is less than the specified value.
- [class LessThanOrEqualToComparator](lessthanorequaltocomparator.md)
  An object that determines whether the value of a comparable property is less than or equal to the specified value.
- [class IsBetweenComparator](isbetweencomparator.md)
  This comparator is only supported for `Date` types in Shortcuts.
### String comparisons
- [class HasPrefixComparator](hasprefixcomparator.md)
  An object that determines whether the value of a string property has the specified prefix.
- [class HasSuffixComparator](hassuffixcomparator.md)
  An object that determines whether the value of a string property has the specified suffix.
- [enum StringComparisonOperator](stringcomparisonoperator.md)
### Containment comparisons
- [class ContainsComparator](containscomparator.md)
  An object that determines whether the value of sequence property contains the specified value.

## See Also

- [protocol EntityPropertyQuery](entitypropertyquery.md)
  An interface for locating entities by matching values against one or more of their properties.
- [struct EntityQueryProperties](entityqueryproperties.md)
  A type that provides the properties to include in a property-matched query.
- [class EntityQueryProperty](entityqueryproperty.md)
  An object that provides the supported comparators you use to describe the different ways users can query against a property of an app entity.
- [struct EntityQuerySortingOptions](entityquerysortingoptions.md)
  The potential properties you can use to sort the results of a query.
- [struct EntityQuerySortableByProperty](entityquerysortablebyproperty.md)
  Details about a specific property you use to sort the query results.
- [struct EntityQuerySort](entityquerysort.md)
  The properties to use to sort the results when the query runs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/property-comparators)*