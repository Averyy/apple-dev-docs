# init(_:shape:dataType:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes an tensor data with a metal buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(_ buffer: any MTLBuffer, shape: [NSNumber], dataType: MPSDataType)
```

#### Return Value

A valid MPSGraphTensorData, or nil if allocation failure.

#### Discussion

The device of the MTLBuffer will be used to get the MPSDevice for this MPSGraphTensorData.

## Parameters

- `buffer`: MTLBuffer to be used within the MPSGraphTensorData
- `shape`: Shape of the output tensor
- `dataType`: dataType of the placeholder tensor


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(_:shape:datatype:))*