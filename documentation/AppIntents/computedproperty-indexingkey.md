# ComputedProperty(indexingKey:)

**Framework**: App Intents  
**Kind**: macro

A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor

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
(peer, names: prefixed(`$`), prefixed(`_`)) @attached(accessor, names: named(get), named(set)) macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)
```

#### Overview

Deferred properties have a few trade offs to consider:

- They are not included when indexing and IndexedEntity
- They are not sent to Shortcuts and Siri automatically and will only be fetched when needed

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
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource)](computedproperty(title:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(customIndexingKey: CSCustomAttributeKey)](computedproperty(customindexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](computedproperty(title:customindexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(title:indexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro DeferredProperty()](deferredproperty().md)
  A macro that creates an async property for an AppEntity that allows for providing an async get accessor
- [macro DeferredProperty(title: LocalizedStringResource)](deferredproperty(title:).md)
  A macro that creates an async property for an AppEntity that allows for providing an async get accessor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/computedproperty(indexingkey:))*