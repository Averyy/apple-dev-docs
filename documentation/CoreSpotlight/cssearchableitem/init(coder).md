# init(coder:)

**Framework**: Core Spotlight  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init?(coder: NSCoder)
```

## See Also

### Getting a searchable item
- [init(uniqueIdentifier: String?, domainIdentifier: String?, attributeSet: CSSearchableItemAttributeSet)](./init%28uniqueidentifier,domainidentifier,attributeset%29.md)
  Returns a searchable item associated with the specified identifier, domain identifier, and attribute set.
- [convenience init(appEntity: some IndexedEntity) async](./init%28appentity%29-3hv5.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.
- [convenience init(appEntity: some IndexedEntity)](./init%28appentity%29-89ehq.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int)](./init%28appentity,priority%29-7h9s.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int) async](./init%28appentity,priority%29-7xlow.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/init(coder:))*