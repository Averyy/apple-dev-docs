# sectionSnapshotHandlers

**Framework**: UIKit  
**Kind**: property

The diffable data source’s handlers for expanding and collapsing items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var sectionSnapshotHandlers: __UICollectionViewDiffableDataSourceSectionSnapshotHandlers { get set }
```

#### Discussion

Provide section snapshot handlers to support the expanding or collapsing of items in your collection view.

Use the [`snapshotForExpandingParentItemHandler`](uicollectionviewdiffabledatasourcesectionsnapshothandlers/snapshotforexpandingparentitemhandler.md) handler to customize the snapshot that returns when a particular parent item is expanded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers)*