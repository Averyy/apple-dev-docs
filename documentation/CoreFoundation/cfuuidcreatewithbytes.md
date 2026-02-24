# CFUUIDCreateWithBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

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
func CFUUIDCreateWithBytes(_ alloc: CFAllocator!, _ byte0: UInt8, _ byte1: UInt8, _ byte2: UInt8, _ byte3: UInt8, _ byte4: UInt8, _ byte5: UInt8, _ byte6: UInt8, _ byte7: UInt8, _ byte8: UInt8, _ byte9: UInt8, _ byte10: UInt8, _ byte11: UInt8, _ byte12: UInt8, _ byte13: UInt8, _ byte14: UInt8, _ byte15: UInt8) -> CFUUID!
```

#### Return Value

A new CFUUID object, or, if a CFUUID object of the same value already exists, the existing instance with its reference count incremented. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFUUID object. Pass `NULL` or [`kCFAllocatorDefault`](kcfallocatordefault.md) to use the current default allocator.
- `byte0`: Raw byte number `0`.
- `byte1`: Raw byte number `1`.
- `byte2`: Raw byte number `2`.
- `byte3`: Raw byte number `3`.
- `byte4`: Raw byte number `4`.
- `byte5`: Raw byte number `5`.
- `byte6`: Raw byte number `6`.
- `byte7`: Raw byte number `7`.
- `byte8`: Raw byte number `8`.
- `byte9`: Raw byte number `9`.
- `byte10`: Raw byte number `10`.
- `byte11`: Raw byte number `11`.
- `byte12`: Raw byte number `12`.
- `byte13`: Raw byte number `13`.
- `byte14`: Raw byte number `14`.
- `byte15`: Raw byte number `15`.

## See Also

- [func CFUUIDCreate(CFAllocator!) -> CFUUID!](cfuuidcreate(_:).md)
  Creates a Universally Unique Identifier (UUID) object.
- [func CFUUIDCreateFromString(CFAllocator!, CFString!) -> CFUUID!](cfuuidcreatefromstring(_:_:).md)
  Creates a CFUUID object for a specified string.
- [func CFUUIDCreateFromUUIDBytes(CFAllocator!, CFUUIDBytes) -> CFUUID!](cfuuidcreatefromuuidbytes(_:_:).md)
  Creates a CFUUID object from raw UUID bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidcreatewithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*