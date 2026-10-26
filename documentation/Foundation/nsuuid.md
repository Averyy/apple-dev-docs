# NSUUID

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A universally unique value that can be used to identify types, interfaces, and other items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSUUID
```

```objc
@interface NSUUID : NSObject
```

#### Overview

In Swift, this object bridges to [`UUID`](./nsuuid/uuid.md); use [`NSUUID`](./nsuuid.md) when you need reference semantics or other Foundation-specific behavior.

UUIDs (Universally Unique Identifiers), also known as GUIDs (Globally Unique Identifiers) or IIDs (Interface Identifiers), are 128-bit values. UUIDs created by `NSUUID` conform to RFC 4122 version 4 and are created with random bytes.

The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`. The hex representation looks, as you might expect, like a list of numerical values preceded by 0x. For example, `0xD7`, `0x36`, `0x95`, `0x0A`, `0x4D`, `0x6E`, `0x12`, `0x26`, `0x80`, `0x3A`, `0x00`, `0x50`, `0xE4`, `0xC0`, `0x00`, `0x67`. Because a UUID is expressed simply as an array of bytes, there are no endianness considerations for different platforms.

The `NSUUID` class is *not* toll-free bridged with CoreFoundation’s [`CFUUID`](../CoreFoundation/cfuuid.md). Use UUID strings to convert between `CFUUIDRef` and `NSUUID`, if needed. Two `NSUUID` objects are not guaranteed to be comparable by pointer value (as [`CFUUID`](../CoreFoundation/cfuuid.md) is); use [`isEqual(_:)`](../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) to compare two `NSUUID` instances.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`UUID`](./nsuuid/uuid.md) structure, which bridges to the [`NSUUID`](./nsuuid.md) class. For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Creating UUIDs
- [init()](./nsuuid/init%28%29.md)
  Initializes a new UUID with RFC 4122 version 4 random bytes.
- [convenience init?(uuidString: String)](./nsuuid/init%28uuidstring%29-8t9n3.md)
  Initializes a new UUID with the formatted string.
- [convenience init(uuidBytes: UnsafePointer<UInt8>?)](./nsuuid/init%28uuidbytes%29-2p4d5.md)
  Initializes a new UUID with the given bytes.
- [+ UUID](./nsuuid/uuid.md)
  Create and returns a new UUID with RFC 4122 version 4 random bytes.
### Get UUID Values
- [func getBytes(UnsafeMutablePointer<UInt8>)](./nsuuid/getbytes%28_%29.md)
  Returns the UUID as bytes.
- [var uuidString: String](./nsuuid/uuidstring.md)
  The UUID as a string.
### Initializers
- [convenience init(UUIDBytes: UnsafePointer<UInt8>?)](./nsuuid/init%28uuidbytes%29-4fntq.md)
- [convenience init?(UUIDString: String)](./nsuuid/init%28uuidstring%29-8kcx.md)
- [init?(coder: NSCoder)](./nsuuid/init%28coder%29.md)
### Instance Methods
- [func compare(UUID) -> ComparisonResult](./nsuuid/compare%28_%29.md)
  Compares the receiver to another NSUUID in constant time.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid)*