# supportsMetal4FX(_:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Queries whether a Metal device supports frame interpolation compatible with a Metal 4 command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+

## Declaration

```swift
class func supportsMetal4FX(_ device: any MTLDevice) -> Bool
```

```objc
+ (BOOL) supportsMetal4FX:(id<MTLDevice>) device;
```

## Return Value

[`true`](../../Swift/true.md) if the device supports frame interpolation for Metal 4, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/supportsmetal4fx(_:))*