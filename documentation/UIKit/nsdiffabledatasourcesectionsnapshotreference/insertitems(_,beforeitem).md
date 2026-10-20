# insertItems(_:beforeItem:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Inserts the provided items immediately before the item with the specified identifier in the section snapshot.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func insertItems(_ items: [Any], beforeItem beforeIdentifier: Any)
```

```objc
- (void) insertItems:(NSArray<id> *) items beforeItem:(ItemIdentifierType) beforeIdentifier;
```

## See Also

### Inserting items
- [func insert(NSDiffableDataSourceSectionSnapshotReference, afterItem: Any) -> Any](./insert%28_,afteritem%29.md)
  Inserts the provided section snapshot immediately after the item with the specified identifier in the section snapshot.
- [func insertItems([Any], afterItem: Any)](./insertitems%28_,afteritem%29.md)
  Inserts the provided items immediately after the item with the specified identifier in the section snapshot.
- [func insert(NSDiffableDataSourceSectionSnapshotReference, beforeItem: Any)](./insert%28_,beforeitem%29.md)
  Inserts the provided section snapshot immediately before the item with the specified identifier in the section snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshotreference/insertitems(_:beforeitem:))*