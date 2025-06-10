# copy(destinationBuffer:pixelSize:flags:)

**Framework**: Accelerate  
**Kind**: method

Copies the contents of a vImage buffer to the specified destination buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func copy(destinationBuffer: inout vImage_Buffer, pixelSize: Int, flags options: vImage.Options = .noFlags) throws
```

## Parameters

- `destinationBuffer`: The destination buffer.
- `pixelSize`: The number of bytes for one pixel.
- `options`: The options to use when performing the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_buffer/copy(destinationbuffer:pixelsize:flags:))*