# supportsMetal4FX(_:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Queries whether a Metal device supports denosing scaling compatible on Metal 4.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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

[`true`](../../Swift/true.md) if the device supports denoising scaling for Metal 4, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/supportsmetal4fx(_:))*