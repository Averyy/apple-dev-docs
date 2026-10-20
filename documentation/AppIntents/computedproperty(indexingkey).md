# ComputedProperty(indexingKey:)

**Framework**: App Intents  
**Kind**: macro

A macro that adds a computed app entity property with get and set accessors.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@attached
(peer, names: prefixed(`$`), prefixed(`_`)) @attached(accessor, names: named(get), named(set)) macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)
```

#### Overview

A deferred property has a few trade-offs:

- The system doesn’t index it when you donate an [`IndexedEntity`](indexedentity.md) to a Spotlight index.
- The system doesn’t send it to Shortcuts or Siri automatically; it fetches the value only when needed.

#### Example

```swift
struct Restaurant: AppEntity {
    var model: Menu

    @ComputedProperty(indexingKey: \.displayName)
    var menuItems: [MenuItem] {
        model.menuItems
    }
}
```

## Parameters

- `indexingKey`: A Spotlight attribute set key mapping for this property.

## See Also

- [macro ComputedProperty()](computedproperty().md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource)](computedproperty(title:).md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/computedproperty(indexingkey:))*