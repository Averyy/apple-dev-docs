# init(device:data:shape:dataType:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes the tensor data with an `NSData` on a device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(device: MPSGraphDevice, data: Data, shape: [NSNumber], dataType: MPSDataType)
```

#### Return Value

A valid MPSGraphTensorData, or nil if allocation failure.

## Parameters

- `device`: MPSDevice on which the MPSGraphTensorData exists
- `data`: NSData from which to copy the contents
- `shape`: Shape of the output tensor
- `dataType`: dataType of the placeholder tensor


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(device:data:shape:datatype:))*