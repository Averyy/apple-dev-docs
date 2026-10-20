# supportsDevice(_:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the temporal scaler works with a GPU.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+

## Declaration

```swift
class func supportsDevice(_ device: any MTLDevice) -> Bool
```

```objc
+ (BOOL) supportsDevice:(id<MTLDevice>) device;
```

## Parameters

- `device`: An [`MTLDevice`](../../Metal/mtldevice.md) instance that represents a GPU.

## See Also

### Checking a GPU device’s scaling support
- [class func supportedInputContentMinScale(device: any MTLDevice) -> Float](./supportedinputcontentminscale%28device%29.md)
  Returns the smallest temporal scaling factor the device supports as a floating-point value.
- [class func supportedInputContentMaxScale(device: any MTLDevice) -> Float](./supportedinputcontentmaxscale%28device%29.md)
  Returns the largest temporal scaling factor the device supports as a floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporalscalerdescriptor/supportsdevice(_:))*