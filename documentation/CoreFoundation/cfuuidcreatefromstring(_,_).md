# CFUUIDCreateFromString(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a CFUUID object for a specified string.

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
func CFUUIDCreateFromString(_ alloc: CFAllocator!, _ uuidStr: CFString!) -> CFUUID!
```

```c
extern CFUUIDRefCFUUIDCreateFromString(CFAllocatorRef alloc, CFStringRef uuidStr);
```

## Return Value

A new CFUUID object, or if a CFUUID object of the same value already exists, the existing instance with its reference count incremented. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFUUID object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
- `uuidStr`: A string containing a UUID. The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`.

## See Also

### Creating CFUUID Objects
- [func CFUUIDCreate(CFAllocator!) -> CFUUID!](./cfuuidcreate%28_%29.md)
  Creates a Universally Unique Identifier (UUID) object.
- [func CFUUIDCreateFromUUIDBytes(CFAllocator!, CFUUIDBytes) -> CFUUID!](./cfuuidcreatefromuuidbytes%28_,_%29.md)
  Creates a CFUUID object from raw UUID bytes.
- [func CFUUIDCreateWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](./cfuuidcreatewithbytes%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a CFUUID object from raw UUID bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidcreatefromstring(_:_:))*