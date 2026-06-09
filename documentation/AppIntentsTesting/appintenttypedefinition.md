# AppIntentTypeDefinition

**Framework**: App Intents Testing  
**Kind**: protocol

A protocol that associates a definition type with its corresponding instance type.

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
protocol AppIntentTypeDefinition
```

#### Overview

The `AppIntentTypeDefinition` bridges a definition type you use to retrieve your intent, entity, and enum type, and the type-erased instance of your concrete intent, entity, or enum. For example, `AppIntentTypeDefinition` bridges [`AppEntityDefinition`](appentitydefinition.md) to the [`AnyAppEntity`](anyappentity.md). Validate that a given instance was produced from the correct definition using the [`isInstance(_:)`](appintenttypedefinition/isinstance(_:).md) function.

## Topics

### Associated Types
- [associatedtype Instance : IntentValueConvertible](appintenttypedefinition/instance.md)
  The instance type that corresponds to this definition type.
### Instance Methods
- [func isInstance(Self.Instance) throws](appintenttypedefinition/isinstance(_:).md)
  Validates that the provided value matches this definition’s type.

## Relationships

### Conforming Types
- [AppEntityDefinition](appentitydefinition.md)
- [AppEnumDefinition](appenumdefinition.md)
- [TransientAppEntityDefinition](transientappentitydefinition.md)

## See Also

- [struct DynamicPropertyPath](dynamicpropertypath.md)
  A type-safe, dynamic path to access nested intent values.
- [struct DynamicPropertyPathCollection](dynamicpropertypathcollection.md)
  Indexed result items from an intent value query.
- [struct IntentValuePropertiesCallable](intentvaluepropertiescallable.md)
  A callable wrapper that creates app intent instances from keyword arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/appintenttypedefinition)*