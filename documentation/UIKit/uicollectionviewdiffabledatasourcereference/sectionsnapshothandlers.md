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
var sectionSnapshotHandlers: __UICollectionViewDiffableDataSourceSectionSnapshotHandlers { get set }
```

#### Discussion

Provide section snapshot handlers to support the expanding or collapsing of items in your collection view.

Use the [`snapshotForExpandingParentItemHandler`](uicollectionviewdiffabledatasourcesectionsnapshothandlers/snapshotforexpandingparentitemhandler.md) handler to customize the snapshot that returns when a particular parent item is expanded.

**Swift**:

```swift
// Allow every item to be collapsed
dataSource.sectionSnapshotHandlers.shouldCollapseItem = { item in return true }

dataSource.sectionSnapshotHandlers.snapshotForExpandingParent = {
    parent, currentChildSnapshot -> NSDiffableDataSourceSectionSnapshot<String> in
    
    // Return child snapshot for the parent, or just currentChildSnapshot
}
```

**Objective-C**:

```objc
// Allow every item to be collapsed.
[dataSource.sectionSnapshotHandlers setShouldCollapseItemHandler:^BOOL(NSString *item) {
    return YES;
}];

[dataSource.sectionSnapshotHandlers setSnapshotForExpandingParentItemHandler:^NSDiffableDataSourceSectionSnapshot<NSString *> * (NSString *parent, NSDiffableDataSourceSectionSnapshot<NSString *> *currentChildSnapshot) {
    // Return child snapshot for the parent, or just currentChildSnapshot.
}];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereference/sectionsnapshothandlers)*