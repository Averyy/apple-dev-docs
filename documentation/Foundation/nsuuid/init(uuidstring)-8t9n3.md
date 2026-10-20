# init(uuidString:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithUUIDString:(NSString *) string;
```

#### Return Value

A new UUID object. Returns `nil` for invalid strings.

## Parameters

- `string`: The source string containing the UUID. The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`.

## See Also

### Creating UUIDs
- [init()](./init%28%29.md)
  Initializes a new UUID with RFC 4122 version 4 random bytes.
- [convenience init(uuidBytes: UnsafePointer<UInt8>?)](./init%28uuidbytes%29-2p4d5.md)
  Initializes a new UUID with the given bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/init(uuidstring:)-8t9n3)*