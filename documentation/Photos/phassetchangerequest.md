# PHAssetChangeRequest

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetChangeRequest
```

```objc
@interface PHAssetChangeRequest : PHChangeRequest
```

## Mentions

- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)
- [Editing Asset Content](../PhotoKit/editing-asset-content.md)

#### Overview

You use the [`PHAssetChangeRequest`](./phassetchangerequest.md) class to request changes for [`PHAsset`](./phasset.md) objects. To make changes to assets in the Photos library, create a change request by using the appropriate class method for the change you want to perform.

- Call one of the methods listed in Adding New Assets to create a new asset from an image or video file.
- Call the [`deleteAssets(_:)`](./phassetchangerequest/deleteassets%28_%29.md) method to delete existing assets.
- Call the [`init(for:)`](./phassetchangerequest/init%28for%29.md) method to modify an asset’s content or metadata.

A change request for creating or modifying an asset works like a mutable version of the asset object. Use the change request’s properties to request changes to the corresponding properties of the asset itself. For example, the following code uses the [`isFavorite`](./phassetchangerequest/isfavorite.md) property of a change request to mark an asset as a favorite:

**Swift**:

```swift
func toggleFavorite(for asset: PHAsset) {        
    PHPhotoLibrary.shared().performChanges {
        // Create a change request from the asset to be modified.
        let request = PHAssetChangeRequest(for: asset)
        // Set a property of the request to change the asset itself.
        request.isFavorite = !asset.isFavorite
    } completionHandler: { success, error in
        print("Finished updating asset. " + (success ? "Success." : error!.localizedDescription))
    }  
}
```

**Objective-C**:

```objc
- (void)toggleFavoriteForAsset:(PHAsset *)asset {
    [[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
        // Create a change request from the asset to be modified.
        PHAssetChangeRequest *request = [PHAssetChangeRequest changeRequestForAsset:asset];
        // Set a property of the request to change the asset itself.
        request.favorite = !asset.favorite;
    } completionHandler:^(BOOL success, NSError *error) {
        NSLog(@"Finished updating asset. %@", (success ? @"Success." : error));
    }];
}
```

After Photos runs the change block and calls your completion handler, the asset’s state reflects the changes that you requested in the block.

If you create or use a change request object outside a photo library change block, Photos raises an Objective-C exception. For details on change blocks, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Adding New Assets
- [class func creationRequestForAsset(from: UIImage) -> Self](./phassetchangerequest/creationrequestforasset%28from%29.md)
  Creates a request for adding a new image asset to the Photos library.
- [class func creationRequestForAssetFromImage(atFileURL: URL) -> Self?](./phassetchangerequest/creationrequestforassetfromimage%28atfileurl%29.md)
  Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [class func creationRequestForAssetFromVideo(atFileURL: URL) -> Self?](./phassetchangerequest/creationrequestforassetfromvideo%28atfileurl%29.md)
  Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.
- [var placeholderForCreatedAsset: PHObjectPlaceholder?](./phassetchangerequest/placeholderforcreatedasset.md)
  A placeholder object for the asset that the change request creates.
### Deleting Assets
- [class func deleteAssets(any NSFastEnumeration)](./phassetchangerequest/deleteassets%28_%29.md)
  Requests that the specified assets be deleted.
### Modifying Assets
- [convenience init(for: PHAsset)](./phassetchangerequest/init%28for%29.md)
  Creates a request for modifying the specified asset.
- [var creationDate: Date?](./phassetchangerequest/creationdate.md)
  The date and time at which the asset claims to have been originally created.
- [var location: CLLocation?](./phassetchangerequest/location.md)
  The location information saved with the asset.
- [var isFavorite: Bool](./phassetchangerequest/isfavorite.md)
  A Boolean value that indicates whether the asset is marked as one of the user’s favorites.
- [var isHidden: Bool](./phassetchangerequest/ishidden.md)
  A Boolean value that indicates whether the asset is hidden in collections.
- [var caption: String?](./phassetchangerequest/caption.md)
  An asset description to change to. Set to nil or an empty string to clear the caption.
- [func addKeyword(String)](./phassetchangerequest/addkeyword%28_%29.md)
  Add or remove a keyword associated with this asset Adding a keyword that is already associated (or removing a keyword that is not) will be silently ignored
- [func removeKeyword(String)](./phassetchangerequest/removekeyword%28_%29.md)
- [var rating: PHAsset.Rating](./phassetchangerequest/rating.md)
  The rating for this asset
- [func setLivePhotoVideoPlaybackEnabled(Bool)](./phassetchangerequest/setlivephotovideoplaybackenabled%28_%29.md)
  Disable or enable the video part of a Live Photo so it just appears as a still image (disabled) or a Live Photo (enabled)
### Editing Asset Content
- [var contentEditingOutput: PHContentEditingOutput?](./phassetchangerequest/contenteditingoutput.md)
  The output of an asset content editing session.
- [func revertAssetContentToOriginal()](./phassetchangerequest/revertassetcontenttooriginal%28%29.md)
  Request to revert any edits made to the asset’s content.
- [func revertAssetContent(to: PHAsset.OriginalResourceChoice)](./phassetchangerequest/revertassetcontent%28to%29.md)
  Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders.
### Initializers
- [convenience init(forAsset: PHAsset)](./phassetchangerequest/init%28forasset%29.md)

## Relationships

### Inherits From
- [PHChangeRequest](./phchangerequest.md)
### Inherited By
- [PHAssetCreationRequest](./phassetcreationrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Updating the Library
- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)
  Create, delete, or modify assets and collections in a photo library by making change requests.
- [func performChanges(() -> Void, completionHandler: ((Bool, (any Error)?) -> Void)?)](./phphotolibrary/performchanges%28_,completionhandler%29.md)
  Asynchronously runs a block that requests changes to the photo library.
- [func performChangesAndWait(() -> Void) throws](./phphotolibrary/performchangesandwait%28_%29.md)
  Synchronously runs a block that requests changes to be performed in the photo library.
- [class PHChangeRequest](./phchangerequest.md)
  The abstract base class of the framework’s photo library change requests.
- [class PHAssetCollectionChangeRequest](./phassetcollectionchangerequest.md)
  A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [class PHCollectionListChangeRequest](./phcollectionlistchangerequest.md)
  A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [class PHObjectPlaceholder](./phobjectplaceholder.md)
  A read-only proxy object that represents a Photos asset or collection to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest)*