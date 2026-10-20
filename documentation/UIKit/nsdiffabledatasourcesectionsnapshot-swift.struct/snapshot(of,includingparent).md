# snapshot(of:includingParent:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a section snapshot that contains the child items of the specified parent item, optionally including the parent item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
func snapshot(of parent: ItemIdentifierType, includingParent: Bool = false) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>
```

## See Also

### Creating a section snapshot
- [init()](./init%28%29.md)
  Creates an empty section snapshot.
- [init(NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)](./init%28_%29.md)
  Creates a copy of the provided section snapshot.
- [func append([ItemIdentifierType], to: ItemIdentifierType?)](./append%28_,to%29.md)
  Adds the specified items as child items of the specified parent item in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/snapshot(of:includingparent:))*