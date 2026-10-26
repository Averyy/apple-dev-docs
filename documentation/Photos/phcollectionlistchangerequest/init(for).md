# init(for:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a request for modifying the specified collection list.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(for collectionList: PHCollectionList)
```

```objc
+ (instancetype) changeRequestForCollectionList:(PHCollectionList *) collectionList;
```

#### Return Value

A collection list change request.

#### Discussion

After you create a change request within a photo library change block, propose changes to the collection’s title or list of child collections with the properties and instance methods of the change request. After Photos runs your change block, the collection list reflects your changes. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

Use this method when modifying a collection list’s metadata or when adding or removing child collections without regard to their arrangement. To work with indexes in the list of child collections, use the [`init(for:childCollections:)`](./init%28for,childcollections%29.md) method instead.

## Parameters

- `collectionList`: The collection list to be modified.

## See Also

### Creating a Change Request
- [convenience init?(for: PHCollectionList, childCollections: PHFetchResult<PHCollection>)](./init%28for,childcollections%29.md)
  Creates a request for modifying the specified collection list, with a fetch result for tracking changes.
- [convenience init?(forTopLevelCollectionListUserCollections: PHFetchResult<PHCollection>)](./init%28fortoplevelcollectionlistusercollections%29.md)
  Creates a request to add, remove, or rearrange child collections in the top-level collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/init(for:))*