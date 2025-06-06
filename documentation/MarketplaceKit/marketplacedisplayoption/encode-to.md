# encode(to:)

**Framework**: MarketplaceKit  
**Kind**: method

Encodes this value into the given encoder.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplacedisplayoption/encode(to:))*