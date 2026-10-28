# transientCollectionList(with:title:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a temporary collection list that contains the specified asset collections.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func transientCollectionList(with collections: [PHCollection], title: String?) -> PHCollectionList
```

```objc
+ (PHCollectionList *) transientCollectionListWithCollections:(NSArray<PHCollection *> *) collections title:(NSString *) title;
```

## Return Value

A new collection list.

## Discussion

Transient collection lists are not saved to local storage or iCloud and do not appear in the Photos application or other apps using the Photos framework. A transient collection can be useful if you’ve designed a UI for displaying the contents of a collection list and want to display an arbitrary set of collections.

## Parameters

- `collections`: An array of [`PHAssetCollection`](../phassetcollection.md) objects.
- `title`: A name for the new temporary collection list.

## See Also

### Creating Temporary Collection Lists
- [class func transientCollectionList(withCollectionsFetchResult: PHFetchResult<PHCollection>, title: String?) -> PHCollectionList](./transientcollectionlist%28withcollectionsfetchresult,title%29.md)
  Creates a temporary collection list containing the asset collections in the specified fetch result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/transientcollectionlist(with:title:))*