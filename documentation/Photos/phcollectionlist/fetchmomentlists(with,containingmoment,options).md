# fetchMomentLists(with:containingMoment:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves collection lists of the specified moment list type containing the specified moment.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+
- tvOS 10.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Will be removed in a future release

## Declaration

```swift
class func fetchMomentLists(with momentListSubtype: PHCollectionListSubtype, containingMoment moment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

```objc
+ (PHFetchResult<PHCollectionList *> *) fetchMomentListsWithSubtype:(PHCollectionListSubtype) momentListSubtype containingMoment:(PHAssetCollection *) moment options:(PHFetchOptions *) options;
```

## Return Value

A fetch result that contains the requested [`PHCollectionList`](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

## Discussion

The Photos app automatically creates moments to group assets by time and location, and also creates moment lists to group related moments. Moment lists have two subtypes: a moment cluster groups a few related moments, and a moment year groups all moments in a calendar year.

## Parameters

- `momentListSubtype`: The type of moment list, either [`PHCollectionListSubtype.momentListCluster`](../phcollectionlistsubtype/momentlistcluster.md) or [`PHCollectionListSubtype.momentListYear`](../phcollectionlistsubtype/momentlistyear.md). See [`PHCollectionListSubtype`](../phcollectionlistsubtype.md).
- `moment`: An asset collection whose type is [`PHAssetCollectionType.moment`](../phassetcollectiontype/moment.md).
- `options`: Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Collection Lists
- [class func fetchCollectionListsContaining(PHCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlistscontaining%28_,options%29.md)
  Retrieves collection lists that contain the specified collection.
- [class func fetchCollectionLists(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlists%28withlocalidentifiers,options%29.md)
  Retrieves collection lists with the specified local-device-specific unique identifiers.
- [class func fetchCollectionLists(with: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlists%28with,subtype,options%29.md)
  Retrieves collection lists of the specified type.
- [class func fetchMomentLists(with: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchmomentlists%28with,options%29.md)
  Retrieves collection lists of the specified moment list type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/fetchmomentlists(with:containingmoment:options:))*