# ComputedProperty()

**Framework**: App Intents  
**Kind**: macro  
**Role**: Macro

A macro that adds a computed app entity property with a get accessor and an optional set accessor.

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
@attached
(peer, names: prefixed(`$`), prefixed(`_`)) @attached(accessor, names: named(get), named(set)) macro ComputedProperty()
```

#### Example

```swift
struct Restaurant: AppEntity {
    var model: Menu

    @ComputedProperty
    var menuItems: [MenuItem] {
        model.menuItems
    }
}
```

## See Also

### Property declarations
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
- [struct EntityPropertyModifiers](./entitypropertymodifiers.md)
- [Property comparators](./property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/computedproperty())*