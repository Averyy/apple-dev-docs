# objects(at:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns an array containing the objects in the fetch result at the indexes in the specified index set.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func objects(at indexes: IndexSet) -> [ObjectType]
```

```objc
- (NSArray<id> *) objectsAtIndexes:(NSIndexSet *) indexes;
```

## Return Value

An array containing the objects in the fetch result at the indexes specified by `indexes`.

## Discussion

The ordering of the returned array follows the index set. That is, in the returned array, an object with a higher index in the index set comes after any object with a smaller index in the index set.

Raises a range exception if any index in the index set is beyond the end of the fetch result (that is, greater than or equal to the value of the [`count`](./count.md) property).

## Parameters

- `indexes`: An index set containing indexes within the bounds of the fetch result.

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
- [func object(at: Int) -> ObjectType](./object%28at%29.md)
  Returns the object located at the specified index.
- [subscript(Int) -> ObjectType](./subscript%28_%29.md)
  Returns the object located at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/objects(at:))*