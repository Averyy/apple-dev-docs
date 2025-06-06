# init(_:)

**Framework**: UIKit  
**Kind**: init

Creates a copy of the provided section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
init(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)
```

## See Also

- [init()](nsdiffabledatasourcesectionsnapshot-swift.struct/init.md)
  Creates an empty section snapshot.
- [func snapshot(of: ItemIdentifierType, includingParent: Bool) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectionsnapshot-swift.struct/snapshot(of:includingparent:).md)
  Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.
- [func append([ItemIdentifierType], to: ItemIdentifierType?)](nsdiffabledatasourcesectionsnapshot-swift.struct/append(_:to:).md)
  Adds the specified items as child items of the specified parent item in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/init(_:))*