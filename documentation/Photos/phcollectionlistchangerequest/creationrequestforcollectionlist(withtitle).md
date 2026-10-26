# creationRequestForCollectionList(withTitle:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a request for adding a new collection list to the Photos library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func creationRequestForCollectionList(withTitle title: String) -> Self
```

```objc
+ (instancetype) creationRequestForCollectionListWithTitle:(NSString *) title;
```

#### Return Value

A collection list creation request.

#### Discussion

Call this method within a photo library change block to create a new collection list. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

To add collections to the newly created collection list or to change its title, use the methods listed in Managing Collections. To reference the newly created collection list later in the same change block or after the change block completes, use the [`placeholderForCreatedCollectionList`](./placeholderforcreatedcollectionlist.md) property to retrieve a placeholder object.

## Parameters

- `title`: A name for the new collection list.

## See Also

### Managing Collection Lists
- [var placeholderForCreatedCollectionList: PHObjectPlaceholder](./placeholderforcreatedcollectionlist.md)
  A placeholder object for the collection list that the change request creates.
- [class func deleteCollectionLists(any NSFastEnumeration)](./deletecollectionlists%28_%29.md)
  Requests to delete the specified asset collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/creationrequestforcollectionlist(withtitle:))*