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

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
  Enable people to configure app intents with their custom input values.
- [Parameter resolution](parameter-resolution.md)
  Define the required parameters for your app intents and specify how to resolve those parameters at runtime.
- [Resolvers](resolvers.md)
  Resolve the parameters of your app intents, and extend the standard resolution types to include your app’s custom types.
- [Common data types](common-data-types.md)
  Specify common types that your app supports, including currencies, files, and contacts.
- [App entities](app-entities.md)
  Make core types or concepts discoverable to the system by declaring them as app entities.
- [Static parameter types](app-enums.md)
  Types that represent an enumerable list of static parameter values.
- [Entity queries](entity-queries.md)
  Help the system find the entities your app defines and use them to resolve parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/property-comparators)*