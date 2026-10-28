# supportsMetal4FX(_:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Queries whether a Metal device supports spatial scaling compatible with Metal 4.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 27.1+
- visionOS 26.0+

## Declaration

```swift
class func supportsMetal4FX(_ device: any MTLDevice) -> Bool
```

```objc
+ (BOOL) supportsMetal4FX:(id<MTLDevice>) device;
```

## Return Value

[`true`](../../Swift/true.md) if the device supports spatial scaling with Metal 4, [`false`](../../Swift/false.md) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor/supportsmetal4fx(_:))*