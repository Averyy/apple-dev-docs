# CFUUIDCreate(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a Universally Unique Identifier (UUID) object.

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
func CFUUIDCreate(_ alloc: CFAllocator!) -> CFUUID!
```

```c
extern CFUUIDRefCFUUIDCreate(CFAllocatorRef alloc);
```

#### Return Value

A new CFUUID object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFUUID object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.

## See Also

### Creating CFUUID Objects
- [func CFUUIDCreateFromString(CFAllocator!, CFString!) -> CFUUID!](./cfuuidcreatefromstring%28_,_%29.md)
  Creates a CFUUID object for a specified string.
- [func CFUUIDCreateFromUUIDBytes(CFAllocator!, CFUUIDBytes) -> CFUUID!](./cfuuidcreatefromuuidbytes%28_,_%29.md)
  Creates a CFUUID object from raw UUID bytes.
- [func CFUUIDCreateWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](./cfuuidcreatewithbytes%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Creates a CFUUID object from raw UUID bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidcreate(_:))*