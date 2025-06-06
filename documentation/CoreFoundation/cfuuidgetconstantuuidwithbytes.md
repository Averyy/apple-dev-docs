# CFUUIDGetConstantUUIDWithBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a CFUUID object from raw UUID bytes.

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
func CFUUIDGetConstantUUIDWithBytes(_ alloc: CFAllocator!, _ byte0: UInt8, _ byte1: UInt8, _ byte2: UInt8, _ byte3: UInt8, _ byte4: UInt8, _ byte5: UInt8, _ byte6: UInt8, _ byte7: UInt8, _ byte8: UInt8, _ byte9: UInt8, _ byte10: UInt8, _ byte11: UInt8, _ byte12: UInt8, _ byte13: UInt8, _ byte14: UInt8, _ byte15: UInt8) -> CFUUID!
```

#### Return Value

A CFUUID object. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

This function can be used in headers to declare a UUID constant with `#define`.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new CFUUID object. Pass   or   to use the current default allocator.
- `byte0`: Raw byte number  .
- `byte1`: Raw byte number  .
- `byte2`: Raw byte number  .
- `byte3`: Raw byte number  .
- `byte4`: Raw byte number  .
- `byte5`: Raw byte number  .
- `byte6`: Raw byte number  .
- `byte7`: Raw byte number  .
- `byte8`: Raw byte number  .
- `byte9`: Raw byte number  .
- `byte10`: Raw byte number  .
- `byte11`: Raw byte number  .
- `byte12`: Raw byte number  .
- `byte13`: Raw byte number  .
- `byte14`: Raw byte number  .
- `byte15`: Raw byte number  .

## See Also

- [func CFUUIDCreateString(CFAllocator!, CFUUID!) -> CFString!](cfuuidcreatestring(_:_:).md)
  Returns the string representation of a specified CFUUID object.
- [func CFUUIDGetUUIDBytes(CFUUID!) -> CFUUIDBytes](cfuuidgetuuidbytes(_:).md)
  Returns the value of a UUID object as raw bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidgetconstantuuidwithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*