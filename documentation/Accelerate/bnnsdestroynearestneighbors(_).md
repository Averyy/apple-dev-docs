# BNNSDestroyNearestNeighbors(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
void BNNSDestroyNearestNeighbors(BNNSNearestNeighbors knn);
```

## Parameters

- `knn`: The k-nearest neighbors object.

## See Also

### K-nearest neighbors calculation
- [struct NearestNeighbors](./bnns/nearestneighbors.md)
  A structure that calculates k-nearest neighbors.
- [typealias BNNSNearestNeighbors](./bnnsnearestneighbors.md)
  A k-nearest neighbors object.
- [func BNNSCreateNearestNeighbors(UInt32, UInt32, UInt32, BNNSDataType, UnsafePointer<BNNSFilterParameters>?) -> BNNSNearestNeighbors?](./bnnscreatenearestneighbors%28_,_,_,_,_%29.md)
  Returns a new k-nearest neighbors object.
- [func BNNSNearestNeighborsLoad(BNNSNearestNeighbors?, UInt32, UnsafeRawPointer) -> Int32](./bnnsnearestneighborsload%28_,_,_%29.md)
  Adds new sample data to a k-nearest neighbors object.
- [func BNNSNearestNeighborsGetInfo(BNNSNearestNeighbors?, Int32, UnsafeMutablePointer<Int32>?, UnsafeMutableRawPointer?) -> Int32](./bnnsnearestneighborsgetinfo%28_,_,_,_%29.md)
  Calculates the sorted indices and Euclidean distances of the k-nearest neighbors to a specified sample data point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdestroynearestneighbors(_:))*