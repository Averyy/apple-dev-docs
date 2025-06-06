# init(from:)

**Framework**: ContactProvider  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [func encode(to: any Encoder) throws](contactitempage/encode(to:).md)
  Encodes this value into the given encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactitempage/init(from:))*