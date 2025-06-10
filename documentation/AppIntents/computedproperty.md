# ComputedProperty()

**Framework**: App Intents  
**Kind**: macro

A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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
  A macro that creates a computed property for an AppEntity that allows for providing a get and/or set accessor
- [macro ComputedProperty(indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](computedproperty(indexingkey:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/computedproperty())*