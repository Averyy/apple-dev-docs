# fetchCollectionLists(with:subtype:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves collection lists of the specified type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchCollectionLists(with collectionListType: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

```objc
+ (PHFetchResult<PHCollectionList *> *) fetchCollectionListsWithType:(PHCollectionListType) collectionListType subtype:(PHCollectionListSubtype) subtype options:(PHFetchOptions *) options;
```

#### Return Value

A fetch result that contains the requested [`PHCollectionList`](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

#### Discussion

By default, the returned [`PHFetchResult`](../phfetchresult.md) object contains all collection lists with the specified type and subtype. To retrieve a more specific set of collection lists, provide a [`PHFetchOptions`](../phfetchoptions.md) object containing a filter predicate.

## Parameters

- `collectionListType`: A type of collection list. See [`PHCollectionListType`](../phcollectionlisttype.md).
- `subtype`: A subtype of collection list. See [`PHCollectionListSubtype`](../phcollectionlistsubtype.md).
- `options`: Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Collection Lists
- [class func fetchCollectionListsContaining(PHCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlistscontaining%28_,options%29.md)
  Retrieves collection lists that contain the specified collection.
- [class func fetchCollectionLists(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlists%28withlocalidentifiers,options%29.md)
  Retrieves collection lists with the specified local-device-specific unique identifiers.
- [class func fetchMomentLists(with: PHCollectionListSubtype, containingMoment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchmomentlists%28with,containingmoment,options%29.md)
  Retrieves collection lists of the specified moment list type containing the specified moment.
- [class func fetchMomentLists(with: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchmomentlists%28with,options%29.md)
  Retrieves collection lists of the specified moment list type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/fetchcollectionlists(with:subtype:options:))*