# supportsDevice(_:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Queries whether a Metal device supports frame interpolation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
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

[`true`](../../Swift/true.md) if the device supports frame interpolation, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/supportsdevice(_:))*