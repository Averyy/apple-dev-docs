# fetchAssetCollections(withLocalIdentifiers:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves asset collections with the specified unique identifiers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchAssetCollections(withLocalIdentifiers identifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>
```

```objc
+ (PHFetchResult<PHAssetCollection *> *) fetchAssetCollectionsWithLocalIdentifiers:(NSArray<NSString *> *) identifiers options:(PHFetchOptions *) options;
```

## Return Value

A fetch result that contains the requested [`PHAssetCollection`](../phassetcollection.md) objects, or an empty fetch result if no objects match the request.

## Parameters

- `identifiers`: An array of `NSString` objects, each the [`localIdentifier`](../phobject/localidentifier.md) string of an asset collection.
- `options`: Options that specify a filter predicate and sort order for the fetched asset collections, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Asset Collections
- [class func fetchAssetCollections(with: PHAssetCollectionType, subtype: PHAssetCollectionSubtype, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollections%28with,subtype,options%29.md)
  Retrieves asset collections of the specified type and subtype.
- [class func fetchAssetCollectionsContaining(PHAsset, with: PHAssetCollectionType, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollectionscontaining%28_,with,options%29.md)
  Retrieves asset collections of the specified type containing the specified asset.
- [class func fetchAssetCollections(withALAssetGroupURLs: [URL], options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchassetcollections%28withalassetgroupurls,options%29.md)
  Retrieves asset collections using URLs provided by the Assets Library framework.
- [class func fetchMoments(inMomentList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchmoments%28inmomentlist,options%29.md)
  Retrieves asset collections in the specified moment list collection.
- [class func fetchMoments(with: PHFetchOptions?) -> PHFetchResult<PHAssetCollection>](./fetchmoments%28with%29.md)
  Retrieves asset collections corresponding to moments seen in the Photos app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection/fetchassetcollections(withlocalidentifiers:options:))*