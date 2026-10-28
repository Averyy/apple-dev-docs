# init()

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a new UUID with RFC 4122 version 4 random bytes.

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
init()
```

```objc
- (instancetype) init;
```

## Return Value

A new UUID object.

## See Also

### Creating UUIDs
- [convenience init?(uuidString: String)](./init%28uuidstring%29-8t9n3.md)
  Initializes a new UUID with the formatted string.
- [convenience init(uuidBytes: UnsafePointer<UInt8>?)](./init%28uuidbytes%29-2p4d5.md)
  Initializes a new UUID with the given bytes.
### Related Documentation
- [+ UUID](./uuid.md)
  Create and returns a new UUID with RFC 4122 version 4 random bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/init())*