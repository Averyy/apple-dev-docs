# PHObject

**Framework**: Photos  
**Kind**: class  
**Role**: Class

The abstract superclass for Photos model objects, including assets and collections.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHObject
```

```objc
@interface PHObject : NSObject
```

## Overview

You do not create or use instances of this class directly. Instead, work with instances of its concrete subclasses—[`PHAsset`](./phasset.md), [`PHAssetCollection`](./phassetcollection.md), [`PHCollectionList`](./phcollectionlist.md), and [`PHObjectPlaceholder`](./phobjectplaceholder.md).

Because the [`PHObject`](./phobject.md) class implements the [`isEqual(_:)`](../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) and [`hash`](../ObjectiveC/nsobjectprotocol/hash.md) methods in terms of its [`localIdentifier`](./phobject/localidentifier.md) property, you can use techniques that depend on these methods to keep track of asset and collection objects.

## Topics

### Identifying an Object
- [var localIdentifier: String](./phobject/localidentifier.md)
  A unique string that persistently identifies the object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [PHAsset](./phasset.md)
- [PHAssetResourceUploadJob](./phassetresourceuploadjob.md)
- [PHCollection](./phcollection.md)
- [PHObjectPlaceholder](./phobjectplaceholder.md)
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

### Asset retrieval
- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)
  Get assets, asset collections, and collection lists matching a specified query.
- [class PHAsset](./phasset.md)
  A representation of an image, video, or Live Photo in the Photos library.
- [class PHAssetCollection](./phassetcollection.md)
  A representation of a Photos asset grouping, such as Moments, a user-created album, or a Smart Album.
- [class PHCollection](./phcollection.md)
  The abstract superclass for Photos asset collections and collection lists.
- [class PHCollectionList](./phcollectionlist.md)
  A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [class PHFetchResult](./phfetchresult.md)
  An ordered list of assets or collections returned from a Photos fetch method.
- [class PHFetchOptions](./phfetchoptions.md)
  A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phobject)*