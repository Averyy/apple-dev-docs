# CFUUIDCreateFromString(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFUUID object for a specified string.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFUUIDCreateFromString(_ alloc: CFAllocator!, _ uuidStr: CFString!) -> CFUUID!
```

#### Return Value

A new CFUUID object, or if a CFUUID object of the same value already exists, the existing instance with its reference count incremented. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFUUID object. Pass   or   to use the current default allocator.
- `uuidStr`: A string containing a UUID. The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example  .

## See Also

- [func CFUUIDCreate(CFAllocator!) -> CFUUID!](cfuuidcreate(_:).md)
  Creates a Universally Unique Identifier (UUID) object.
- [func CFUUIDCreateFromUUIDBytes(CFAllocator!, CFUUIDBytes) -> CFUUID!](cfuuidcreatefromuuidbytes(_:_:).md)
  Creates a CFUUID object from raw UUID bytes.
- [func CFUUIDCreateWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](cfuuidcreatewithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a CFUUID object from raw UUID bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidcreatefromstring(_:_:))*