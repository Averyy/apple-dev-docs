# CFUUIDCreateFromUUIDBytes(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a CFUUID object from raw UUID bytes.

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
func CFUUIDCreateFromUUIDBytes(_ alloc: CFAllocator!, _ bytes: CFUUIDBytes) -> CFUUID!
```

#### Return Value

A new CFUUID object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFUUID object. Pass   or   to use the current default allocator.
- `bytes`: Raw UUID bytes to use to create the CFUUID object.

## See Also

- [func CFUUIDCreate(CFAllocator!) -> CFUUID!](cfuuidcreate(_:).md)
  Creates a Universally Unique Identifier (UUID) object.
- [func CFUUIDCreateFromString(CFAllocator!, CFString!) -> CFUUID!](cfuuidcreatefromstring(_:_:).md)
  Creates a CFUUID object for a specified string.
- [func CFUUIDCreateWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](cfuuidcreatewithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a CFUUID object from raw UUID bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidcreatefromuuidbytes(_:_:))*