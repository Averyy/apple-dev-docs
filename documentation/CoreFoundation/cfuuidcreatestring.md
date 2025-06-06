# CFUUIDCreateString(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the string representation of a specified CFUUID object.

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
func CFUUIDCreateString(_ alloc: CFAllocator!, _ uuid: CFUUID!) -> CFString!
```

#### Return Value

The string representation of `uuid`. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new string. Pass   or   to use the current default allocator.
- `uuid`: The CFUUID object whose string representation to obtain.

## See Also

- [func CFUUIDGetConstantUUIDWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](cfuuidgetconstantuuidwithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a CFUUID object from raw UUID bytes.
- [func CFUUIDGetUUIDBytes(CFUUID!) -> CFUUIDBytes](cfuuidgetuuidbytes(_:).md)
  Returns the value of a UUID object as raw bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidcreatestring(_:_:))*