# creationRequestForAssetCollection(withTitle:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a request for adding a new asset collection to the Photos library.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func creationRequestForAssetCollection(withTitle title: String) -> Self
```

```objc
+ (instancetype) creationRequestForAssetCollectionWithTitle:(NSString *) title;
```

## Mentions

- [Requesting Changes to the Photo Library](../../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Return Value

An asset collection creation request.

#### Discussion

Call this method within a photo library change block to create a new asset collection. For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

To add assets to the newly created asset collection or change its title, use the methods listed in Modifying Asset Collections. To reference the newly created asset collection later in the same change block or after the change block completes, use the [`placeholderForCreatedAssetCollection`](./placeholderforcreatedassetcollection.md) property to retrieve a placeholder object.

## Parameters

- `title`: A name for the new asset collection.

## See Also

### Adding New Asset Collections
- [var placeholderForCreatedAssetCollection: PHObjectPlaceholder](./placeholderforcreatedassetcollection.md)
  A placeholder object for the asset collection that the change request creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/creationrequestforassetcollection(withtitle:))*