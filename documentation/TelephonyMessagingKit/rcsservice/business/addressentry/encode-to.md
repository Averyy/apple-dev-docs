# encode(to:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Encodes this value into the given encoder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.

## See Also

- [init(from: any Decoder) throws](rcsservice/business/addressentry/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/addressentry/encode(to:))*