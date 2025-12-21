# kIOSurfacePixelFormat

**Framework**: IOSurface  
**Kind**: var

A 32-bit unsigned integer that stores the traditional macOS buffer format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
let kIOSurfacePixelFormat: CFString
```

#### Discussion

This value is stored as a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber).

#### Discussion

## See Also

- [let kIOSurfaceAllocSize: CFString](kiosurfaceallocsize.md)
  CFNumber of the total allocation size of the buffer including all planes.
- [let kIOSurfaceBytesPerElement: CFString](kiosurfacebytesperelement.md)
  The total number of bytes in an element.
- [let kIOSurfaceBytesPerRow: CFString](kiosurfacebytesperrow.md)
  The bytes per row of the buffer.
- [let kIOSurfaceCacheMode: CFString](kiosurfacecachemode.md)
  The CPU cache mode to be used for the allocation.
- [let kIOSurfaceColorSpace: CFString](kiosurfacecolorspace.md)
- [let kIOSurfaceElementHeight: CFString](kiosurfaceelementheight.md)
  CFNumber for how many pixels high each element is.
- [let kIOSurfaceElementWidth: CFString](kiosurfaceelementwidth.md)
  CFNumber for how many pixels wide each element is.
- [let kIOSurfaceHeight: CFString](kiosurfaceheight.md)
  The height of the IOSurface buffer in pixels.
- [let kIOSurfaceICCProfile: CFString](kiosurfaceiccprofile.md)
- [let kIOSurfaceIsGlobal: CFString](kiosurfaceisglobal.md)
  CFBoolean If true, the IOSurface may be looked up by any task in the system by its ID.
- [let kIOSurfaceName: CFString](kiosurfacename.md)
- [let kIOSurfaceOffset: CFString](kiosurfaceoffset.md)
  The starting offset into the buffer.
- [let kIOSurfacePixelSizeCastingAllowed: CFString](kiosurfacepixelsizecastingallowed.md)
- [let kIOSurfacePlaneBase: CFString](kiosurfaceplanebase.md)
  The base offset into the buffer for this plane.
- [let kIOSurfacePlaneBitsPerElement: CFString](kiosurfaceplanebitsperelement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/kiosurfacepixelformat)*