# init(uuidString:)

**Framework**: Foundation  
**Kind**: init

Creates a UUID from a string representation.

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
init?(uuidString string: String)
```

#### Discussion

Returns `nil` if the string isn’t a valid UUID representation.

## Parameters

- `string`: The string representation of a UUID, such as  .

## See Also

- [init()](uuid/init.md)
  Creates a UUID with RFC 4122 version 4 random bytes.
- [init(uuid: uuid_t)](uuid/init(uuid:).md)
  Creates a UUID from the uuid C-language structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/uuid/init(uuidstring:))*