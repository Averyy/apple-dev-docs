# fetchCollectionListsContaining(_:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves collection lists that contain the specified collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchCollectionListsContaining(_ collection: PHCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

```objc
+ (PHFetchResult<PHCollectionList *> *) fetchCollectionListsContainingCollection:(PHCollection *) collection options:(PHFetchOptions *) options;
```

#### Return Value

A fetch result that contains the requested [`PHCollectionList`](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

#### Discussion

Different kinds of collections have different containment possibilities. For example, an asset collection whose type is [`PHAssetCollectionType.album`](../phassetcollectiontype/album.md) may be contained in a folder, or have no containing collection list. A folder, in turn, may be contained in another folder. An asset collection whose type is [`PHAssetCollectionType.moment`](../phassetcollectiontype/moment.md) is always contained by two collection lists: a moment cluster and a moment year.

## Parameters

- `collection`: An asset collection or another collection list.
- `options`: Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Collection Lists
- [class func fetchCollectionLists(withLocalIdentifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlists%28withlocalidentifiers,options%29.md)
  Retrieves collection lists with the specified local-device-specific unique identifiers.
- [class func fetchCollectionLists(with: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlists%28with,subtype,options%29.md)
  Retrieves collection lists of the specified type.
- [class func fetchMomentLists(with: PHCollectionListSubtype, containingMoment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchmomentlists%28with,containingmoment,options%29.md)
  Retrieves collection lists of the specified moment list type containing the specified moment.
- [class func fetchMomentLists(with: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchmomentlists%28with,options%29.md)
  Retrieves collection lists of the specified moment list type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/fetchcollectionlistscontaining(_:options:))*