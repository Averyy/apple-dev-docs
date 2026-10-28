# subscript(_:)

**Framework**: Photos  
**Kind**: subscript  
**Role**: Instance Subscript

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
subscript(idx: Int) -> ObjectType { get }
```

```objc
- (ObjectType) objectAtIndexedSubscript:(NSUInteger) idx;
```

## Return Value

The object located at `index` in the fetch result.

## Discussion

Raises a range exception if `idx` is beyond the end of the fetch result (that is, greater than or equal to the value of the [`count`](./count.md) property).

This method behaves identically to the [`object(at:)`](./object%28at%29.md) method and allows you to access a fetch result using subscript syntax. That is, the two statements below produce the same result.

**Swift**:

```swift
print("First object \(fetchResult[0])")
print("First object \(fetchResult.object(at: 0))")
```

**Objective-C**:

```objc
NSLog(@"First object: %@", [fetchResult objectAtIndex:0]);
NSLog(@"First object: %@", fetchResult[0]);
```

## Parameters

- `idx`: An index within the bounds of the fetch result.

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
- [func objects(at: IndexSet) -> [ObjectType]](./objects%28at%29.md)
  Returns an array containing the objects in the fetch result at the indexes in the specified index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phfetchresult/subscript(_:))*