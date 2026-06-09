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

- [macro ComputedProperty()](computedproperty().md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource)](computedproperty(title:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(indexingkey:).md)
  A macro that adds a computed app entity property with get and set accessors.
- [macro ComputedProperty(customIndexingKey: CSCustomAttributeKey)](computedproperty(customindexingkey:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](computedproperty(title:customindexingkey:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(title:indexingkey:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro DeferredProperty()](deferredproperty().md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource)](deferredproperty(title:).md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](deferredproperty(indexingkey:).md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](deferredproperty(title:indexingkey:).md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [class EntityProperty](entityproperty.md)
  A property wrapper that exposes the associated property to the system.
- [struct EntityPropertyModifiers](entitypropertymodifiers.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/property-comparators)*