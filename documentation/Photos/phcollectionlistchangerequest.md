# PHCollectionListChangeRequest

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A request to create, delete, or modify a Photos collection list, for use in a photo library change block.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHCollectionListChangeRequest
```

```objc
@interface PHCollectionListChangeRequest : PHChangeRequest
```

## Mentions

- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Overview

You use the [`PHCollectionListChangeRequest`](./phcollectionlistchangerequest.md) class to request changes for [`PHCollectionList`](./phcollectionlist.md) objects. To make changes to collection lists (such as folders containing user-created albums) in the Photos library, create a change request using the appropriate class method for the change you want to perform.

- Call the [`creationRequestForCollectionList(withTitle:)`](./phcollectionlistchangerequest/creationrequestforcollectionlist%28withtitle%29.md) method to create a new asset collection.
- Call the [`deleteCollectionLists(_:)`](./phcollectionlistchangerequest/deletecollectionlists%28_%29.md) method to delete existing asset collections.
- Call the [`init(for:)`](./phcollectionlistchangerequest/init%28for%29.md) or [`init(for:childCollections:)`](./phcollectionlistchangerequest/init%28for,childcollections%29.md) method to modify a collection’s metadata or its list of child collections.

Before creating a change request, use the [`canPerform(_:)`](./phcollection/canperform%28_%29.md) method to verify that the collection allows the edit operation you’re requesting. If you attempt to perform an unsupported edit operation, Photos throws an exception.

A change request for creating or modifying a collection list works like a mutable version of the collection list object. Use the change request’s properties and instance methods to request changes to the collection list itself. For example, the following code removes an album from a folder.

**Swift**:

```swift
PHPhotoLibrary.shared().performChanges {
            
    let request = PHCollectionListChangeRequest(for: folder,
                                                childCollections: folderContentsFetchResult)
            
    request!.removeChildCollections([album!] as NSFastEnumeration)
            
} completionHandler: { success, error in
    print("Finished removing the album from the folder. \(success ? "Success" : String(describing: error))")
}
```

**Objective-C**:

```objc
[[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
        
    PHCollectionListChangeRequest *request =
        [PHCollectionListChangeRequest changeRequestForCollectionList:folder
                                                     childCollections:folderContentsFetchResult];
        
    [request removeChildCollections:@[ album ]];
     
} completionHandler:^(BOOL success, NSError *error) {
    NSLog(@"Finished removing the album from the folder. %@", (success ? @"Success" : error));
}];
```

After Photos runs the change block and calls your completion handler, the collection list’s state reflects the changes you requested in the block.

If you create or use a change request object outside a photo library change block, Photos raises an Objective-C exception. For details on change blocks, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Creating a Change Request
- [convenience init?(for: PHCollectionList)](./phcollectionlistchangerequest/init%28for%29.md)
  Creates a request for modifying the specified collection list.
- [convenience init?(for: PHCollectionList, childCollections: PHFetchResult<PHCollection>)](./phcollectionlistchangerequest/init%28for,childcollections%29.md)
  Creates a request for modifying the specified collection list, with a fetch result for tracking changes.
- [convenience init?(forTopLevelCollectionListUserCollections: PHFetchResult<PHCollection>)](./phcollectionlistchangerequest/init%28fortoplevelcollectionlistusercollections%29.md)
  Creates a request to add, remove, or rearrange child collections in the top-level collection list.
### Managing Collection Lists
- [class func creationRequestForCollectionList(withTitle: String) -> Self](./phcollectionlistchangerequest/creationrequestforcollectionlist%28withtitle%29.md)
  Creates a request for adding a new collection list to the Photos library.
- [var placeholderForCreatedCollectionList: PHObjectPlaceholder](./phcollectionlistchangerequest/placeholderforcreatedcollectionlist.md)
  A placeholder object for the collection list that the change request creates.
- [class func deleteCollectionLists(any NSFastEnumeration)](./phcollectionlistchangerequest/deletecollectionlists%28_%29.md)
  Requests to delete the specified asset collections.
### Managing Collections
- [func addChildCollections(any NSFastEnumeration)](./phcollectionlistchangerequest/addchildcollections%28_%29.md)
  Adds the specified collections as children of the collection list.
- [func insertChildCollections(any NSFastEnumeration, at: IndexSet)](./phcollectionlistchangerequest/insertchildcollections%28_,at%29.md)
  Inserts the specified collections into the collection list at the specified indexes.
- [func moveChildCollections(at: IndexSet, to: Int)](./phcollectionlistchangerequest/movechildcollections%28at,to%29.md)
  Moves the child collections at the specified indexes in the collection list to a new index.
- [func replaceChildCollections(at: IndexSet, withChildCollections: any NSFastEnumeration)](./phcollectionlistchangerequest/replacechildcollections%28at,withchildcollections%29.md)
  Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [func removeChildCollections(any NSFastEnumeration)](./phcollectionlistchangerequest/removechildcollections%28_%29.md)
  Removes the specified child collections from the collection list.
- [func removeChildCollections(at: IndexSet)](./phcollectionlistchangerequest/removechildcollections%28at%29.md)
  Removes the child collections at the specified indexes from the collection list.
### Inspecting the Request
- [var title: String](./phcollectionlistchangerequest/title.md)
  The displayed name of the collection list.
### Initializers
- [convenience init?(forCollectionList: PHCollectionList)](./phcollectionlistchangerequest/init%28forcollectionlist%29.md)
- [convenience init?(forCollectionList: PHCollectionList, childCollections: PHFetchResult<PHCollection>)](./phcollectionlistchangerequest/init%28forcollectionlist,childcollections%29.md)

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
- [class PHAssetCollectionChangeRequest](./phassetcollectionchangerequest.md)
  A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [class PHObjectPlaceholder](./phobjectplaceholder.md)
  A read-only proxy object that represents a Photos asset or collection to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlistchangerequest)*