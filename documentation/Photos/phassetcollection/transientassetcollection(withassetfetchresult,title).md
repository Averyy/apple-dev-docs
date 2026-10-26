# transientAssetCollection(withAssetFetchResult:title:)

**Framework**: Photos  
**Kind**: method  
**Role**: Type Method

Creates a temporary asset collection containing the assets from the specified fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func transientAssetCollection(withAssetFetchResult fetchResult: PHFetchResult<PHAsset>, title: String?) -> PHAssetCollection
```

```objc
+ (PHAssetCollection *) transientAssetCollectionWithAssetFetchResult:(PHFetchResult<PHAsset *> *) fetchResult title:(NSString *) title;
```

#### Return Value

A new asset collection.

#### Discussion

Transient asset collections are not saved to local storage or iCloud and do not appear in the Photos application or other apps using the Photos framework. A transient collection can be useful if you’ve designed a UI for displaying the contents of a collection and want to display an arbitrary set of assets.

## Parameters

- `fetchResult`: A fetch result containing one or more [`PHAsset`](../phasset.md) objects.
- `title`: A name for the new temporary asset collection.

## See Also

### Creating Temporary Asset Collections
- [class func transientAssetCollection(with: [PHAsset], title: String?) -> PHAssetCollection](./transientassetcollection%28with,title%29.md)
  Creates a temporary asset collection containing the specified assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcollection/transientassetcollection(withassetfetchresult:title:))*