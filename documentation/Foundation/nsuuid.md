# NSUUID

**Framework**: Foundation  
**Kind**: class

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

#### Overview

In Swift, this object bridges to [`UUID`](nsuuid/uuid.md); use [`NSUUID`](nsuuid.md) when you need reference semantics or other Foundation-specific behavior.

UUIDs (Universally Unique Identifiers), also known as GUIDs (Globally Unique Identifiers) or IIDs (Interface Identifiers), are 128-bit values. UUIDs created by `NSUUID` conform to RFC 4122 version 4 and are created with random bytes.

The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`. The hex representation looks, as you might expect, like a list of numerical values preceded by 0x. For example, `0xD7`, `0x36`, `0x95`, `0x0A`, `0x4D`, `0x6E`, `0x12`, `0x26`, `0x80`, `0x3A`, `0x00`, `0x50`, `0xE4`, `0xC0`, `0x00`, `0x67`. Because a UUID is expressed simply as an array of bytes, there are no endianness considerations for different platforms.

The `NSUUID` class is  toll-free bridged with CoreFoundation’s [`CFUUID`](https://developer.apple.com/documentation/CoreFoundation/CFUUID). Use UUID strings to convert between `CFUUIDRef` and `NSUUID`, if needed. Two `NSUUID` objects are not guaranteed to be comparable by pointer value (as [`CFUUID`](https://developer.apple.com/documentation/CoreFoundation/CFUUID) is); use [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) to compare two `NSUUID` instances.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`UUID`](nsuuid/uuid.md) structure, which bridges to the [`NSUUID`](nsuuid.md) class. For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Creating UUIDs
- [init()](nsuuid/init.md)
  Initializes a new UUID with RFC 4122 version 4 random bytes.
- [convenience init?(uuidString: String)](nsuuid/init(uuidstring:).md)
  Initializes a new UUID with the formatted string.
- [convenience init(uuidBytes: UnsafePointer<UInt8>?)](nsuuid/init(uuidbytes:).md)
  Initializes a new UUID with the given bytes.
### Get UUID Values
- [func getBytes(UnsafeMutablePointer<UInt8>)](nsuuid/getbytes(_:).md)
  Returns the UUID as bytes.
- [var uuidString: String](nsuuid/uuidstring.md)
  The UUID as a string.
### Instance Methods
- [func compare(UUID) -> ComparisonResult](nsuuid/compare(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid)*