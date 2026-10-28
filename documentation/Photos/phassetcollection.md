# PHAssetCollection

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A representation of a Photos asset grouping, such as Moments, a user-created album, or a Smart Album.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetCollection
```

```objc
@interface PHAssetCollection : PHCollection
```

## Mentions

- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)
- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)

## Overview

In the Photos framework, collection objects (including asset collections) do not directly reference their member objects, and there are no other objects that directly reference collection objects. To retrieve the members of an asset collection, fetch them with a [`PHAsset`](./phasset.md) class method such as [`fetchAssets(in:options:)`](./phasset/fetchassets%28in,options%29.md). To find asset collections, use one of the methods listed in the Fetching Asset Collections group below.

> ❗ **Important**:  Accessing or modifying the Photos library requires explicit authorization from the user. The first time you call one of the methods listed in the Fetching Asset Collections group, Photos automatically prompts the user for authorization. (Alternatively, you can use the [`PHPhotoLibrary`](./phphotolibrary.md)  [`requestAuthorization(_:)`](./phphotolibrary/requestauthorization%28_%29.md) method to prompt the user at a time of your choosing.)
>
> Your app’s `Info.plist` file must provide a value for the [NSPhotoLibraryUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW17) key that explains to the user why your app is requesting Photos access. Apps linked on or after iOS 10.0 will crash if this key is not present.

Like assets and collection lists, asset collections are immutable. To create, rename, or delete asset collections, or to add, remove, or rearrange members in an asset collection, create a [`PHAssetCollectionChangeRequest`](./phassetcollectionchangerequest.md) object within a photo library change block. For details on using change requests and change blocks to update the photo library, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Fetching Asset Collections
- [class func fetchAssetCollections(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./phassetcollection/fetchassetcollections%28withlocalidentifiers,options%29.md)
  Retrieves asset collections with the specified unique identifiers.
- [class func fetchAssetCollections(with: PHAssetCollectionType, subtype: PHAssetCollectionSubtype, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./phassetcollection/fetchassetcollections%28with,subtype,options%29.md)
  Retrieves asset collections of the specified type and subtype.
- [class func fetchAssetCollectionsContaining(PHAsset, with: PHAssetCollectionType, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./phassetcollection/fetchassetcollectionscontaining%28_,with,options%29.md)
  Retrieves asset collections of the specified type containing the specified asset.
- [class func fetchAssetCollections(withALAssetGroupURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./phassetcollection/fetchassetcollections%28withalassetgroupurls,options%29.md)
  Retrieves asset collections using URLs provided by the Assets Library framework.
- [class func fetchMoments(inMomentList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./phassetcollection/fetchmoments%28inmomentlist,options%29.md)
  Retrieves asset collections in the specified moment list collection.
- [class func fetchMoments(with: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./phassetcollection/fetchmoments%28with%29.md)
  Retrieves asset collections corresponding to moments seen in the Photos app.
### Reading Asset Collection Metadata
- [var assetCollectionType: PHAssetCollectionType](./phassetcollection/assetcollectiontype.md)
  The type of the asset collection, such as an album or a moment.
- [enum PHAssetCollectionType](./phassetcollectiontype.md)
  Major distinctions between kinds of asset collections, used by the [`assetCollectionType`](./phassetcollection/assetcollectiontype.md) property and the [`fetchAssetCollectionsContaining(_:with:options:)`](./phassetcollection/fetchassetcollectionscontaining%28_,with,options%29.md) and [`fetchAssetCollections(with:subtype:options:)`](./phassetcollection/fetchassetcollections%28with,subtype,options%29.md) methods.
- [var assetCollectionSubtype: PHAssetCollectionSubtype](./phassetcollection/assetcollectionsubtype.md)
  The subtype of the asset collection.
- [enum PHAssetCollectionSubtype](./phassetcollectionsubtype.md)
  Minor distinctions between kinds of asset collections, used by the [`assetCollectionSubtype`](./phassetcollection/assetcollectionsubtype.md) property and the [`fetchAssetCollections(with:subtype:options:)`](./phassetcollection/fetchassetcollections%28with,subtype,options%29.md) method.
- [var estimatedAssetCount: Int](./phassetcollection/estimatedassetcount.md)
  The estimated number of assets in the asset collection.
- [var startDate: Date?](./phassetcollection/startdate.md)
  The earliest creation date among all assets in the asset collection.
- [var endDate: Date?](./phassetcollection/enddate.md)
  The latest creation date among all assets in the asset collection.
- [var approximateLocation: CLLocation?](./phassetcollection/approximatelocation.md)
  A location representing those of all assets in the collection.
- [var localizedLocationNames: [String]](./phassetcollection/localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).
### Creating Temporary Asset Collections
- [class func transientAssetCollection(with: [PHAsset], title: String?) -> PHAssetCollection](./phassetcollection/transientassetcollection%28with,title%29.md)
  Creates a temporary asset collection containing the specified assets.
- [class func transientAssetCollection(withAssetFetchResult: PHFetchResult<PHAsset>, title: String?) -> PHAssetCollection](./phassetcollection/transientassetcollection%28withassetfetchresult,title%29.md)
  Creates a temporary asset collection containing the assets from the specified fetch result.

## Relationships

### Inherits From
- [PHCollection](./phcollection.md)
### Inherited By
- [PHProject](./phproject.md)
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
- [class PHCollection](./phcollection.md)
  The abstract superclass for Photos asset collections and collection lists.
- [class PHCollectionList](./phcollectionlist.md)
  A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.
- [class PHObject](./phobject.md)
  The abstract superclass for Photos model objects, including assets and collections.
- [class PHFetchResult](./phfetchresult.md)
  An ordered list of assets or collections returned from a Photos fetch method.
- [class PHFetchOptions](./phfetchoptions.md)
  A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection)*