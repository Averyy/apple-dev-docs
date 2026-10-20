# UUID

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A universally unique value to identify types, interfaces, and other items.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 6.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct UUID
```

## Topics

### Creating UUIDs
- [init()](./uuid/init%28%29.md)
  Creates a UUID with RFC 4122 version 4 random bytes.
- [init(uuid: uuid_t)](./uuid/init%28uuid%29.md)
  Creates a UUID from the uuid C-language structure.
- [init?(uuidString: String)](./uuid/init%28uuidstring%29.md)
  Creates a UUID from a string representation.
### Getting UUID Values
- [var uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](./uuid/uuid.md)
  Returns the UUID as bytes.
- [var uuidString: String](./uuid/uuidstring.md)
  Returns a string created from the UUID, such as “E621E1F8-C36C-495A-93FC-0C247A3E6E5F”
### Using Reference Types
- [class NSUUID](./nsuuid.md)
  A universally unique value that can be used to identify types, interfaces, and other items.
### Type Methods
- [static func random(using: inout some RandomNumberGenerator) -> UUID](./uuid/random%28using%29.md)
  Generates a new random UUID.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [EntityIdentifierConvertible](../AppIntents/entityidentifierconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [ReferenceConvertible](./referenceconvertible.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/uuid)*