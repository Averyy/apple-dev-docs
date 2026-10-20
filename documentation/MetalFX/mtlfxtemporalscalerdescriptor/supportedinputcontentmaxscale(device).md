# supportedInputContentMaxScale(device:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Returns the largest temporal scaling factor the device supports as a floating-point value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 27.1+

## Declaration

```swift
class func supportedInputContentMaxScale(device: any MTLDevice) -> Float
```

```objc
+ (float) supportedInputContentMaxScaleForDevice:(id<MTLDevice>) device;
```

## Parameters

- `device`: The [`MTLDevice`](../../Metal/mtldevice.md) instance that represents a GPU.

## See Also

### Checking a GPU device’s scaling support
- [class func supportsDevice(any MTLDevice) -> Bool](./supportsdevice%28_%29.md)
  Returns a Boolean value that indicates whether the temporal scaler works with a GPU.
- [class func supportedInputContentMinScale(device: any MTLDevice) -> Float](./supportedinputcontentminscale%28device%29.md)
  Returns the smallest temporal scaling factor the device supports as a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/supportedinputcontentmaxscale(device:))*