# init(for:childCollections:)

**Framework**: Photos  
**Kind**: init  
**Role**: Initializer

Creates a request for modifying the specified collection list, with a fetch result for tracking changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(for collectionList: PHCollectionList, childCollections: PHFetchResult<PHCollection>)
```

```objc
+ (instancetype) changeRequestForCollectionList:(PHCollectionList *) collectionList childCollections:(PHFetchResult<__kindof PHCollection *> *) childCollections;
```

## Return Value

A collection list change request.

## Discussion

After you create a change request within a photo library change block, propose changes to the collection’s title or list of child collections with the properties and instance methods of the change request. After Photos runs your change block, the collection list reflects your changes. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

Use this method when you need to insert, remove, or rearrange collections at specified indexes in the collection list. By passing in a fetch result reflecting what your app sees as the current state of the collection’s membership, the Photos framework can ensure that the indexes you specify are valid even if the collection has changed since you last fetched it. If you don’t need to work with indexes in the list of child collections, you can use the [`init(for:)`](./init%28for%29.md) method instead.

## Parameters

- `collectionList`: The collection list to be modified.
- `childCollections`: A fetch result listing the child collections in the collection.

## See Also

### Creating a Change Request
- [convenience init?(for: PHCollectionList)](./init%28for%29.md)
  Creates a request for modifying the specified collection list.
- [convenience init?(forTopLevelCollectionListUserCollections: PHFetchResult<PHCollection>)](./init%28fortoplevelcollectionlistusercollections%29.md)
  Creates a request to add, remove, or rearrange child collections in the top-level collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/init(for:childcollections:))*