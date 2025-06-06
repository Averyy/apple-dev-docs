# init(uuid:)

**Framework**: Foundation  
**Kind**: init

Creates a UUID from the uuid C-language structure.

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
init(uuid: uuid_t)
```

## Parameters

- `uuid`: The C-language structure of a UUID.

## See Also

- [init()](uuid/init.md)
  Creates a UUID with RFC 4122 version 4 random bytes.
- [init?(uuidString: String)](uuid/init(uuidstring:).md)
  Creates a UUID from a string representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/uuid/init(uuid:))*