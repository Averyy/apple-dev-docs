# init(device:kernelWidth:kernelHeight:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a spatial normalization kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)
```

#### Return Value

A valid [`MPSCNNSpatialNormalization`](mpscnnspatialnormalization.md) object or `nil`, if failure.

#### Discussion

> **Note**:  The value of `kernelWidth` must be equal to the value of `kernelHeight`.

## Parameters

- `device`: The device the kernel will run on.
- `kernelWidth`: The width of the kernel.
- `kernelHeight`: The height of the kernel.

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnspatialnormalization/init(coder:device:).md)
  Initializes a spatial normalization kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnspatialnormalization/init(device:kernelwidth:kernelheight:))*