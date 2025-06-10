# supportedInputContentMaxScale(for:)

**Framework**: MetalFX  
**Kind**: method

Returns the largest temporal scaling factor the device supports as a floating-point value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- tvOS 18.0+

## Declaration

```swift
class func supportedInputContentMaxScale(for device: any MTLDevice) -> Float
```

#### Return Value

The maximum input content scale the GPU device supports.

## Parameters

- `device`: The Metal device for which this method checks the maximum input content scale it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/supportedinputcontentmaxscale(for:))*