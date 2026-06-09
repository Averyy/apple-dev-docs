# ComputedProperty()

**Framework**: App Intents  
**Kind**: macro

A macro that adds a computed app entity property with a get accessor and an optional set accessor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
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
- [Property comparators](property-comparators.md)
  Specify the type of comparison to perform during a property-matched query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/computedproperty())*