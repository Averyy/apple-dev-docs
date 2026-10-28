# object(at:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns the object located at the specified index.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func object(at index: Int) -> ObjectType
```

```objc
- (ObjectType) objectAtIndex:(NSUInteger) index;
```

## Return Value

The object located at `index` in the fetch result.

## Discussion

Raises a range exception if `index` is beyond the end of the fetch result (that is, greater than or equal to the value of the [`count`](./count.md) property).

## Parameters

- `index`: An index within the bounds of the fetch result.

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
- [var lastObject: ObjectType?](./lastobject.md)
  The last object in the fetch result.
- [subscript(Int) -> ObjectType](./subscript%28_%29.md)
  Returns the object located at the specified index.
- [func objects(at: IndexSet) -> [ObjectType]](./objects%28at%29.md)
  Returns an array containing the objects in the fetch result at the indexes in the specified index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/object(at:))*