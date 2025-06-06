# CFUUID

**Framework**: Core Foundation  
**Kind**: class

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
class CFUUID
```

#### Overview

CFUUID objects are used by plug-ins to uniquely identify types, interfaces, and factories. When creating a new type, host developers must generate UUIDs to identify the type as well as its interfaces and factories.

UUIDs (Universally Unique Identifiers), also known as GUIDs (Globally Unique Identifiers) or IIDs (Interface Identifiers), are 128-bit values designed to be unique.

The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`. The hex representation looks, as you might expect, like a list of numerical values preceded by `0x`. For example, `0x68, 0x75, 0x3A, 0x44, 0x4D, 0x6F, 0x12, 0x26, 0x9C, 0x60, 0x00, 0x50, 0xE4, 0xC0, 0x00, 0x67` . To use a UUID, you create it and then copy the resulting strings into your header and C language source files. Because a UUID is expressed as an array of bytes, there are no endianness considerations for different platforms.

You can create a CFUUID object using any one of the `CFUUIDCreate...` functions. Use the [`CFUUIDGetConstantUUIDWithBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](cfuuidgetconstantuuidwithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) function if you want to declare a UUID constant in a `#define` statement. You can get the raw bytes of an existing CFUUID object using the [`CFUUIDGetUUIDBytes(_:)`](cfuuidgetuuidbytes(_:).md) function.

## Topics

### Creating CFUUID Objects
- [func CFUUIDCreate(CFAllocator!) -> CFUUID!](cfuuidcreate(_:).md)
  Creates a Universally Unique Identifier (UUID) object.
- [func CFUUIDCreateFromString(CFAllocator!, CFString!) -> CFUUID!](cfuuidcreatefromstring(_:_:).md)
  Creates a CFUUID object for a specified string.
- [func CFUUIDCreateFromUUIDBytes(CFAllocator!, CFUUIDBytes) -> CFUUID!](cfuuidcreatefromuuidbytes(_:_:).md)
  Creates a CFUUID object from raw UUID bytes.
- [func CFUUIDCreateWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](cfuuidcreatewithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Creates a CFUUID object from raw UUID bytes.
### Getting Information About CFUUID Objects
- [func CFUUIDCreateString(CFAllocator!, CFUUID!) -> CFString!](cfuuidcreatestring(_:_:).md)
  Returns the string representation of a specified CFUUID object.
- [func CFUUIDGetConstantUUIDWithBytes(CFAllocator!, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) -> CFUUID!](cfuuidgetconstantuuidwithbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Returns a CFUUID object from raw UUID bytes.
- [func CFUUIDGetUUIDBytes(CFUUID!) -> CFUUIDBytes](cfuuidgetuuidbytes(_:).md)
  Returns the value of a UUID object as raw bytes.
### Getting the CFUUID Type Identifier
- [func CFUUIDGetTypeID() -> CFTypeID](cfuuidgettypeid().md)
  Returns the type identifier for all CFUUID objects.
### Data Types
- [struct CFUUIDBytes](cfuuidbytes.md)
  A 128-bit struct that represents a UUID as raw bytes.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfuuid)*