# transientCollectionList(withCollectionsFetchResult:title:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a temporary collection list containing the asset collections in the specified fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func transientCollectionList(withCollectionsFetchResult fetchResult: PHFetchResult<PHCollection>, title: String?) -> PHCollectionList
```

```objc
+ (PHCollectionList *) transientCollectionListWithCollectionsFetchResult:(PHFetchResult<PHCollection *> *) fetchResult title:(NSString *) title;
```

#### Return Value

A new collection list.

#### Discussion

Transient collection lists are not saved to local storage or iCloud and do not appear in the Photos application or other apps using the Photos framework. A transient collection can be useful if you’ve designed a UI for displaying the contents of a collection list and want to display an arbitrary set of collections.

## Parameters

- `fetchResult`: A fetch result that contains one or more [`PHAssetCollection`](../phassetcollection.md) objects.
- `title`: A name for the new temporary collection list.

## See Also

### Creating Temporary Collection Lists
- [class func transientCollectionList(with: [PHCollection], title: String?) -> PHCollectionList](./transientcollectionlist%28with,title%29.md)
  Creates a temporary collection list that contains the specified asset collections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollectionlist/transientcollectionlist(withcollectionsfetchresult:title:))*