# supportsDevice(_:)

**Framework**: MetalFX  
**Kind**: method

Queries whether a Metal device supports frame interpolation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
class func supportsDevice(_ device: any MTLDevice) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the device supports frame interpolation, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## Parameters

- `device`: The GPU device for which this methods tests support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxframeinterpolatordescriptor/supportsdevice(_:))*