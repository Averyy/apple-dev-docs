# init(_:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Initializes a tensor data with an MPS image batch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(_ imageBatch: [MPSImage])
```

#### Return Value

A valid MPSGraphTensorData, or nil if allocation failure.

#### Discussion

The dataLayout used will be NHWC, call a transpose or permute to change to a layout of your choice.

## Parameters

- `imageBatch`: The device on which the kernel will run, unorm8 and unorm16 images will create a float32 tensorData


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensordata/init(_:)-511a)*