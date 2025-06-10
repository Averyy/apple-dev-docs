# makeArray(of:batchSize:)

**Framework**: Accelerate  
**Kind**: method

Returns a new array that contains a copy of the n-dimensional array descriptor’s data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func makeArray<T>(of scalarType: T.Type, batchSize: Int = 1) -> [T]?
```

## Parameters

- `scalarType`: The data type of the data.
- `batchSize`: The number of batches of data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/makearray(of:batchsize:))*