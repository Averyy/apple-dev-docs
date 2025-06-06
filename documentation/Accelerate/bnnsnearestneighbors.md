# BNNSNearestNeighbors

**Framework**: Accelerate  
**Kind**: typealias

A k-nearest neighbors object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias BNNSNearestNeighbors = UnsafeMutableRawPointer
```

## See Also

- [struct NearestNeighbors](bnns/nearestneighbors.md)
  A structure that calculates k-nearest neighbors.
- [func BNNSCreateNearestNeighbors(UInt32, UInt32, UInt32, BNNSDataType, UnsafePointer<BNNSFilterParameters>?) -> BNNSNearestNeighbors?](bnnscreatenearestneighbors(_:_:_:_:_:).md)
  Returns a new k-nearest neighbors object.
- [func BNNSNearestNeighborsLoad(BNNSNearestNeighbors?, UInt32, UnsafeRawPointer) -> Int32](bnnsnearestneighborsload(_:_:_:).md)
  Adds new sample data to a k-nearest neighbors object.
- [func BNNSNearestNeighborsGetInfo(BNNSNearestNeighbors?, Int32, UnsafeMutablePointer<Int32>?, UnsafeMutableRawPointer?) -> Int32](bnnsnearestneighborsgetinfo(_:_:_:_:).md)
  Calculates the sorted indices and Euclidean distances of the k-nearest neighbors to a specified sample data point.
- [func BNNSDestroyNearestNeighbors(BNNSNearestNeighbors?)](bnnsdestroynearestneighbors(_:).md)
  Destroys a k-nearest neighbors object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsnearestneighbors)*