# placeholderForCreatedAssetCollection

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A placeholder object for the asset collection that the change request creates.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var placeholderForCreatedAssetCollection: PHObjectPlaceholder { get }
```

```objc
@property (nonatomic, strong, readonly) PHObjectPlaceholder * placeholderForCreatedAssetCollection;
```

#### Discussion

Use this property if you need to reference the asset collection created by a change request within the same change block. For example, the following code, when included in a photo library change block, creates an asset collection and then adds it to a collection list.

**Swift**:

```swift
let createAlbumRequest = PHAssetCollectionChangeRequest.creationRequestForAssetCollection(withTitle: "New Album")
let albumPlaceholder = createAlbumRequest.placeholderForCreatedAssetCollection
let folderChangeRequest = PHCollectionListChangeRequest(for: folder)
folderChangeRequest!.addChildCollections([albumPlaceholder] as NSFastEnumeration)
```

**Objective-C**:

```objc
PHAssetCollectionChangeRequest *createAlbumRequest =
    [PHAssetCollectionChangeRequest creationRequestForAssetCollectionWithTitle:@"New Album"];
PHObjectPlaceholder *albumPlaceholder = createAlbumRequest.placeholderForCreatedAssetCollection;
PHCollectionListChangeRequest *folderChangeRequest =
    [PHCollectionListChangeRequest changeRequestForCollectionList:folder];
[folderChangeRequest addChildCollections:@[ albumPlaceholder ]];
```

For details on change blocks, see [`PHPhotoLibrary`](../phphotolibrary.md).

## See Also

### Adding New Asset Collections
- [class func creationRequestForAssetCollection(withTitle: String) -> Self](./creationrequestforassetcollection%28withtitle%29.md)
  Creates a request for adding a new asset collection to the Photos library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/placeholderforcreatedassetcollection)*