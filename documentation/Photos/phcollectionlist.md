# PHCollectionList

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A group containing Photos asset collections, such as Moments, Years, or folders of user-created albums.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHCollectionList
```

```objc
@interface PHCollectionList : PHCollection
```

## Mentions

- [Fetching Objects and Requesting Changes](../PhotoKit/fetching-objects-and-requesting-changes.md)
- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)

#### Overview

In the Photos framework, collection objects (including asset collections) do not directly reference their member objects, and there are no other objects that directly reference collection objects. To retrieve the members of a collection list, fetch them with a [`PHCollection`](./phcollection.md) class method such as [`fetchCollections(in:options:)`](./phcollection/fetchcollections%28in,options%29.md). To find objects at the root of the collection list hierarchy (such as album folders with no parent folders), use the [`fetchTopLevelUserCollections(with:)`](./phcollection/fetchtoplevelusercollections%28with%29.md) method.

> ❗ **Important**:  Accessing or modifying the Photos library requires explicit authorization from the user. The first time you call one of the methods listed in the Fetching Collection Lists group, Photos automatically prompts the user for authorization. (Alternatively, you can use the [`PHPhotoLibrary`](./phphotolibrary.md) [`requestAuthorization(_:)`](./phphotolibrary/requestauthorization%28_%29.md) method to prompt the user at a time of your choosing.)
>
> Your app’s `Info.plist` file must provide a value for the [NSPhotoLibraryUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW17) key that explains to the user why your app is requesting Photos access. Apps linked on or after iOS 10.0 will crash if this key is not present.

Like assets and asset collections, collection lists are immutable. To create, rename, or delete collection lists, or to add, remove, or rearrange members in a collection list, create a [`PHCollectionListChangeRequest`](./phcollectionlistchangerequest.md) object within a photo library change block. For details on using change requests and change blocks to update the photo library, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Fetching Collection Lists
- [class func fetchCollectionListsContaining(PHCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./phcollectionlist/fetchcollectionlistscontaining%28_,options%29.md)
  Retrieves collection lists that contain the specified collection.
- [class func fetchCollectionLists(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./phcollectionlist/fetchcollectionlists%28withlocalidentifiers,options%29.md)
  Retrieves collection lists with the specified local-device-specific unique identifiers.
- [class func fetchCollectionLists(with: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./phcollectionlist/fetchcollectionlists%28with,subtype,options%29.md)
  Retrieves collection lists of the specified type.
- [class func fetchMomentLists(with: PHCollectionListSubtype, containingMoment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./phcollectionlist/fetchmomentlists%28with,containingmoment,options%29.md)
  Retrieves collection lists of the specified moment list type containing the specified moment.
- [class func fetchMomentLists(with: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./phcollectionlist/fetchmomentlists%28with,options%29.md)
  Retrieves collection lists of the specified moment list type.
### Reading Collection List Metadata
- [var collectionListType: PHCollectionListType](./phcollectionlist/collectionlisttype.md)
  The type of asset collection group that the collection list represents.
- [enum PHCollectionListType](./phcollectionlisttype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListType`](./phcollectionlist/collectionlisttype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./phcollectionlist/fetchcollectionlists%28with,subtype,options%29.md) method.
- [var collectionListSubtype: PHCollectionListSubtype](./phcollectionlist/collectionlistsubtype.md)
  The type of asset collection grouping the collection list represents.
- [enum PHCollectionListSubtype](./phcollectionlistsubtype.md)
  Major distinctions between kinds of collection list, used by the [`collectionListSubtype`](./phcollectionlist/collectionlistsubtype.md) property and [`fetchCollectionLists(with:subtype:options:)`](./phcollectionlist/fetchcollectionlists%28with,subtype,options%29.md), [`fetchMomentLists(with:containingMoment:options:)`](./phcollectionlist/fetchmomentlists%28with,containingmoment,options%29.md), and [`fetchMomentLists(with:options:)`](./phcollectionlist/fetchmomentlists%28with,options%29.md) methods.
- [var startDate: Date?](./phcollectionlist/startdate.md)
  The earliest creation date among all assets in the collection list.
- [var endDate: Date?](./phcollectionlist/enddate.md)
  The latest creation date among all assets in the collection list.
- [var localizedLocationNames: [String]](./phcollectionlist/localizedlocationnames.md)
  The names of locations grouped by the collection (an array of `NSString` objects).
### Creating Temporary Collection Lists
- [class func transientCollectionList(with: [PHCollection], title: String?) -> PHCollectionList](./phcollectionlist/transientcollectionlist%28with,title%29.md)
  Creates a temporary collection list that contains the specified asset collections.
- [class func transientCollectionList(withCollectionsFetchResult: PHFetchResult<PHCollection>, title: String?) -> PHCollectionList](./phcollectionlist/transientcollectionlist%28withcollectionsfetchresult,title%29.md)
  Creates a temporary collection list containing the asset collections in the specified fetch result.

## Relationships

### Inherits From
- [PHCollection](./phcollection.md)
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
- [class PHObject](./phobject.md)
  The abstract superclass for Photos model objects, including assets and collections.
- [class PHFetchResult](./phfetchresult.md)
  An ordered list of assets or collections returned from a Photos fetch method.
- [class PHFetchOptions](./phfetchoptions.md)
  A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist)*