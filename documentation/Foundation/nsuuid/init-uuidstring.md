# init(uuidString:)

**Framework**: Foundation  
**Kind**: init

Initializes a new UUID with the formatted string.

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
convenience init?(uuidString string: String)
```

#### Return Value

A new UUID object. Returns `nil` for invalid strings.

## Parameters

- `string`: The source string containing the UUID. The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example  .

## See Also

- [init()](nsuuid/init.md)
  Initializes a new UUID with RFC 4122 version 4 random bytes.
- [convenience init(uuidBytes: UnsafePointer<UInt8>?)](nsuuid/init(uuidbytes:).md)
  Initializes a new UUID with the given bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/init(uuidstring:))*