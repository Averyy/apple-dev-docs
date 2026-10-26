# IOSurface Functions

**Framework**: IOSurface  
**Role**: API Collection

## Topics

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
- [func IOSurfaceGetBytesPerRowOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetbytesperrowofplane%28_,_%29.md)
  Returns the size of each row (in bytes) in the specified plane.
- [func IOSurfaceGetElementHeight(IOSurfaceRef) -> Int](./iosurfacegetelementheight%28_%29.md)
  Returns the height (in pixels) of each element in a particular buffer.
- [func IOSurfaceGetElementHeightOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetelementheightofplane%28_,_%29.md)
  Returns the height (in pixels) of each element in the specified plane.
- [func IOSurfaceGetElementWidth(IOSurfaceRef) -> Int](./iosurfacegetelementwidth%28_%29.md)
  Returns the width (in pixels) of each element in a particular buffer.
- [func IOSurfaceGetElementWidthOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetelementwidthofplane%28_,_%29.md)
  Returns the width (in pixels) of each element in the specified plane.
- [func IOSurfaceGetHeight(IOSurfaceRef) -> Int](./iosurfacegetheight%28_%29.md)
  Returns the height of the IOSurface buffer in pixels.
- [func IOSurfaceGetHeightOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetheightofplane%28_,_%29.md)
  Returns the height of the specified plane (in pixels).
- [func IOSurfaceGetID(IOSurfaceRef) -> IOSurfaceID](./iosurfacegetid%28_%29.md)
  Retrieves the unique [`IOSurfaceID`](./iosurfaceid.md) value for an [`IOSurface`](./iosurface-page.md).
- [func IOSurfaceGetNameOfComponentOfPlane(IOSurfaceRef, Int, Int) -> IOSurfaceComponentName](./iosurfacegetnameofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetNumberOfComponentsOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetnumberofcomponentsofplane%28_,_%29.md)
- [func IOSurfaceGetPixelFormat(IOSurfaceRef) -> OSType](./iosurfacegetpixelformat%28_%29.md)
  Returns an unsigned integer that contains the traditional macOS buffer format.
- [func IOSurfaceGetPlaneCount(IOSurfaceRef) -> Int](./iosurfacegetplanecount%28_%29.md)
- [func IOSurfaceGetPropertyAlignment(CFString) -> Int](./iosurfacegetpropertyalignment%28_%29.md)
  Returns the alignment requirements for a property (if any).
- [func IOSurfaceGetPropertyMaximum(CFString) -> Int](./iosurfacegetpropertymaximum%28_%29.md)
  Returns the maximum value for a given property that is guaranteed to be compatible with all of the current devices (GPUs, etc.) in the system.
- [func IOSurfaceGetRangeOfComponentOfPlane(IOSurfaceRef, Int, Int) -> IOSurfaceComponentRange](./iosurfacegetrangeofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetSeed(IOSurfaceRef) -> UInt32](./iosurfacegetseed%28_%29.md)
- [func IOSurfaceGetSubsampling(IOSurfaceRef) -> IOSurfaceSubsampling](./iosurfacegetsubsampling%28_%29.md)
- [func IOSurfaceGetTypeID() -> CFTypeID](./iosurfacegettypeid%28%29.md)
- [func IOSurfaceGetTypeOfComponentOfPlane(IOSurfaceRef, Int, Int) -> IOSurfaceComponentType](./iosurfacegettypeofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetUseCount(IOSurfaceRef) -> Int32](./iosurfacegetusecount%28_%29.md)
  Returns the per-process usage count for an [`IOSurface`](./iosurface-page.md).
- [func IOSurfaceGetWidth(IOSurfaceRef) -> Int](./iosurfacegetwidth%28_%29.md)
  Returns the width of the IOSurface buffer in pixels.
- [func IOSurfaceGetWidthOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetwidthofplane%28_,_%29.md)
  Returns the width of the specified plane (in pixels).
- [func IOSurfaceIncrementUseCount(IOSurfaceRef)](./iosurfaceincrementusecount%28_%29.md)
  Increments the per-process usage count for an [`IOSurface`](./iosurface-page.md).
- [func IOSurfaceIsInUse(IOSurfaceRef) -> Bool](./iosurfaceisinuse%28_%29.md)
  Returns true of an IOSurface is in use by any process in the system, otherwise false.
- [func IOSurfaceLock(IOSurfaceRef, IOSurfaceLockOptions, UnsafeMutablePointer<UInt32>?) -> kern_return_t](./iosurfacelock%28_,_,_%29.md)
  “Lock” an IOSurface for reading or writing.
- [func IOSurfaceLookup(IOSurfaceID) -> IOSurfaceRef?](./iosurfacelookup%28_%29.md)
  Performs an atomic lookup and retain of an IOSurface by its IOSurfaceID.
- [func IOSurfaceLookupFromMachPort(mach_port_t) -> IOSurfaceRef?](./iosurfacelookupfrommachport%28_%29.md)
  Recreates an IOSurfaceRef from a mach port.
- [func IOSurfaceLookupFromXPCObject(xpc_object_t) -> IOSurfaceRef?](./iosurfacelookupfromxpcobject%28_%29.md)
- [func IOSurfaceRemoveAllValues(IOSurfaceRef)](./iosurfaceremoveallvalues%28_%29.md)
- [func IOSurfaceRemoveValue(IOSurfaceRef, CFString)](./iosurfaceremovevalue%28_,_%29.md)
  Deletes a value in the dictionary associated with the buffer.
- [func IOSurfaceSetOwnershipIdentity(IOSurfaceRef, task_id_token_t, Int32, UInt32) -> kern_return_t](./iosurfacesetownershipidentity%28_,_,_,_%29.md)
- [func IOSurfaceSetPurgeable(IOSurfaceRef, UInt32, UnsafeMutablePointer<UInt32>?) -> kern_return_t](./iosurfacesetpurgeable%28_,_,_%29.md)
- [func IOSurfaceSetValue(IOSurfaceRef, CFString, CFTypeRef)](./iosurfacesetvalue%28_,_,_%29.md)
  Sets a value in the dictionary associated with the buffer.
- [func IOSurfaceSetValues(IOSurfaceRef, CFDictionary)](./iosurfacesetvalues%28_,_%29.md)
- [func IOSurfaceUnlock(IOSurfaceRef, IOSurfaceLockOptions, UnsafeMutablePointer<UInt32>?) -> kern_return_t](./iosurfaceunlock%28_,_,_%29.md)
  “Unlock” an [`IOSurface`](./iosurface-page.md) for reading or writing.

## See Also

### Reference
- [IOSurface Structures](./iosurface-structures.md)
- [IOSurface Constants](./iosurface-constants.md)
- [IOSurface Enumerations](./iosurface-enumerations.md)
- [IOSurface Data Types](./iosurface-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurface-functions)*