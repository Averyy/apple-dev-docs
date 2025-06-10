# init(from:)

**Framework**: TelephonyMessagingKit  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [func encode(to: any Encoder) throws](rcsservice/business/menu/encode(to:).md)
  Encodes this value into the given encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/menu/init(from:))*