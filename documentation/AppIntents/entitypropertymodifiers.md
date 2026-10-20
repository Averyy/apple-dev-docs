# EntityPropertyModifiers

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct EntityPropertyModifiers
```

## Topics

### Type Properties
- [static let async: EntityPropertyModifiers](./entitypropertymodifiers/async.md)
- [static let readOnly: EntityPropertyModifiers](./entitypropertymodifiers/readonly.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Property declarations
- [macro ComputedProperty()](./computedproperty%28%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource)](./computedproperty%28title%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./computedproperty%28indexingkey%29.md)
  A macro that adds a computed app entity property with get and set accessors.
- [macro ComputedProperty(customIndexingKey: CSCustomAttributeKey)](./computedproperty%28customindexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](./computedproperty%28title,customindexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./computedproperty%28title,indexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro DeferredProperty()](./deferredproperty%28%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource)](./deferredproperty%28title%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./deferredproperty%28indexingkey%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./deferredproperty%28title,indexingkey%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [class EntityProperty](./entityproperty.md)
  A property wrapper that exposes the associated property to the system.
- [Property comparators](./property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitypropertymodifiers)*