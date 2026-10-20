# CFUUIDCreateString(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the string representation of a specified CFUUID object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFUUIDCreateString(_ alloc: CFAllocator!, _ uuid: CFUUID!) -> CFString!
```

```c
extern CFStringRefCFUUIDCreateString(CFAllocatorRef alloc, CFUUIDRef uuid);
```

#### Return Value

The string representation of `uuid`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new string. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `uuid`: The CFUUID object whose string representation to obtain.

## See Also

### Getting Information About CFUUID Objects
- [func CFUUIDGetConstantUUIDWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](./cfuuidgetconstantuuidwithbytes%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Returns a CFUUID object from raw UUID bytes.
- [func CFUUIDGetUUIDBytes(CFUUID!) -> CFUUIDBytes](./cfuuidgetuuidbytes%28_%29.md)
  Returns the value of a UUID object as raw bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidcreatestring(_:_:))*