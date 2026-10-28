# PHFetchOptions

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A set of options that affect the filtering, sorting, and management of results that Photos returns when you fetch asset or collection objects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHFetchOptions
```

```objc
@interface PHFetchOptions : NSObject
```

## Mentions

- [Fetching Assets](../PhotoKit/fetching-assets.md)

## Overview

Using class methods on the [`PHAsset`](./phasset.md), [`PHCollection`](./phcollection.md), [`PHAssetCollection`](./phassetcollection.md), and [`PHCollectionList`](./phcollectionlist.md) classes to fetch assets or collections produces a [`PHFetchResult`](./phfetchresult.md) object containing the requested objects. The options you specify control which objects the fetch result includes, how those objects are arranged in the fetch result, and how Photos should notify your app of changes to the fetch result.

Photos supports only a restricted set of keys for the [`predicate`](./phfetchoptions/predicate.md) and [`sortDescriptors`](./phfetchoptions/sortdescriptors.md) properties. The set of available keys depends on which class you’re using to fetch assets or collections. The following table lists the keys supported by each class:

| Class for Fetch Method | Supported Keys |
| --- | --- |
| [`PHAsset`](./phasset.md) | `SELF`, [`localIdentifier`](./phobject/localidentifier.md), [`creationDate`](./phasset/creationdate.md), [`modificationDate`](./phasset/modificationdate.md), [`mediaType`](./phasset/mediatype.md), [`mediaSubtypes`](./phasset/mediasubtypes.md), [`duration`](./phasset/duration.md), [`pixelWidth`](./phasset/pixelwidth.md), [`pixelHeight`](./phasset/pixelheight.md), [`isFavorite`](./phasset/isfavorite.md) (or `isFavorite`), [`isHidden`](./phasset/ishidden.md) (or `isHidden`), [`burstIdentifier`](./phasset/burstidentifier.md) |
| [`PHAssetCollection`](./phassetcollection.md) | `SELF`, [`localIdentifier`](./phobject/localidentifier.md), [`localizedTitle`](./phcollection/localizedtitle.md) (or `title`), [`startDate`](./phassetcollection/startdate.md), [`endDate`](./phassetcollection/enddate.md), [`estimatedAssetCount`](./phassetcollection/estimatedassetcount.md) |
| [`PHCollectionList`](./phcollectionlist.md) | `SELF`, [`localIdentifier`](./phobject/localidentifier.md), [`localizedTitle`](./phcollection/localizedtitle.md) (or `title`), [`startDate`](./phcollectionlist/startdate.md), [`endDate`](./phcollectionlist/enddate.md) |
| [`PHCollection`](./phcollection.md) (can fetch a mix of [`PHCollectionList`](./phcollectionlist.md) and [`PHAssetCollection`](./phassetcollection.md) objects) | `SELF`, [`localIdentifier`](./phobject/localidentifier.md), [`localizedTitle`](./phcollection/localizedtitle.md) (or `title`), [`startDate`](./phcollectionlist/startdate.md), [`endDate`](./phcollectionlist/enddate.md) |

## Topics

### Sorting and Filtering Fetch Results
- [var predicate: NSPredicate?](./phfetchoptions/predicate.md)
  A predicate that specifies which properties to select results by and that also specifies any constraints on selection.
- [var sortDescriptors: [NSSortDescriptor]?](./phfetchoptions/sortdescriptors.md)
  A list of sort descriptors, specifying an order for the fetched objects.
### Subscribing to Changes
- [var wantsIncrementalChangeDetails: Bool](./phfetchoptions/wantsincrementalchangedetails.md)
  A Boolean value that determines whether your app receives detailed change information for the objects in the fetch result.
### Limiting Fetch Results
- [var fetchLimit: Int](./phfetchoptions/fetchlimit.md)
  The maximum number of objects to include in the fetch result.
- [var includeAllBurstAssets: Bool](./phfetchoptions/includeallburstassets.md)
  A Boolean value that determines whether the fetch result includes all assets from burst photo sequences.
- [var includeHiddenAssets: Bool](./phfetchoptions/includehiddenassets.md)
  A Boolean value that determines whether the fetch result includes assets marked as hidden.
- [var includeAssetSourceTypes: PHAssetSourceType](./phfetchoptions/includeassetsourcetypes.md)
  The set of source types for which to include assets in the fetch result.
- [var prefetchAssetExtendedMetadata: Bool](./phfetchoptions/prefetchassetextendedmetadata.md)
  A Boolean value to fetch `PHAssetExtendedMetadata` when the asset is also fetched.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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
- [class PHObject](./phobject.md)
  The abstract superclass for Photos model objects, including assets and collections.
- [class PHFetchResult](./phfetchresult.md)
  An ordered list of assets or collections returned from a Photos fetch method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchoptions)*