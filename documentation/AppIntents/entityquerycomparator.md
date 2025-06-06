# EntityQueryComparator

**Framework**: App Intents  
**Kind**: class

The base class for all concrete entity query comparators.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class EntityQueryComparator<Property, PropertyType, InputType, ComparatorMappingType> where Property : EntityProperty<PropertyType>, PropertyType : _IntentValue, PropertyType : Sendable, InputType : _IntentValue
```

#### Overview

An entity query comparator specifies a particular query comparison that can be made against a [`EntityQueryProperty`](entityqueryproperty.md). For each query property comparator, `mappingTransform` maps the user-supplied `Value` at runtime into a `ComparatorMappingType` type of your choice.

The following example illustrates the declaration of a [`EntityQueryProperty`](entityqueryproperty.md) on a fictional `IntentPersonEntity` that allows finding entities by strict equality or prefix on the entity `firstName` property by defining its supported `EntityQueryComparator`s:

```swift
Property(\.$firstName) {
   EqualToComparator { value in
        // This is called at runtime with `value` being the user-supplied value.
        // For example, value would be: "John" when the user says:
        // "Hey Siri, find persons named John", given the appropriate mapping
        // in the application's Siri metadata.

        // This closure returns an object of type `ComparatorMappingType`. In the context of
        // a `EntityQuery`, every `EntityQueryComparator` must return the same output type,
        // which is the Query's `ComparatorMappingType`.
        return "firstName must be equal to \{value}"
   }
   HasPrefixComparator { "firstName must start with \{$0}" }
}
```

#### Resolvers

Additionally, you can supply a set of [`Resolver`](resolver.md)s to fine-tune how the system will transform a user’s supplied value into into the target `Value` type.

## Relationships

### Inherited By
- [ContainsComparator](containscomparator.md)
- [EqualToComparator](equaltocomparator.md)
- [GreaterThanComparator](greaterthancomparator.md)
- [GreaterThanOrEqualToComparator](greaterthanorequaltocomparator.md)
- [HasPrefixComparator](hasprefixcomparator.md)
- [HasSuffixComparator](hassuffixcomparator.md)
- [IsBetweenComparator](isbetweencomparator.md)
- [LessThanComparator](lessthancomparator.md)
- [LessThanOrEqualToComparator](lessthanorequaltocomparator.md)
- [NotEqualToComparator](notequaltocomparator.md)

## See Also

- [static func buildBlock(AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>...) -> [AnyEntityQueryComparator<Entity, Subject, Property, PropertyType, ComparatorMappingType>]](entityquerycomparatorsbuilder/buildblock(_:).md)
- [struct AnyEntityQueryComparator](anyentityquerycomparator.md)
  A type that erases the type information of the underlying query comparator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityquerycomparator)*