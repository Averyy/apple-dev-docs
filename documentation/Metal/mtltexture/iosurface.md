# iosurface

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A reference to the underlying surface instance for the texture, if applicable.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var iosurface: IOSurfaceRef? { get }
```

```objc
@property (readonly, nullable) IOSurfaceRef iosurface;
```

#### Discussion

The property’s value is `nil` for textures that don’t come from an [`IOSurface`](../../IOSurface/iosurface-page.md) instance.

## See Also

### Getting information about the IOSurface the texture was created from
- [var iosurfacePlane: Int](./iosurfaceplane.md)
  The number of a plane within the underlying surface instance for the texture, if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/iosurface)*