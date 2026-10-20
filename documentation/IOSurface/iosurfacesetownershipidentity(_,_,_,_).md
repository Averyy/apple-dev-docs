# IOSurfaceSetOwnershipIdentity(_:_:_:_:)

**Framework**: IOSurface  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func IOSurfaceSetOwnershipIdentity(_ buffer: IOSurfaceRef, _ task_id_token: task_id_token_t, _ newLedgerTag: Int32, _ newLedgerOptions: UInt32) -> kern_return_t
```

```c
kern_return_t IOSurfaceSetOwnershipIdentity(IOSurfaceRef buffer, task_id_token_t task_id_token, int newLedgerTag, uint32_t newLedgerOptions);
```

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
- [func IOSurfaceGetBaseAddressOfPlane(IOSurfaceRef, Int) -> UnsafeMutableRawPointer](./iosurfacegetbaseaddressofplane%28_,_%29.md)
  Returns the address of the first byte of data in the specified plane.
- [func IOSurfaceGetBitDepthOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](./iosurfacegetbitdepthofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetBitOffsetOfComponentOfPlane(IOSurfaceRef, Int, Int) -> Int](./iosurfacegetbitoffsetofcomponentofplane%28_,_,_%29.md)
- [func IOSurfaceGetBytesPerElement(IOSurfaceRef) -> Int](./iosurfacegetbytesperelement%28_%29.md)
  Returns the length (in bytes) of each element in a particular buffer.
- [func IOSurfaceGetBytesPerElementOfPlane(IOSurfaceRef, Int) -> Int](./iosurfacegetbytesperelementofplane%28_,_%29.md)
  Returns the size of each element (in bytes) in the specified plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfacesetownershipidentity(_:_:_:_:))*