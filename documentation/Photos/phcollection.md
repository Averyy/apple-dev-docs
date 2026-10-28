# PHCollection

**Framework**: Photos  
**Kind**: class  
**Role**: Class

The abstract superclass for Photos asset collections and collection lists.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHCollection
```

```objc
@interface PHCollection : PHObject
```

## Overview

You do not create or work with instances of this class directly. Instead, use one of its two concrete subclasses, [`PHAssetCollection`](./phassetcollection.md) or [`PHCollectionList`](./phcollectionlist.md).

- A [`PHAssetCollection`](./phassetcollection.md) object represents a collection of photo or video assets, such as an album, moment, or Shared Photo Stream.
- A [`PHCollectionList`](./phcollectionlist.md) object represents a collection that contains other collections, such as a a folder containing albums or the set of all moments in a calendar year.

> ❗ **Important**:  Accessing or modifying the Photos library requires explicit authorization from the user. The first time you call one of the methods listed in the Fetching Collections group, Photos automatically prompts the user for authorization. (Alternatively, you can use the [`PHPhotoLibrary`](./phphotolibrary.md) [`requestAuthorization(_:)`](./phphotolibrary/requestauthorization%28_%29.md) method to prompt the user at a time of your choosing.)
>
> Your app’s `Info.plist` file must provide a value for the [NSPhotoLibraryUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW17) key that explains to the user why your app is requesting Photos access. Apps linked on or after iOS 10.0 will crash if this key is not present.

## Topics

### Fetching Collections
- [class func fetchCollections(in: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHCollection>](./phcollection/fetchcollections%28in,options%29.md)
  Retrieves collections from the specified collection list.
- [class func fetchTopLevelUserCollections(with: PHFetchOptions?) -> PHFetchResult<PHCollection>](./phcollection/fetchtoplevelusercollections%28with%29.md)
  Retrieves collections from the root of the photo library’s hierarchy of user-created albums and folders.
### Reading Collection Metadata
- [var localizedTitle: String?](./phcollection/localizedtitle.md)
  The localized name of the collection.
### Determining Collection Capabilities
- [var canContainAssets: Bool](./phcollection/cancontainassets.md)
  A Boolean value indicating whether the collection can contain assets.
- [var canContainCollections: Bool](./phcollection/cancontaincollections.md)
  A Boolean value indicating whether the collection can contain other collections.
- [func canPerform(PHCollectionEditOperation) -> Bool](./phcollection/canperform%28_%29.md)
  Returns whether the collection supports the specified editing operation.
- [enum PHCollectionEditOperation](./phcollectioneditoperation.md)
  Values identifying possible actions that a collection can support, used by the [`canPerform(_:)`](./phcollection/canperform%28_%29.md) method.
### Instance Properties
- [var modificationDate: Date?](./phcollection/modificationdate.md)
  The last date at which this collection was modified.

## Relationships

### Inherits From
- [PHObject](./phobject.md)
### Inherited By
- [PHAssetCollection](./phassetcollection.md)
- [PHCollectionList](./phcollectionlist.md)
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
- [class PHCollectionList](./phcollectionlist.md)
  A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [class PHObject](./phobject.md)
  The abstract superclass for Photos model objects, including assets and collections.
- [class PHFetchResult](./phfetchresult.md)
  An ordered list of assets or collections returned from a Photos fetch method.
- [class PHFetchOptions](./phfetchoptions.md)
  A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollection)*