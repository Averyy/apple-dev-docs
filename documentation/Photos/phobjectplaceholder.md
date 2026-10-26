# PHObjectPlaceholder

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A read-only proxy object that represents a Photos asset or collection to create.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHObjectPlaceholder
```

```objc
@interface PHObjectPlaceholder : PHObject
```

## Mentions

- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Overview

You obtain object placeholders when you use change requests to create assets, collections, or collection lists. After the change request completes, you can use the object placeholder to fetch the newly created object. You can also use an object placeholder to make additional change requests involving the object to create.

For example, the following code uses a placeholder to add a newly created asset to an album.

**Swift**:

```swift
let createAssetRequest = PHAssetChangeRequest.creationRequestForAsset(from: image)
let assetPlaceholder = createAssetRequest.placeholderForCreatedAsset!
let albumChangeRequest = PHAssetCollectionChangeRequest(for: album)
albumChangeRequest!.addAssets([assetPlaceholder] as NSFastEnumeration)
```

**Objective-C**:

```objc
PHAssetChangeRequest *createAssetRequest =
    [PHAssetChangeRequest creationRequestForAssetFromImage:image];
PHObjectPlaceholder *assetPlaceholder = createAssetRequest.placeholderForCreatedAsset;
PHAssetCollectionChangeRequest *albumChangeRequest =
    [PHAssetCollectionChangeRequest changeRequestForAssetCollection:album];
[albumChangeRequest addAssets:@[ assetPlaceholder ]];
```

A placeholder always has the same local identifier as the asset, collection, or collection list that it represents. To find the object that corresponds to a placeholder, read the placeholder’s [`localIdentifier`](./phobject/localidentifier.md) property and use it to fetch the actual object. Alternatively, because the [`PHObjectPlaceholder`](./phobjectplaceholder.md) class implements the `==` and [`hash`](../ObjectiveC/nsobjectprotocol/hash.md) methods in terms of its [`localIdentifier`](./phobject/localidentifier.md) property, you can also find the object for a placeholder using techniques that depend on these methods.

## Relationships

### Inherits From
- [PHObject](./phobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [class PHCollectionListChangeRequest](./phcollectionlistchangerequest.md)
  A request to create, delete, or modify a Photos collection list, for use in a photo library change block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobjectplaceholder)*