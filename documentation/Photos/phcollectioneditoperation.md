# PHCollectionEditOperation

**Framework**: Photos  
**Kind**: enum  
**Role**: Enumeration

Values identifying possible actions that a collection can support, used by the [`canPerform(_:)`](./phcollection/canperform%28_%29.md) method.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum PHCollectionEditOperation
```

```c
enum PHCollectionEditOperation : NSInteger;
```

## Topics

### Constants
- [PHCollectionEditOperation.deleteContent](./phcollectioneditoperation/deletecontent.md)
  The collection supports deleting the items it contains.
- [PHCollectionEditOperation.removeContent](./phcollectioneditoperation/removecontent.md)
  The collection supports removing the items it contains.
- [PHCollectionEditOperation.addContent](./phcollectioneditoperation/addcontent.md)
  The collection supports adding items that already exist elsewhere in the photo library.
- [PHCollectionEditOperation.createContent](./phcollectioneditoperation/createcontent.md)
  The collection supports creating new items.
- [PHCollectionEditOperation.rearrangeContent](./phcollectioneditoperation/rearrangecontent.md)
  The collection supports reordering the arrangement of items it contains.
- [PHCollectionEditOperation.delete](./phcollectioneditoperation/delete.md)
  The collection itself can be deleted.
- [PHCollectionEditOperation.rename](./phcollectioneditoperation/rename.md)
  The collection itself can be renamed.
### Initializers
- [init?(rawValue: Int)](./phcollectioneditoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining Collection Capabilities
- [var canContainAssets: Bool](./phcollection/cancontainassets.md)
  A Boolean value indicating whether the collection can contain assets.
- [var canContainCollections: Bool](./phcollection/cancontaincollections.md)
  A Boolean value indicating whether the collection can contain other collections.
- [func canPerform(PHCollectionEditOperation) -> Bool](./phcollection/canperform%28_%29.md)
  Returns whether the collection supports the specified editing operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectioneditoperation)*