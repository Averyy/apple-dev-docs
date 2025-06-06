# append(_:to:)

**Framework**: UIKit  
**Kind**: method

Adds the specified items as child items of the specified parent item in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
mutating func append(_ items: [ItemIdentifierType], to parent: ItemIdentifierType? = nil)
```

## Parameters

- `items`: The identifiers of the items to append to the parent item in the section snapshot.
- `parent`: The parent item to append the items to. If you don’t specify a parent, the section snapshot appends the items to its root level.

## See Also

- [init()](nsdiffabledatasourcesectionsnapshot-swift.struct/init.md)
  Creates an empty section snapshot.
- [init(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)](nsdiffabledatasourcesectionsnapshot-swift.struct/init(_:).md)
  Creates a copy of the provided section snapshot.
- [func snapshot(of: ItemIdentifierType, includingParent: Bool) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectionsnapshot-swift.struct/snapshot(of:includingparent:).md)
  Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/append(_:to:))*