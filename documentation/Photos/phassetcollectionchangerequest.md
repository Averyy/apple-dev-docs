# PHAssetCollectionChangeRequest

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetCollectionChangeRequest
```

```objc
@interface PHAssetCollectionChangeRequest : PHChangeRequest
```

## Mentions

- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)

## Overview

You use the [`PHAssetCollectionChangeRequest`](./phassetcollectionchangerequest.md) class to request changes for [`PHAssetCollection`](./phassetcollection.md) objects. To make changes to asset collections (such as user-created albums) in the Photos library, create a change request using the appropriate class method for the change you want to perform.

- Call the [`creationRequestForAssetCollection(withTitle:)`](./phassetcollectionchangerequest/creationrequestforassetcollection%28withtitle%29.md) method to create a new asset collection.
- Call the [`deleteAssetCollections(_:)`](./phassetcollectionchangerequest/deleteassetcollections%28_%29.md) method to delete existing asset collections.
- Call the [`init(for:)`](./phassetcollectionchangerequest/init%28for%29.md) or [`init(for:assets:)`](./phassetcollectionchangerequest/init%28for,assets%29.md) method to modify a collection’s metadata or list of member assets.

Before creating a change request, use the [`canPerform(_:)`](./phcollection/canperform%28_%29.md) method to verify that the collection allows the edit operation you’re requesting. If you attempt to perform an unsupported edit operation, Photos throws an exception.

A change request for creating or modifying an asset collection works like a mutable version of the asset collection object. Use the change request’s properties and instance methods to request changes to the asset collection itself. For example, the following code removes an asset from an album.

**Swift**:

```swift
PHPhotoLibrary.shared().performChanges {

    let request = PHAssetCollectionChangeRequest(for: myAlbum,
                                                 assets: albumAssetsFetchResult)
    
    request!.removeAssets([asset] as NSFastEnumeration)

} completionHandler: { success, error in
    print("Finished removing the asset from the album. \(success ? "Success" : String(describing: error))")
}
```

**Objective-C**:

```objc
[[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
        
    PHAssetCollectionChangeRequest *request =
        [PHAssetCollectionChangeRequest changeRequestForAssetCollection:myAlbum
                                                                 assets:albumAssetsFetchResult];
        
    [request removeAssets:@[asset]];
     
} completionHandler:^(BOOL success, NSError *error) {
    NSLog(@"Finished removing the asset from the album. %@", (success ? @"Success" : error));
}];
```

After Photos runs the change block and calls your completion handler, the asset collection’s state reflects the changes you requested in the block.

If you create or use a change request object outside a photo library change block, Photos raises an Objective-C exception. For details on change blocks, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Adding New Asset Collections
- [class func creationRequestForAssetCollection(withTitle: String) -> Self](./phassetcollectionchangerequest/creationrequestforassetcollection%28withtitle%29.md)
  Creates a request for adding a new asset collection to the Photos library.
- [var placeholderForCreatedAssetCollection: PHObjectPlaceholder](./phassetcollectionchangerequest/placeholderforcreatedassetcollection.md)
  A placeholder object for the asset collection that the change request creates.
### Deleting Asset Collections
- [class func deleteAssetCollections(any NSFastEnumeration)](./phassetcollectionchangerequest/deleteassetcollections%28_%29.md)
  Requests that the specified asset collections be deleted.
### Modifying Asset Collections
- [convenience init?(for: PHAssetCollection)](./phassetcollectionchangerequest/init%28for%29.md)
  Creates a request for modifying the specified asset collection.
- [convenience init?(for: PHAssetCollection, assets: PHFetchResult<PHAsset>?)](./phassetcollectionchangerequest/init%28for,assets%29.md)
  Creates a request for modifying the specified asset collection, with a fetch result for tracking changes.
- [var title: String](./phassetcollectionchangerequest/title.md)
  The displayed name of the asset collection.
- [func addAssets(any NSFastEnumeration)](./phassetcollectionchangerequest/addassets%28_%29.md)
  Adds the specified assets to the asset collection.
- [func insertAssets(any NSFastEnumeration, at: IndexSet)](./phassetcollectionchangerequest/insertassets%28_,at%29.md)
  Inserts the specified assets into the collection at the specified indexes.
- [func removeAssets(any NSFastEnumeration)](./phassetcollectionchangerequest/removeassets%28_%29.md)
  Removes the specified assets from the asset collection.
- [func removeAssets(at: IndexSet)](./phassetcollectionchangerequest/removeassets%28at%29.md)
  Removes the assets at the specified indexes from the asset collection.
- [func replaceAssets(at: IndexSet, withAssets: any NSFastEnumeration)](./phassetcollectionchangerequest/replaceassets%28at,withassets%29.md)
  Replaces the assets at the specified indexes in the asset collection with the specified assets.
- [func moveAssets(at: IndexSet, to: Int)](./phassetcollectionchangerequest/moveassets%28at,to%29.md)
  Moves the assets at the specified indexes in the asset collection to a new index.
### Initializers
- [convenience init?(forAssetCollection: PHAssetCollection)](./phassetcollectionchangerequest/init%28forassetcollection%29.md)
- [convenience init?(forAssetCollection: PHAssetCollection, assets: PHFetchResult<PHAsset>?)](./phassetcollectionchangerequest/init%28forassetcollection,assets%29.md)

## Relationships

### Inherits From
- [PHChangeRequest](./phchangerequest.md)
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
- [class PHAssetChangeRequest](./phassetchangerequest.md)
  A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [class PHCollectionListChangeRequest](./phcollectionlistchangerequest.md)
  A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [class PHObjectPlaceholder](./phobjectplaceholder.md)
  A read-only proxy object that represents a Photos asset or collection to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollectionchangerequest)*