# init(appEntity:priority:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

Initializes a new searchable item with the relevant fields populated from the provided app entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
convenience init<Entity>(appEntity: Entity, priority: Int) where Entity : IndexedEntity
```

## Parameters

- `appEntity`: The app entity to use for initialization.
- `priority`: The importance of this item compared to the other donated items.

## See Also

### Getting a searchable item
- [init(uniqueIdentifier: String?, domainIdentifier: String?, attributeSet: CSSearchableItemAttributeSet)](./init%28uniqueidentifier,domainidentifier,attributeset%29.md)
  Returns a searchable item associated with the specified identifier, domain identifier, and attribute set.
- [convenience init(appEntity: some IndexedEntity) async](./init%28appentity%29-3hv5.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.
- [convenience init(appEntity: some IndexedEntity)](./init%28appentity%29-89ehq.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int) async](./init%28appentity,priority%29-7xlow.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/init(appentity:priority:)-7h9s)*