# fetchAssetCollections(with:subtype:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves asset collections of the specified type and subtype.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchAssetCollections(with type: PHAssetCollectionType, subtype: PHAssetCollectionSubtype, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

```objc
+ (PHFetchResult<PHAssetCollection *> *) fetchAssetCollectionsWithType:(PHAssetCollectionType) type subtype:(PHAssetCollectionSubtype) subtype options:(PHFetchOptions *) options;
```

#### Return Value

A fetch result that contains the requested [`PHAssetCollection`](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

#### Discussion

By default, the returned [`PHFetchResult`](../phfetchresult.md) object contains all asset collections with the specified type and subtype. To retrieve a more specific set of asset collections, provide a [`PHFetchOptions`](../phfetchoptions.md) object containing a filter predicate.

## Parameters

- `type`: A type of asset collection, such as an album or a moment. See [`PHAssetCollectionType`](../phassetcollectiontype.md).
- `subtype`: A subtype of asset collection. See [`PHAssetCollectionSubtype`](../phassetcollectionsubtype.md).
- `options`: Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Asset Collections
- [class func fetchAssetCollections(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollections%28withlocalidentifiers,options%29.md)
  Retrieves asset collections with the specified unique identifiers.
- [class func fetchAssetCollectionsContaining(PHAsset, with: PHAssetCollectionType, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollectionscontaining%28_,with,options%29.md)
  Retrieves asset collections of the specified type containing the specified asset.
- [class func fetchAssetCollections(withALAssetGroupURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollections%28withalassetgroupurls,options%29.md)
  Retrieves asset collections using URLs provided by the Assets Library framework.
- [class func fetchMoments(inMomentList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchmoments%28inmomentlist,options%29.md)
  Retrieves asset collections in the specified moment list collection.
- [class func fetchMoments(with: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchmoments%28with%29.md)
  Retrieves asset collections corresponding to moments seen in the Photos app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection/fetchassetcollections(with:subtype:options:))*