# supportsDevice(_:)

**Framework**: MetalFX  
**Kind**: method

Returns a Boolean value that indicates whether the temporal scaler works with a GPU.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+

## Declaration

```swift
class func supportsDevice(_ device: any MTLDevice) -> Bool
```

## Parameters

- `device`: An   instance that represents a GPU.

## See Also

- [class func supportedInputContentMinScale(device: any MTLDevice) -> Float](mtlfxtemporalscalerdescriptor/supportedinputcontentminscale(device:).md)
  Returns the smallest temporal scaling factor the device supports as a floating-point value.
- [class func supportedInputContentMaxScale(device: any MTLDevice) -> Float](mtlfxtemporalscalerdescriptor/supportedinputcontentmaxscale(device:).md)
  Returns the largest temporal scaling factor the device supports as a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/supportsdevice(_:))*