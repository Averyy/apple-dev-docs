# supportedInputContentMaxScale(device:)

**Framework**: MetalFX  
**Kind**: method

Returns the largest temporal scaling factor the device supports as a floating-point value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class func supportedInputContentMaxScale(device: any MTLDevice) -> Float
```

## Parameters

- `device`: The   instance that represents a GPU.

## See Also

- [class func supportsDevice(any MTLDevice) -> Bool](mtlfxtemporalscalerdescriptor/supportsdevice(_:).md)
  Returns a Boolean value that indicates whether the temporal scaler works with a GPU.
- [class func supportedInputContentMinScale(device: any MTLDevice) -> Float](mtlfxtemporalscalerdescriptor/supportedinputcontentminscale(device:).md)
  Returns the smallest temporal scaling factor the device supports as a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/supportedinputcontentmaxscale(device:))*