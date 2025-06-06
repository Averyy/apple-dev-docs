# CFUUIDGetUUIDBytes(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the value of a UUID object as raw bytes.

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
func CFUUIDGetUUIDBytes(_ uuid: CFUUID!) -> CFUUIDBytes
```

#### Return Value

The value of `uuid` represented as raw bytes.

## Parameters

- `uuid`: The CFUUID object to examine.

## See Also

- [func CFUUIDCreateString(CFAllocator!, CFUUID!) -> CFString!](cfuuidcreatestring(_:_:).md)
  Returns the string representation of a specified CFUUID object.
- [func CFUUIDGetConstantUUIDWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](cfuuidgetconstantuuidwithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a CFUUID object from raw UUID bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuidgetuuidbytes(_:))*