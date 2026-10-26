# fetchCollectionLists(withLocalIdentifiers:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves collection lists with the specified local-device-specific unique identifiers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchCollectionLists(withLocalIdentifiers identifiers: [String], options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>
```

```objc
+ (PHFetchResult<PHCollectionList *> *) fetchCollectionListsWithLocalIdentifiers:(NSArray<NSString *> *) identifiers options:(PHFetchOptions *) options;
```

#### Return Value

A fetch result that contains the requested [`PHCollectionList`](../phcollectionlist.md) objects, or an empty fetch result if no objects match the request.

## Parameters

- `identifiers`: An array of `NSString` objects, each the [`localIdentifier`](../phobject/localidentifier.md) string of a collection list.
- `options`: Options that specify a filter predicate and sort order for the fetched collection lists, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Collection Lists
- [class func fetchCollectionListsContaining(PHCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlistscontaining%28_,options%29.md)
  Retrieves collection lists that contain the specified collection.
- [class func fetchCollectionLists(with: PHCollectionListType, subtype: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchcollectionlists%28with,subtype,options%29.md)
  Retrieves collection lists of the specified type.
- [class func fetchMomentLists(with: PHCollectionListSubtype, containingMoment: PHAssetCollection, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchmomentlists%28with,containingmoment,options%29.md)
  Retrieves collection lists of the specified moment list type containing the specified moment.
- [class func fetchMomentLists(with: PHCollectionListSubtype, options: PHFetchOptions?) -> PHFetchResult<PHCollectionList>](./fetchmomentlists%28with,options%29.md)
  Retrieves collection lists of the specified moment list type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/fetchcollectionlists(withlocalidentifiers:options:))*