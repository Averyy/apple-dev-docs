# contains(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns whether the specified object is present in the fetch result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func contains(_ anObject: ObjectType) -> Bool
```

```objc
- (BOOL) containsObject:(ObjectType) anObject;
```

## Return Value

`true` if `anObject` is present in the fetch result, otherwise `false`.

## Discussion

This method determines whether `anObject` is present in the fetch result by sending an `==` message to each of the fetch result’s objects (and passing `anObject` as the parameter to each `==` message).

## Parameters

- `anObject`: An object.

## See Also

### Querying a Fetch Result
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
- [func objects(at: IndexSet) -> [ObjectType]](./objects%28at%29.md)
  Returns an array containing the objects in the fetch result at the indexes in the specified index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/contains(_:))*