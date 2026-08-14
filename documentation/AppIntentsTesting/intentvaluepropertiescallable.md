# IntentValuePropertiesCallable

**Framework**: App Intents Testing  
**Kind**: struct

A callable wrapper that creates app intent instances from keyword arguments.

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
@dynamicCallable
struct IntentValuePropertiesCallable<T>
```

#### Overview

The `IntentValuePropertiesCallable` wrapper uses the `@dynamicCallable` attribute to provide a natural function-call syntax for setting properties on type-erased app intents instances. Don’t create instances of this type directly. Instead, use [`makeIntent`](appintentdefinition/makeintent.md) or [`makeEntity`](transientappentitydefinition/makeentity.md).

## Topics

### Instance Methods
- [func dynamicallyCall(withKeywordArguments: KeyValuePairs<String, (any IntentValueExpressing)?>) -> T](intentvaluepropertiescallable/dynamicallycall(withkeywordarguments:).md)
  Returns an instance of `T` by applying the provided argument values to the properties.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol AppIntentTypeDefinition](appintenttypedefinition.md)
  A protocol that associates a definition type with its corresponding instance type.
- [struct DynamicPropertyPath](dynamicpropertypath.md)
  A type-safe, dynamic path to access nested intent values.
- [struct DynamicPropertyPathCollection](dynamicpropertypathcollection.md)
  Indexed result items from an intent value query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/intentvaluepropertiescallable)*