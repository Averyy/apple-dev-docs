# init(_:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a copy of the provided section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
init(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)
```

## See Also

### Creating a section snapshot
- [init()](./init%28%29.md)
  Creates an empty section snapshot.
- [func snapshot(of: ItemIdentifierType, includingParent: Bool) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](./snapshot%28of,includingparent%29.md)
  Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.
- [func append([ItemIdentifierType], to: ItemIdentifierType?)](./append%28_,to%29.md)
  Adds the specified items as child items of the specified parent item in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/init(_:))*