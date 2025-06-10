# supportedInputContentMinScale(for:)

**Framework**: MetalFX  
**Kind**: method

Returns the smallest temporal scaling factor the device supports as a floating-point value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+ (Beta)
- tvOS 18.0+

## Declaration

```swift
class func supportedInputContentMinScale(for device: any MTLDevice) -> Float
```

#### Return Value

The minimum input content scale the GPU device supports.

## Parameters

- `device`: The Metal device for which this method checks the minimum input content scale it supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/supportedinputcontentminscale(for:))*