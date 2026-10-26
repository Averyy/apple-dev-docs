# Requesting Changes to the Photo Library

**Framework**: PhotoKit  
**Role**: Article

Create, delete, or modify assets and collections in a photo library by making change requests.

#### Overview

Because [`PHAsset`](https://developer.apple.com/documentation/photos/phasset), [`PHAssetCollection`](https://developer.apple.com/documentation/photos/phassetcollection), and [`PHCollectionList`](https://developer.apple.com/documentation/photos/phcollectionlist) instances are immutable objects, you can’t make changes to them. To modify the Photos assets or collections these objects represent, use the shared photo library to execute a change block. Inside the change block, create change request objects. Then apply a change block with one of the methods listed in Updating the Library. The changes you request take effect after Photos runs the change block and calls your completion handler.

Each of the change request classes—[`PHAssetChangeRequest`](https://developer.apple.com/documentation/photos/phassetchangerequest), [`PHAssetCollectionChangeRequest`](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest), and [`PHCollectionListChangeRequest`](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest)—corresponds to an asset or collection class. Use these classes to make the following types of changes:

Creating items. Each change request class provides methods for requesting to create a new item of the corresponding asset or collection class. For example, use the [`creationRequestForAssetCollection(withTitle:)`](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/creationrequestforassetcollection(withtitle:)) method to create an asset collection.

To reference a newly created request within the change block—for example, to add a new asset to a collection—use the [`PHObjectPlaceholder`](https://developer.apple.com/documentation/photos/phobjectplaceholder) object provided by the change request. After the change block completes, use the placeholder object’s [`localIdentifier`](https://developer.apple.com/documentation/photos/phobject/localidentifier) property to fetch the created object.

Deleting items. Each change request class provides methods for requesting to delete one or more items of the corresponding asset or collection class. For example, use the [`deleteCollectionLists(_:)`](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/deletecollectionlists(_:)) method to delete collection lists.

Modifying items. You modify an existing asset or collection by creating a change request from a [`PHAsset`](https://developer.apple.com/documentation/photos/phasset), [`PHAssetCollection`](https://developer.apple.com/documentation/photos/phassetcollection), or [`PHCollectionList`](https://developer.apple.com/documentation/photos/phcollectionlist) object representing it. For example, the [`init(for:)`](https://developer.apple.com/documentation/photos/phassetchangerequest/init(for:)) method creates a change request you can use for modifying an asset.

After creating a change request, use its properties and instance methods to modify the corresponding features of the asset or collection it represents. For example, to set an asset’s [`isFavorite`](https://developer.apple.com/documentation/photos/phasset/isfavorite) property, set the [`isFavorite`](https://developer.apple.com/documentation/photos/phassetchangerequest/isfavorite) property of a change request created from that asset. To add to an asset collection, call the [`addAssets(_:)`](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/addassets(_:)) method on an asset collection change request.

##### Create an Asset for an Album

Use a change block to combine several changes to the photo library into a single atomic update. The following code uses a change block to create an asset from an image and add that asset to an album.

**Swift**:

```swift
func addAsset(image: UIImage, to album: PHAssetCollection) {
    PHPhotoLibrary.shared().performChanges {
        // Request creating an asset from the image.
        let creationRequest = PHAssetChangeRequest.creationRequestForAsset(from: image)
        // Request editing the album.
        guard let addAssetRequest = PHAssetCollectionChangeRequest(for: album) else { return }
        // Get a placeholder for the new asset and add it to the album editing request.
        addAssetRequest.addAssets([creationRequest.placeholderForCreatedAsset!] as NSArray)
    } completionHandler: { success, error in
        if !success, let error = error {
            print("error creating asset: \(error)")
        }
    }
}
```

**Objective-C**:

```objc
- (void) addNewAssetWithImage:(UIImage*)image toAlbum:(PHAssetCollection*)album 
{
    [[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
        // Request creating an asset from the image.
        PHAssetChangeRequest* createAssetRequest = [PHAssetChangeRequest creationRequestForAssetFromImage:image];
         // Request editing the album.
        PHAssetCollectionChangeRequest* albumChangeRequest = [PHAssetCollectionChangeRequest changeRequestForAssetCollection:album];
         // Get a placeholder for the new asset and add it to the album editing request.
        PHObjectPlaceholder* assetPlaceholder = [createAssetRequest placeholderForCreatedAsset];        [albumChangeRequest addAssets:@[ assetPlaceholder ]];
     } completionHandler:^(BOOL success, NSError* error) {
        NSLog(@"Finished adding asset. %@", (success ? @"Success" : error));
    }];
}
```

For each call to the [`performChanges(_:completionHandler:)`](https://developer.apple.com/documentation/photos/phphotolibrary/performchanges(_:completionhandler:)) or [`performChangesAndWait(_:)`](https://developer.apple.com/documentation/photos/phphotolibrary/performchangesandwait(_:)) method, Photos shows an alert asking the user for permission to edit the contents of the photo library. If your app needs to submit several changes at once, combine them into a single change block.

For example, to add several new images in one batch, extend the code to create multiple [`PHAssetChangeRequest`](https://developer.apple.com/documentation/photos/phassetchangerequest) objects using the [`creationRequestForAsset(from:)`](https://developer.apple.com/documentation/photos/phassetchangerequest/creationrequestforasset(from:)) method. To edit the content of multiple existing photos, create multiple [`PHAssetChangeRequest`](https://developer.apple.com/documentation/photos/phassetchangerequest) objects and set the [`contentEditingOutput`](https://developer.apple.com/documentation/photos/phassetchangerequest/contenteditingoutput) property on each to an independent [`PHContentEditingOutput`](https://developer.apple.com/documentation/photos/phcontenteditingoutput) object.

You can modify and delete assets in a similar way.

## See Also

### Updating the Library
- [func performChanges(() -> Void, completionHandler: ((Bool, (any Error)?) -> Void)?)](https://developer.apple.com/documentation/photos/phphotolibrary/performchanges(_:completionhandler:))
  Asynchronously runs a block that requests changes to the photo library.
- [func performChangesAndWait(() -> Void) throws](https://developer.apple.com/documentation/photos/phphotolibrary/performchangesandwait(_:))
  Synchronously runs a block that requests changes to be performed in the photo library.
- [class PHChangeRequest](https://developer.apple.com/documentation/photos/phchangerequest)
  The abstract base class of the framework’s photo library change requests.
- [class PHAssetChangeRequest](https://developer.apple.com/documentation/photos/phassetchangerequest)
  A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [class PHAssetCollectionChangeRequest](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest)
  A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [class PHCollectionListChangeRequest](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest)
  A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [class PHObjectPlaceholder](https://developer.apple.com/documentation/photos/phobjectplaceholder)
  A read-only proxy object that represents a Photos asset or collection to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photokit/requesting-changes-to-the-photo-library)*