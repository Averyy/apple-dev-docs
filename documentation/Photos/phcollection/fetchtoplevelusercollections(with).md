# fetchTopLevelUserCollections(with:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Retrieves collections from the root of the photo library’s hierarchy of user-created albums and folders.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func fetchTopLevelUserCollections(with options: PHFetchOptions?) -> PHFetchResult<PHCollection>
```

```objc
+ (PHFetchResult<PHCollection *> *) fetchTopLevelUserCollectionsWithOptions:(PHFetchOptions *) options;
```

#### Return Value

A fetch result that contains the requested [`PHCollection`](../phcollection.md) objects, or an empty fetch result if no objects match the request.

## Parameters

- `options`: Options that specify a filter predicate and sort order for the fetched collections, or `nil` to use default options. For details, see [`PHFetchOptions`](../phfetchoptions.md).

## See Also

### Fetching Collections
- [class func fetchCollections(in: PHCollectionList, options: PHFetchOptions?) -> PHFetchResult<PHCollection>](./fetchcollections%28in,options%29.md)
  Retrieves collections from the specified collection list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollection/fetchtoplevelusercollections(with:))*