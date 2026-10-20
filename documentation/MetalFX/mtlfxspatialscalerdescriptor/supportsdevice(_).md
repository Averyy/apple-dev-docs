# supportsDevice(_:)

**Framework**: MetalFX  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the spatial scaler works with a GPU.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 27.1+
- visionOS 1.0+

## Declaration

```swift
class func supportsDevice(_ device: any MTLDevice) -> Bool
```

```objc
+ (BOOL) supportsDevice:(id<MTLDevice>) device;
```

## Parameters

- `device`: An [`MTLDevice`](../../Metal/mtldevice.md) instance that represents a GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalfx/mtlfxspatialscalerdescriptor/supportsdevice(_:))*