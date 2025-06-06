# IOSurfaceGetElementWidthOfPlane(_:_:)

**Framework**: IOSurface  
**Kind**: func

Returns the width (in pixels) of each element in the specified plane.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func IOSurfaceGetElementWidthOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> Int
```

#### Discussion

If the planeIndex is greater than or equal to the plane count of the IOSurface, zero is returned…. with one exception. If this IOSurface has zero planes and a planeIndex of zero is passed in, the routines function just like the non-planar APIs. This is to allow higher level code to treat planar and non-planar buffers is a more uniform fashion.

## See Also

- [func IOSurfaceAlignProperty(CFString, Int) -> Int](iosurfacealignproperty(_:_:).md)
  Returns the smallest aligned value greater than or equal to the specified value.
- [func IOSurfaceAllowsPixelSizeCasting(IOSurfaceRef) -> Bool](iosurfaceallowspixelsizecasting(_:).md)
- [func IOSurfaceCopyAllValues(IOSurfaceRef) -> CFDictionary?](iosurfacecopyallvalues(_:).md)
- [func IOSurfaceCopyValue(IOSurfaceRef, CFString) -> CFTypeRef?](iosurfacecopyvalue(_:_:).md)
  Retrieves a value from the dictionary associated with the buffer.
- [func IOSurfaceCreate(CFDictionary) -> IOSurfaceRef?](iosurfacecreate(_:).md)
  Creates a brand new IOSurface object
- [func IOSurfaceCreateMachPort(IOSurfaceRef) -> mach_port_t](iosurfacecreatemachport(_:).md)
  Returns a mach_port_t that holds a reference to the IOSurface.
- [func IOSurfaceCreateXPCObject(IOSurfaceRef) -> xpc_object_t](iosurfacecreatexpcobject(_:).md)
  Returns an xpc_object_t that holds a reference to the IOSurface.
- [func IOSurfaceDecrementUseCount(IOSurfaceRef)](iosurfacedecrementusecount(_:).md)
  Decrements the per-process usage count for an [`IOSurface`](iosurface.md).
- [func IOSurfaceGetAllocSize(IOSurfaceRef) -> Int](iosurfacegetallocsize(_:).md)
  Returns the total allocation size of the buffer including all planes.
- [func IOSurfaceGetBaseAddress(IOSurfaceRef) -> UnsafeMutableRawPointer](iosurfacegetbaseaddress(_:).md)
  Returns the address of the first byte of data in a particular buffer.
- [func IOSurfaceGetBaseAddressOfPlane(IOSurfaceRef, Int) -> UnsafeMutableRawPointer](iosurfacegetbaseaddressofplane(_:_:).md)
  Returns the address of the first byte of data in the specified plane.
- [func IOSurfaceGetBitDepthOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](iosurfacegetbitdepthofcomponentofplane(_:_:_:).md)
- [func IOSurfaceGetBitOffsetOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](iosurfacegetbitoffsetofcomponentofplane(_:_:_:).md)
- [func IOSurfaceGetBytesPerElement(IOSurfaceRef) -> Int](iosurfacegetbytesperelement(_:).md)
  Returns the length (in bytes) of each element in a particular buffer.
- [func IOSurfaceGetBytesPerElementOfPlane(IOSurfaceRef, Int) -> Int](iosurfacegetbytesperelementofplane(_:_:).md)
  Returns the size of each element (in bytes) in the specified plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfacegetelementwidthofplane(_:_:))*