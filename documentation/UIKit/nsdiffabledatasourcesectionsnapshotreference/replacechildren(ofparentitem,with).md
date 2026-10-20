# replaceChildren(ofParentItem:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Replaces all child items of the specified parent item with the provided section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func replaceChildren(ofParentItem parentItem: Any, with snapshot: NSDiffableDataSourceSectionSnapshotReference)
```

```objc
- (void) replaceChildrenOfParentItem:(ItemIdentifierType) parentItem withSnapshot:(NSDiffableDataSourceSectionSnapshot<id> *) snapshot;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/replacechildren(ofparentitem:with:))*