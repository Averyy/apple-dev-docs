# IOSurfaceUnlock(_:_:_:)

**Framework**: IOSurface  
**Kind**: func

“Unlock” an [`IOSurface`](iosurface.md) for reading or writing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func IOSurfaceUnlock(_ buffer: IOSurfaceRef, _ options: IOSurfaceLockOptions, _ seed: UnsafeMutablePointer<UInt32>?) -> kern_return_t
```

#### Discussion

The term “lock” is used loosely in this context, and is used along with the “unlock” information to put a bound on CPU access to the raw [`IOSurface`](iosurface.md) data.

If the seed parameter is non-NULL, [`IOSurfaceLock(_:_:_:)`](iosurfacelock(_:_:_:).md) will store the buffer’s internal modification seed value at the time you made the lock call. You can compare this value to a value returned previously to determine of the contents of the buffer has been changed since the last lock.

In the case of [`IOSurfaceUnlock(_:_:_:)`](iosurfaceunlock(_:_:_:).md), the seed value returned will be the internal seed value at the time of the unlock. If you locked the buffer for writing, this value will be incremented as the unlock is performed and the new value will be returned.

See the kIOSurfaceLock enums for more information.

> **Note**:  Locking and unlocking an [`IOSurface`](iosurface.md) is not a particularly cheap operation, so care should be taken to avoid the calls whenever possible. The seed values are particularly useful for keeping a cache of the buffer contents.

 Locking and unlocking an [`IOSurface`](iosurface.md) is not a particularly cheap operation, so care should be taken to avoid the calls whenever possible. The seed values are particularly useful for keeping a cache of the buffer contents.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfaceunlock(_:_:_:))*