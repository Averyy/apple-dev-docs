# PHCollectionEditOperation.removeContent

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The collection supports removing the items it contains.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case removeContent
```

```c
PHCollectionEditOperationRemoveContent
```

## Discussion

Removing an item removes it from the collection, but does not permanently delete it from the photo library.

## See Also

### Constants
- [PHCollectionEditOperation.deleteContent](./deletecontent.md)
  The collection supports deleting the items it contains.
- [PHCollectionEditOperation.addContent](./addcontent.md)
  The collection supports adding items that already exist elsewhere in the photo library.
- [PHCollectionEditOperation.createContent](./createcontent.md)
  The collection supports creating new items.
- [PHCollectionEditOperation.rearrangeContent](./rearrangecontent.md)
  The collection supports reordering the arrangement of items it contains.
- [PHCollectionEditOperation.delete](./delete.md)
  The collection itself can be deleted.
- [PHCollectionEditOperation.rename](./rename.md)
  The collection itself can be renamed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectioneditoperation/removecontent)*