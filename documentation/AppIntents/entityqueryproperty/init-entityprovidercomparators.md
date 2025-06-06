# init(_:entityProvider:comparators:)

**Framework**: App Intents  
**Kind**: init

Initializes a EntityQueryProperty that applies to entity property at the provided keyPath.

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
init(_ keyPath: KeyPath<Subject, Property>, entityProvider: @escaping (Entity) -> Subject, @EntityQueryComparatorsBuilder<Entity, Subject, Property, PropertyType, ComparatorMappingType> comparators: () -> EntityQueryProperty<Entity, Subject, Property, PropertyType, ComparatorMappingType>.QueryComparators)
```

## Parameters

- `keyPath`: The keypath to the property that this EntityQueryProperty applies to. The target   property type determines which comparator modifiers will be available.
- `entityProvider`: Closure which, given a   instance, returns the appropriate    instance to apply  s to.
- `comparators`: The set of   that this property supports being queried by.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityqueryproperty/init(_:entityprovider:comparators:))*