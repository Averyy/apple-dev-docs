# DynamicPropertyPath

**Framework**: App Intents Testing  
**Kind**: struct

A type-safe, dynamic path to access nested intent values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@dynamicMemberLookup
struct DynamicPropertyPath
```

#### Overview

You typically don’t create instances of `DynamicPropertyPath` directly. The system returns instances of the type to indicate that you can further traverse a nested property. Use `DynamicPropertyPath` for chained property access and array indexing on entities and intent results.

```swift
// Navigate nested properties.
let name: String = try entity.profile.name

// Index properties into an array.
let first: String = try entity.tags[0]

// Cast the entity to a known entity type definition.
let coffee: AnyAppEntity = try result.value.as(CoffeeEntity)
```

## Topics

### Instance Methods
- [func `as`<T>(T.Type) throws -> T](dynamicpropertypath/as(_:)-5po1a.md)
  Casts a property to the provided type.
- [func `as`<IntentType>(IntentType) throws -> IntentType.Instance](dynamicpropertypath/as(_:)-6n9rh.md)
  Casts the value to the given type.
### Subscripts
- [subscript(Int) -> (any IntentValueExpressing)?](dynamicpropertypath/subscript(_:)-1hj9z.md)
  Accesses a collection element by index, without casting.
- [subscript(Int) -> DynamicPropertyPath](dynamicpropertypath/subscript(_:)-4bof1.md)
  Accesses a nested property on a collection element by index.
- [subscript<T>(Int) -> T](dynamicpropertypath/subscript(_:)-kiay.md)
  Accesses a collection element by index, for comparison with a known value.
- [subscript(dynamicMember _: String) -> DynamicPropertyPath](dynamicpropertypath/subscript(dynamicmember:)-aj9z.md)
  Creates a dynamic path for navigating deeper into a nested property hierarchy.
- [subscript(dynamicMember _: String) -> (any IntentValueExpressing)?](dynamicpropertypath/subscript(dynamicmember:)-hqdv.md)
  Accesses a property by name without casting.
- [subscript<T>(dynamicMember _: String) -> T](dynamicpropertypath/subscript(dynamicmember:)-lizi.md)
  Accesses a typed property at the current path by name.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol AppIntentTypeDefinition](appintenttypedefinition.md)
  A protocol that associates a definition type with its corresponding instance type.
- [struct DynamicPropertyPathCollection](dynamicpropertypathcollection.md)
  Indexed result items from an intent value query.
- [struct IntentValuePropertiesCallable](intentvaluepropertiescallable.md)
  A callable wrapper that creates app intent instances from keyword arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath)*