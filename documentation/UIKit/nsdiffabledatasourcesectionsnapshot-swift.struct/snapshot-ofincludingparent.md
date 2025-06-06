# snapshot(of:includingParent:)

**Framework**: UIKit  
**Kind**: method

Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
func snapshot(of parent: ItemIdentifierType, includingParent: Bool = false) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>
```

## See Also

- [init()](nsdiffabledatasourcesectionsnapshot-swift.struct/init.md)
  Creates an empty section snapshot.
- [init(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)](nsdiffabledatasourcesectionsnapshot-swift.struct/init(_:).md)
  Creates a copy of the provided section snapshot.
- [func append([ItemIdentifierType], to: ItemIdentifierType?)](nsdiffabledatasourcesectionsnapshot-swift.struct/append(_:to:).md)
  Adds the specified items as child items of the specified parent item in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/snapshot(of:includingparent:))*