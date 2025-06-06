# init(_:shape:dataType:rowBytes:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes an tensor data with a metal buffer.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
init(_ buffer: any MTLBuffer, shape: [NSNumber], dataType: MPSDataType, rowBytes: Int)
```

#### Return Value

A valid MPSGraphTensorData, or nil if allocation failure.

#### Discussion

The device of the MTLBuffer will be used to get the MPSDevice for this MPSGraphTensorData.

## Parameters

- `buffer`: MTLBuffer to be used within the MPSGraphTensorData
- `shape`: Shape of the output tensor
- `dataType`: dataType of the placeholder tensor
- `rowBytes`: rowBytes for the fastest moving dimension, must be larger than or equal to sizeOf(dataType)shape[rank - 1] and must be a multiple of sizeOf(dataType)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(_:shape:datatype:rowbytes:))*