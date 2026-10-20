# supportsDevice(_:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Queries whether a Metal device supports denoising scaling.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
class func supportsDevice(_ device: any MTLDevice) -> Bool
```

```objc
+ (BOOL) supportsDevice:(id<MTLDevice>) device;
```

#### Return Value

[`true`](../../Swift/true.md) if the device supports denoising scaling, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/supportsdevice(_:))*