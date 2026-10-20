# IOSurfaceCreateMachPort(_:)

**Framework**: IOSurface  
**Kind**: func  
**Role**: Function

Returns a mach_port_t that holds a reference to the IOSurface.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func IOSurfaceCreateMachPort(_ buffer: IOSurfaceRef) -> mach_port_t
```

```c
mach_port_t IOSurfaceCreateMachPort(IOSurfaceRef buffer);
```

#### Discussion

This is useful if you need to atomically or securely pass an IOSurface to another task without making the surface global to the entire system. The returned port must be deallocated with mach_port_deallocate or the equivalent.

> **Note**:  Any live mach ports created from an IOSurfaceRef implicitly increase the IOSurface’s global use count by one until the port is deleted.

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
- [func IOSurfaceCreateXPCObject(IOSurfaceRef) -> xpc_object_t](./iosurfacecreatexpcobject%28_%29.md)
  Returns an xpc_object_t that holds a reference to the IOSurface.
- [func IOSurfaceDecrementUseCount(IOSurfaceRef)](./iosurfacedecrementusecount%28_%29.md)
  Decrements the per-process usage count for an [`IOSurface`](./iosurface-page.md).
- [func IOSurfaceGetAllocSize(IOSurfaceRef) -> Int](./iosurfacegetallocsize%28_%29.md)
  Returns the total allocation size of the buffer including all planes.
- [func IOSurfaceGetBaseAddress(IOSurfaceRef) -> UnsafeMutableRawPointer](./iosurfacegetbaseaddress%28_%29.md)
  Returns the address of the first byte of data in a particular buffer.
- [func IOSurfaceGetBaseAddressOfPlane(IOSurfaceRef, Int) -> UnsafeMutableRawPointer](./iosurfacegetbaseaddressofplane%28_,_%29.md)
  Returns the address of the first byte of data in the specified plane.
- [func IOSurfaceGetBitDepthOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](./iosurfacegetbitdepthofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetBitOffsetOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](./iosurfacegetbitoffsetofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetBytesPerElement(IOSurfaceRef) -> Int](./iosurfacegetbytesperelement%28_%29.md)
  Returns the length (in bytes) of each element in a particular buffer.
- [func IOSurfaceGetBytesPerElementOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetbytesperelementofplane%28_,_%29.md)
  Returns the size of each element (in bytes) in the specified plane.
- [func IOSurfaceGetBytesPerRow(IOSurfaceRef) -> Int](./iosurfacegetbytesperrow%28_%29.md)
  Returns the length (in bytes) of each row in a particular buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfacecreatemachport(_:))*