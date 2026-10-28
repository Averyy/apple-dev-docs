# IOSurfaceGetBaseAddressOfPlane(_:_:)

**Framework**: IOSurface  
**Kind**: func  
**Role**: Function

Returns the address of the first byte of data in the specified plane.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func IOSurfaceGetBaseAddressOfPlane(_ buffer: IOSurfaceRef, _ planeIndex: Int) -> UnsafeMutableRawPointer
```

```c
void *IOSurfaceGetBaseAddressOfPlane(IOSurfaceRef buffer, size_t planeIndex);
```

## Discussion

If the planeIndex is greater than or equal to the plane count of the IOSurface, zero is returned…. with one exception. If this IOSurface has zero planes and a planeIndex of zero is passed in, the routines function just like the non-planar APIs. This is to allow higher level code to treat planar and non-planar buffers is a more uniform fashion.

## See Also

### Functions
- [func IOSurfaceAlignProperty(CFString, Int) -> Int](./iosurfacealignproperty%28_,_%29.md)
  Returns the smallest aligned value greater than or equal to the specified value.
- [func IOSurfaceAllowsPixelSizeCasting(IOSurfaceRef) -> Bool](./iosurfaceallowspixelsizecasting%28_%29.md)
- [func IOSurfaceCopyAllValues(IOSurfaceRef) -> CFDictionary?](./iosurfacecopyallvalues%28_%29.md)
- [func IOSurfaceCopyValue(IOSurfaceRef, CFString) -> CFTypeRef?](./iosurfacecopyvalue%28_,_%29.md)
  Retrieves a value from the dictionary associated with the buffer.
- [func IOSurfaceCreate(CFDictionary) -> IOSurfaceRef?](./iosurfacecreate%28_%29.md)
  Creates a brand new IOSurface object
- [func IOSurfaceCreateMachPort(IOSurfaceRef) -> mach_port_t](./iosurfacecreatemachport%28_%29.md)
  Returns a mach_port_t that holds a reference to the IOSurface.
- [func IOSurfaceCreateXPCObject(IOSurfaceRef) -> xpc_object_t](./iosurfacecreatexpcobject%28_%29.md)
  Returns an xpc_object_t that holds a reference to the IOSurface.
- [func IOSurfaceDecrementUseCount(IOSurfaceRef)](./iosurfacedecrementusecount%28_%29.md)
  Decrements the per-process usage count for an [`IOSurface`](./iosurface-page.md).
- [func IOSurfaceGetAllocSize(IOSurfaceRef) -> Int](./iosurfacegetallocsize%28_%29.md)
  Returns the total allocation size of the buffer including all planes.
- [func IOSurfaceGetBaseAddress(IOSurfaceRef) -> UnsafeMutableRawPointer](./iosurfacegetbaseaddress%28_%29.md)
  Returns the address of the first byte of data in a particular buffer.
- [func IOSurfaceGetBitDepthOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](./iosurfacegetbitdepthofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetBitOffsetOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](./iosurfacegetbitoffsetofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetBytesPerElement(IOSurfaceRef) -> Int](./iosurfacegetbytesperelement%28_%29.md)
  Returns the length (in bytes) of each element in a particular buffer.
- [func IOSurfaceGetBytesPerElementOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetbytesperelementofplane%28_,_%29.md)
  Returns the size of each element (in bytes) in the specified plane.
- [func IOSurfaceGetBytesPerRow(IOSurfaceRef) -> Int](./iosurfacegetbytesperrow%28_%29.md)
  Returns the length (in bytes) of each row in a particular buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfacegetbaseaddressofplane(_:_:))*