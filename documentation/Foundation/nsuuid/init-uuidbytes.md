# init(uuidBytes:)

**Framework**: Foundation  
**Kind**: init

Initializes a new UUID with the given bytes.

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
convenience init(uuidBytes bytes: UnsafePointer<UInt8>?)
```

#### Return Value

A new UUID object.

## Parameters

- `bytes`: Raw UUID bytes to use to create the UUID.

## See Also

- [init()](nsuuid/init.md)
  Initializes a new UUID with RFC 4122 version 4 random bytes.
- [convenience init?(uuidString: String)](nsuuid/init(uuidstring:).md)
  Initializes a new UUID with the formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/init(uuidbytes:))*