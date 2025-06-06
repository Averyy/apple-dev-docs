# IOSurface Functions

**Framework**: IOSurface

## Topics

### Functions
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
- [func IOSurfaceGetBytesPerRow(IOSurfaceRef) -> Int](iosurfacegetbytesperrow(_:).md)
  Returns the length (in bytes) of each row in a particular buffer.
- [func IOSurfaceGetBytesPerRowOfPlane(IOSurfaceRef, Int) -> Int](iosurfacegetbytesperrowofplane(_:_:).md)
  Returns the size of each row (in bytes) in the specified plane.
- [func IOSurfaceGetElementHeight(IOSurfaceRef) -> Int](iosurfacegetelementheight(_:).md)
  Returns the height (in pixels) of each element in a particular buffer.
- [func IOSurfaceGetElementHeightOfPlane(IOSurfaceRef, Int) -> Int](iosurfacegetelementheightofplane(_:_:).md)
  Returns the height (in pixels) of each element in the specified plane.
- [func IOSurfaceGetElementWidth(IOSurfaceRef) -> Int](iosurfacegetelementwidth(_:).md)
  Returns the width (in pixels) of each element in a particular buffer.
- [func IOSurfaceGetElementWidthOfPlane(IOSurfaceRef, Int) -> Int](iosurfacegetelementwidthofplane(_:_:).md)
  Returns the width (in pixels) of each element in the specified plane.
- [func IOSurfaceGetHeight(IOSurfaceRef) -> Int](iosurfacegetheight(_:).md)
  Returns the height of the IOSurface buffer in pixels.
- [func IOSurfaceGetHeightOfPlane(IOSurfaceRef, Int) -> Int](iosurfacegetheightofplane(_:_:).md)
  Returns the height of the specified plane (in pixels).
- [func IOSurfaceGetID(IOSurfaceRef) -> IOSurfaceID](iosurfacegetid(_:).md)
  Retrieves the unique [`IOSurfaceID`](iosurfaceid.md) value for an [`IOSurface`](iosurface.md).
- [func IOSurfaceGetNameOfComponentOfPlane(IOSurfaceRef, Int, Int) -> IOSurfaceComponentName](iosurfacegetnameofcomponentofplane(_:_:_:).md)
- [func IOSurfaceGetNumberOfComponentsOfPlane(IOSurfaceRef, Int) -> Int](iosurfacegetnumberofcomponentsofplane(_:_:).md)
- [func IOSurfaceGetPixelFormat(IOSurfaceRef) -> OSType](iosurfacegetpixelformat(_:).md)
  Returns an unsigned integer that contains the traditional macOS buffer format.
- [func IOSurfaceGetPlaneCount(IOSurfaceRef) -> Int](iosurfacegetplanecount(_:).md)
- [func IOSurfaceGetPropertyAlignment(CFString) -> Int](iosurfacegetpropertyalignment(_:).md)
  Returns the alignment requirements for a property (if any).
- [func IOSurfaceGetPropertyMaximum(CFString) -> Int](iosurfacegetpropertymaximum(_:).md)
  Returns the maximum value for a given property that is guaranteed to be compatible with all of the current devices (GPUs, etc.) in the system.
- [func IOSurfaceGetRangeOfComponentOfPlane(IOSurfaceRef, Int, Int) -> IOSurfaceComponentRange](iosurfacegetrangeofcomponentofplane(_:_:_:).md)
- [func IOSurfaceGetSeed(IOSurfaceRef) -> UInt32](iosurfacegetseed(_:).md)
- [func IOSurfaceGetSubsampling(IOSurfaceRef) -> IOSurfaceSubsampling](iosurfacegetsubsampling(_:).md)
- [func IOSurfaceGetTypeID() -> CFTypeID](iosurfacegettypeid().md)
- [func IOSurfaceGetTypeOfComponentOfPlane(IOSurfaceRef, Int, Int) -> IOSurfaceComponentType](iosurfacegettypeofcomponentofplane(_:_:_:).md)
- [func IOSurfaceGetUseCount(IOSurfaceRef) -> Int32](iosurfacegetusecount(_:).md)
  Returns the per-process usage count for an [`IOSurface`](iosurface.md).
- [func IOSurfaceGetWidth(IOSurfaceRef) -> Int](iosurfacegetwidth(_:).md)
  Returns the width of the IOSurface buffer in pixels.
- [func IOSurfaceGetWidthOfPlane(IOSurfaceRef, Int) -> Int](iosurfacegetwidthofplane(_:_:).md)
  Returns the width of the specified plane (in pixels).
- [func IOSurfaceIncrementUseCount(IOSurfaceRef)](iosurfaceincrementusecount(_:).md)
  Increments the per-process usage count for an [`IOSurface`](iosurface.md).
- [func IOSurfaceIsInUse(IOSurfaceRef) -> Bool](iosurfaceisinuse(_:).md)
  Returns true of an IOSurface is in use by any process in the system, otherwise false.
- [func IOSurfaceLock(IOSurfaceRef, IOSurfaceLockOptions, UnsafeMutablePointer<UInt32>?) -> kern_return_t](iosurfacelock(_:_:_:).md)
  “Lock” an IOSurface for reading or writing.
- [func IOSurfaceLookup(IOSurfaceID) -> IOSurfaceRef?](iosurfacelookup(_:).md)
  Performs an atomic lookup and retain of an IOSurface by its IOSurfaceID.
- [func IOSurfaceLookupFromMachPort(mach_port_t) -> IOSurfaceRef?](iosurfacelookupfrommachport(_:).md)
  Recreates an IOSurfaceRef from a mach port.
- [func IOSurfaceLookupFromXPCObject(xpc_object_t) -> IOSurfaceRef?](iosurfacelookupfromxpcobject(_:).md)
- [func IOSurfaceRemoveAllValues(IOSurfaceRef)](iosurfaceremoveallvalues(_:).md)
- [func IOSurfaceRemoveValue(IOSurfaceRef, CFString)](iosurfaceremovevalue(_:_:).md)
  Deletes a value in the dictionary associated with the buffer.
- [func IOSurfaceSetOwnershipIdentity(IOSurfaceRef, task_id_token_t, Int32, UInt32) -> kern_return_t](iosurfacesetownershipidentity(_:_:_:_:).md)
- [func IOSurfaceSetPurgeable(IOSurfaceRef, UInt32, UnsafeMutablePointer<UInt32>?) -> kern_return_t](iosurfacesetpurgeable(_:_:_:).md)
- [func IOSurfaceSetValue(IOSurfaceRef, CFString, CFTypeRef)](iosurfacesetvalue(_:_:_:).md)
  Sets a value in the dictionary associated with the buffer.
- [func IOSurfaceSetValues(IOSurfaceRef, CFDictionary)](iosurfacesetvalues(_:_:).md)
- [func IOSurfaceUnlock(IOSurfaceRef, IOSurfaceLockOptions, UnsafeMutablePointer<UInt32>?) -> kern_return_t](iosurfaceunlock(_:_:_:).md)
  “Unlock” an [`IOSurface`](iosurface.md) for reading or writing.

## See Also

- [IOSurface Structures](iosurface-structures.md)
- [IOSurface Constants](iosurface-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurface-functions)*