# DADissenterCreate(_:_:_:)

**Framework**: Disk Arbitration  
**Kind**: func  
**Role**: Function

Creates a new dissenter object.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.4+

## Declaration

```swift
func DADissenterCreate(_ allocator: CFAllocator?, _ status: DAReturn, _ string: CFString?) -> DADissenter
```

```c
extern DADissenterRefDADissenterCreate(CFAllocatorRef allocator, DAReturn status, CFStringRef string);
```

#### Return Value

A reference to a new DADissenter.

## Parameters

- `allocator`: The allocator object to be used to allocate memory.
- `status`: The return code.
- `string`: The return code string. Pass NULL for no reason.

## See Also

### Miscellaneous
- [func DADissenterGetStatus(DADissenter) -> DAReturn](./dadissentergetstatus%28_%29.md)
  Obtains the return code.
- [func DADissenterGetStatusString(DADissenter) -> CFString?](./dadissentergetstatusstring%28_%29.md)
  Obtains the return code string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskarbitration/dadissentercreate(_:_:_:))*