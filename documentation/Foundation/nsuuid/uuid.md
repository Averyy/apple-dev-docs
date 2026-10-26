# UUID

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Create and returns a new UUID with RFC 4122 version 4 random bytes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) UUID;
```

#### Return Value

A new UUID object.

## See Also

### Creating UUIDs
- [init()](./init%28%29.md)
  Initializes a new UUID with RFC 4122 version 4 random bytes.
- [convenience init?(uuidString: String)](./init%28uuidstring%29-8t9n3.md)
  Initializes a new UUID with the formatted string.
- [convenience init(uuidBytes: UnsafePointer<UInt8>?)](./init%28uuidbytes%29-2p4d5.md)
  Initializes a new UUID with the given bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/uuid)*