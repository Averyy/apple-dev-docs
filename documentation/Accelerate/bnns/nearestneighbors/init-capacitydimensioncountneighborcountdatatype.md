# init(capacity:dimensionCount:neighborCount:dataType:)

**Framework**: Accelerate  
**Kind**: init

Returns a new k-nearest neighbors object.

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
init(capacity: Int, dimensionCount: Int, neighborCount: Int, dataType: BNNSDataType)
```

## Parameters

- `capacity`: The maximum number of data points.
- `dimensionCount`: The number of features or dimensions of each data point.
- `neighborCount`: The number of nearest neighbors that a subsequent call to   calculates.
- `dataType`: The data type of the data points. This must be either   or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/nearestneighbors/init(capacity:dimensioncount:neighborcount:datatype:))*