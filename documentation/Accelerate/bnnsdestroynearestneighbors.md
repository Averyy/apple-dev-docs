# BNNSDestroyNearestNeighbors(_:)

**Framework**: Accelerate  
**Kind**: func

Destroys a k-nearest neighbors object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func BNNSDestroyNearestNeighbors(_ knn: BNNSNearestNeighbors?)
```

## Parameters

- `knn`: The k-nearest neighbors object.

## See Also

- [struct NearestNeighbors](bnns/nearestneighbors.md)
  A structure that calculates k-nearest neighbors.
- [typealias BNNSNearestNeighbors](bnnsnearestneighbors.md)
  A k-nearest neighbors object.
- [func BNNSCreateNearestNeighbors(UInt32, UInt32, UInt32, BNNSDataType, UnsafePointer<BNNSFilterParameters>?) -> BNNSNearestNeighbors?](bnnscreatenearestneighbors(_:_:_:_:_:).md)
  Returns a new k-nearest neighbors object.
- [func BNNSNearestNeighborsLoad(BNNSNearestNeighbors?, UInt32, UnsafeRawPointer) -> Int32](bnnsnearestneighborsload(_:_:_:).md)
  Adds new sample data to a k-nearest neighbors object.
- [func BNNSNearestNeighborsGetInfo(BNNSNearestNeighbors?, Int32, UnsafeMutablePointer<Int32>?, UnsafeMutableRawPointer?) -> Int32](bnnsnearestneighborsgetinfo(_:_:_:_:).md)
  Calculates the sorted indices and Euclidean distances of the k-nearest neighbors to a specified sample data point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdestroynearestneighbors(_:))*