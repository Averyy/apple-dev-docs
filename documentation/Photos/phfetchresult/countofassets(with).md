# countOfAssets(with:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns the number of assets in the fetch result of a specified type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func countOfAssets(with mediaType: PHAssetMediaType) -> Int
```

```objc
- (NSUInteger) countOfAssetsWithMediaType:(PHAssetMediaType) mediaType;
```

#### Return Value

The number of assets in the fetch result of the specified type.

#### Discussion

The first time you call this method, Photos enumerates the contents of the fetch result to count those of the specified type, then caches the result. Subsequent calls with the same `mediaType` parameter return the cached value.

This method counts only the [`PHAsset`](../phasset.md) objects in a fetch result. If a fetch result contains only [`PHAssetCollection`](../phassetcollection.md) or [`PHCollectionList`](../phcollectionlist.md) objects, the return value is `0`.

## Parameters

- `mediaType`: The type of assets to count, such as image or video. See [`PHAssetMediaType`](../phassetmediatype.md).

## See Also

### Querying a Fetch Result
- [func contains(ObjectType) -> Bool](./contains%28_%29.md)
  Returns whether the specified object is present in the fetch result.
- [var count: Int](./count.md)
  The number of objects in the fetch result.
- [var firstObject: ObjectType?](./firstobject.md)
  The first object in the fetch result.
- [var lastObject: ObjectType?](./lastobject.md)
  The last object in the fetch result.
- [func object(at: Int) -> ObjectType](./object%28at%29.md)
  Returns the object located at the specified index.
- [subscript(Int) -> ObjectType](./subscript%28_%29.md)
  Returns the object located at the specified index.
- [func objects(at: IndexSet) -> [ObjectType]](./objects%28at%29.md)
  Returns an array containing the objects in the fetch result at the indexes in the specified index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/countofassets(with:))*