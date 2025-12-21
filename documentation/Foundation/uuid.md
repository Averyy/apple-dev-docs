# UUID

**Framework**: Foundation  
**Kind**: struct

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
- [init()](uuid/init.md)
  Creates a UUID with RFC 4122 version 4 random bytes.
- [init(uuid: uuid_t)](uuid/init(uuid:).md)
  Creates a UUID from the uuid C-language structure.
- [init?(uuidString: String)](uuid/init(uuidstring:).md)
  Creates a UUID from a string representation.
### Getting UUID Values
- [var uuid: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](uuid/uuid.md)
  Returns the UUID as bytes.
- [var uuidString: String](uuid/uuidstring.md)
  Returns a string created from the UUID, such as “E621E1F8-C36C-495A-93FC-0C247A3E6E5F”
### Using Reference Types
- [class NSUUID](nsuuid.md)
  A universally unique value that can be used to identify types, interfaces, and other items.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [EntityIdentifierConvertible](../AppIntents/EntityIdentifierConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/uuid)*