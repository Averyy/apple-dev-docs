# DeferredProperty()

**Framework**: App Intents  
**Kind**: macro

A macro that creates an async property for an AppEntity that allows for providing an async get accessor

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
(peer, names: prefixed(`$`), prefixed(`_`)) @attached(accessor, names: named(get), named(set)) macro DeferredProperty()
```

#### Example

```swift
struct Restaurant: AppEntity {
    var model: Menu

    @DeferredProperty
    var popularItems: [MenuItem] {
        get async {
            await model.server.popularMenuItems()
        }
    }
}
```

> **Note**: Deferred properties are not included when indexing an `IndexedEntity`

## See Also

- [macro ComputedProperty()](computedproperty().md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource)](computedproperty(title:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(indexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(customIndexingKey: CSCustomAttributeKey)](computedproperty(customindexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource, customIndexingKey: CSCustomAttributeKey)](computedproperty(title:customindexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(title: LocalizedStringResource, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(title:indexingkey:).md)
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro DeferredProperty(title: LocalizedStringResource)](deferredproperty(title:).md)
  A macro that creates an async property for an AppEntity that allows for providing an async get accessor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deferredproperty())*