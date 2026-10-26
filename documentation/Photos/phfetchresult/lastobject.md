# lastObject

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The last object in the fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var lastObject: ObjectType? { get }
```

```objc
@property (nonatomic, readonly, nullable) ObjectType lastObject;
```

#### Discussion

You specify the ordering of a fetch result in the [`PHFetchOptions`](../phfetchoptions.md) object you pass to a fetch method.

Returns `nil` if the fetch result is empty.

## See Also

### Querying a Fetch Result
- [func contains(ObjectType) -> Bool](./contains%28_%29.md)
  Returns whether the specified object is present in the fetch result.
- [var count: Int](./count.md)
  The number of objects in the fetch result.
- [func countOfAssets(with: PHAssetMediaType) -> Int](./countofassets%28with%29.md)
  Returns the number of assets in the fetch result of a specified type.
- [var firstObject: ObjectType?](./firstobject.md)
  The first object in the fetch result.
- [func object(at: Int) -> ObjectType](./object%28at%29.md)
  Returns the object located at the specified index.
- [subscript(Int) -> ObjectType](./subscript%28_%29.md)
  Returns the object located at the specified index.
- [func objects(at: IndexSet) -> [ObjectType]](./objects%28at%29.md)
  Returns an array containing the objects in the fetch result at the indexes in the specified index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/lastobject)*