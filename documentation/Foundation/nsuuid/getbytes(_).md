# getBytes(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the UUID as bytes.

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
func getBytes(_ uuid: UnsafeMutablePointer<UInt8>)
```

```objc
- (void) getUUIDBytes:(uuid_t) uuid;
```

## Parameters

- `uuid`: The value of uuid represented as raw bytes.

## See Also

### Get UUID Values
- [var uuidString: String](./uuidstring.md)
  The UUID as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuuid/getbytes(_:))*