# deleteCollectionLists(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Requests to delete the specified asset collections.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func deleteCollectionLists(_ collectionLists: any NSFastEnumeration)
```

```objc
+ (void) deleteCollectionLists:(id<NSFastEnumeration>) collectionLists;
```

## Mentions

- [Requesting Changes to the Photo Library](../../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Discussion

Call this method within a photo library change block to delete collection lists. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

> ❗ **Important**:  Deleting a collection list also deletes any child collections it contains. To preserve those collections, remove them from the collection list (with the [`removeChildCollections(_:)`](./removechildcollections%28_%29.md) or [`removeChildCollections(at:)`](./removechildcollections%28at%29.md) method) before deleting it. Deleting a collection list does not delete assets contained in its child collections.

## Parameters

- `collectionLists`: An array of [`PHCollectionList`](../phcollectionlist.md) objects to be deleted.

## See Also

### Managing Collection Lists
- [class func creationRequestForCollectionList(withTitle: String) -> Self](./creationrequestforcollectionlist%28withtitle%29.md)
  Creates a request for adding a new collection list to the Photos library.
- [var placeholderForCreatedCollectionList: PHObjectPlaceholder](./placeholderforcreatedcollectionlist.md)
  A placeholder object for the collection list that the change request creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/deletecollectionlists(_:))*