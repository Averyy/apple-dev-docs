# CFUUIDGetConstantUUIDWithBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a CFUUID object from raw UUID bytes.

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
func CFUUIDGetConstantUUIDWithBytes(_ alloc: CFAllocator!, _ byte0: UInt8, _ byte1: UInt8, _ byte2: UInt8, _ byte3: UInt8, _ byte4: UInt8, _ byte5: UInt8, _ byte6: UInt8, _ byte7: UInt8, _ byte8: UInt8, _ byte9: UInt8, _ byte10: UInt8, _ byte11: UInt8, _ byte12: UInt8, _ byte13: UInt8, _ byte14: UInt8, _ byte15: UInt8) -> CFUUID!
```

```c
extern CFUUIDRefCFUUIDGetConstantUUIDWithBytes(CFAllocatorRef alloc, UInt8 byte0, UInt8 byte1, UInt8 byte2, UInt8 byte3, UInt8 byte4, UInt8 byte5, UInt8 byte6, UInt8 byte7, UInt8 byte8, UInt8 byte9, UInt8 byte10, UInt8 byte11, UInt8 byte12, UInt8 byte13, UInt8 byte14, UInt8 byte15);
```

#### Return Value

A CFUUID object. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

This function can be used in headers to declare a UUID constant with `#define`.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFUUID object. Pass `NULL` or [`kCFAllocatorDefault`](./kcfallocatordefault.md) to use the current default allocator.
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

### Getting Information About CFUUID Objects
- [func CFUUIDCreateString(CFAllocator!, CFUUID!) -> CFString!](./cfuuidcreatestring%28_,_%29.md)
  Returns the string representation of a specified CFUUID object.
- [func CFUUIDGetUUIDBytes(CFUUID!) -> CFUUIDBytes](./cfuuidgetuuidbytes%28_%29.md)
  Returns the value of a UUID object as raw bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidgetconstantuuidwithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*