# init(appEntity:)

**Framework**: Core Spotlight  
**Kind**: init

Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(appEntity: some IndexedEntity) async
```

## Parameters

- `appEntity`: The app entity to use for initialization.

## See Also

- [init(uniqueIdentifier: String?, domainIdentifier: String?, attributeSet: CSSearchableItemAttributeSet)](cssearchableitem/init(uniqueidentifier:domainidentifier:attributeset:).md)
  Returns a searchable item associated with the specified identifier, domain identifier, and attribute set.
- [convenience init(appEntity: some IndexedEntity)](cssearchableitem/init(appentity:)-89ehq.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int)](cssearchableitem/init(appentity:priority:)-7h9s.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity.
- [convenience init<Entity>(appEntity: Entity, priority: Int) async](cssearchableitem/init(appentity:priority:)-7xlow.md)
  Initializes a new searchable item with the relevant fields populated from the provided app entity. Resolves deferred properties before indexing.
- [init?(coder: NSCoder)](cssearchableitem/init(coder:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/init(appentity:)-3hv5)*