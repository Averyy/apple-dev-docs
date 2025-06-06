# IOSurfaceGetPropertyMaximum(_:)

**Framework**: IOSurface  
**Kind**: func

Returns the maximum value for a given property that is guaranteed to be compatible with all of the current devices (GPUs, etc.) in the system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func IOSurfaceGetPropertyMaximum(_ property: CFString) -> Int
```

#### Discussion

The most important values to obtain are:

- `kIOSurfaceBytesPerRow`
- `kIOSurfaceWidth`
- `kIOSurfaceHeight`
- `kIOSurfacePlaneBytesPerRow`
- `kIOSurfacePlaneWidth`
- `kIOSurfacePlaneHeight`

For the width and height properties, the maximum values are the largest that are guaranteed to work for both reading and writing. In OpenGL terms this translates into the largest size that will work for both textures and render targets.

This function returns 0 for properties that have no predefined limit or where the concept of a limit would be considered invalid (such as `kIOSurfacePixelFormat`).

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

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfacegetpropertymaximum(_:))*