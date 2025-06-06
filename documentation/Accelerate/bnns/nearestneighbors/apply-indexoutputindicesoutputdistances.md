# apply(index:outputIndices:outputDistances:)

**Framework**: Accelerate  
**Kind**: method

Calculates the sorted indices and Euclidean distances of the k-nearest neighbors to a specified sample data point.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
func apply(index: Int?, outputIndices: BNNSNDArrayDescriptor, outputDistances: BNNSNDArrayDescriptor)
```

## Parameters

- `index`: The index of the sample data point of which the function computes the k-nearest neighbors.
- `outputIndices`: The sorted indices of the k-nearest neighbours to the sample data point.
- `outputDistances`: The sorted distances of the k-nearest neighbours to the sample data point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/nearestneighbors/apply(index:outputindices:outputdistances:))*