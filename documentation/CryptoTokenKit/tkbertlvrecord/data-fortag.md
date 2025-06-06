# data(forTag:)

**Framework**: CryptoTokenKit  
**Kind**: method

Encodes a specified tag using BER-TLV tag encoding rules.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func data(forTag tag: TKTLVTag) -> Data
```

#### Return Value

A data object that encodes a tag value using BER-TLV encoding.

## Parameters

- `tag`: The tag value to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/data(fortag:))*