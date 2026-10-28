# fetchCollections(in:options:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves collections from the specified collection list.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchCollections(in collectionList: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHCollection>
```

```objc
+ (PHFetchResult<PHCollection *> *) fetchCollectionsInCollectionList:(PHCollectionList *) collectionList options:(PHFetchOptions *) options;
```

## Return Value

A fetch result that contains the requested [`PHCollection`](../phcollection.md) objects, or an empty fetch result if no objects match the request.

## Discussion

By default, the returned [`PHFetchResult`](../phfetchresult.md) object contains all collections in the specified collection list. To retrieve a more specific set of assets, provide a [`PHFetchOptions`](../phfetchoptions.md) object that contains a filter predicate.

## Parameters

- `collectionList`: The collection list from which to fetch collections.
- `options`: Options that specify a filter predicate and sort order for the fetched collections, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Collections
- [class func fetchTopLevelUserCollections(with: PHFetchOptions?) -> PHFetchResult<PHCollection>](./fetchtoplevelusercollections%28with%29.md)
  Retrieves collections from the root of the photo library’s hierarchy of user-created albums and folders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollection/fetchcollections(in:options:))*