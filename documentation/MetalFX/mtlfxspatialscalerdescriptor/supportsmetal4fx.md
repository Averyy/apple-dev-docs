# supportsMetal4FX(_:)

**Framework**: MetalFX  
**Kind**: method

Queries whether a Metal device supports spatial scaling compatible with Metal 4.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func supportsMetal4FX(_ device: any MTLDevice) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device supports spatial scaling with Metal 4, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor/supportsmetal4fx(_:))*