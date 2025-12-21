# supportsDevice(_:)

**Framework**: MetalFX  
**Kind**: method

Queries whether a Metal device supports denoising scaling.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- tvOS 18.0+

## Declaration

```swift
class func supportsDevice(_ device: any MTLDevice) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the device supports denoising scaling, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxtemporaldenoisedscalerdescriptor/supportsdevice(_:))*