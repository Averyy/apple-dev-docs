# init(device:kernelWidth:kernelHeight:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes the kernel with a specified width and height.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)
```

#### Return Value

Returns an initialized kernel object with a specific width and height.

## Parameters

- `device`: The Metal device the filter will run on.
- `kernelWidth`: The width of the kernel. Must be an odd number.
- `kernelHeight`: The height of the kernel. Must be an odd number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamax/init(device:kernelwidth:kernelheight:))*