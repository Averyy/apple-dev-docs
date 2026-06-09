# init(uniqueIdentifier:domainIdentifier:attributeSet:)

**Framework**: Core Spotlight  
**Kind**: init

Returns a searchable item associated with the specified identifier, domain identifier, and attribute set.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
init(uniqueIdentifier: String?, domainIdentifier: String?, attributeSet: CSSearchableItemAttributeSet)
```

#### Return Value

A searchable item that’s associated with the specified identifier, domain identifier, and attribute set.

## Parameters

- `uniqueIdentifier`: The unique identifier for the item. If you specify `NULL`, an identifier is generated automatically.
- `domainIdentifier`: An identifier for a domain, such as an album, that helps you group items together in a way that makes sense.
- `attributeSet`: A set of properties that specify the metadata you want to display about an item in a search result. See [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) for the types of properties you can use.

## See Also

- [convenience init(appEntity: some IndexedEntity) async](cssearchableitem/init(appentity:)-3hv5.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.
- [convenience init(appEntity: some IndexedEntity)](cssearchableitem/init(appentity:)-89ehq.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int)](cssearchableitem/init(appentity:priority:)-7h9s.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int) async](cssearchableitem/init(appentity:priority:)-7xlow.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.
- [init?(coder: NSCoder)](cssearchableitem/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/init(uniqueidentifier:domainidentifier:attributeset:))*