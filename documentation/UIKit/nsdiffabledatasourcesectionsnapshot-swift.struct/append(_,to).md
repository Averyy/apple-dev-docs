# append(_:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified items as child items of the specified parent item in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
mutating func append(_ items: [ItemIdentifierType], to parent: ItemIdentifierType? = nil)
```

## Parameters

- `items`: The identifiers of the items to append to the parent item in the section snapshot.
- `parent`: The parent item to append the items to. If you don’t specify a parent, the section snapshot appends the items to its root level.

## See Also

### Creating a section snapshot
- [init()](./init%28%29.md)
  Creates an empty section snapshot.
- [init(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)](./init%28_%29.md)
  Creates a copy of the provided section snapshot.
- [func snapshot(of: ItemIdentifierType, includingParent: Bool) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](./snapshot%28of,includingparent%29.md)
  Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/append(_:to:))*