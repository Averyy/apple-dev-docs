# init(from:)

**Framework**: RealityKit  
**Kind**: init

Creates a new instance from a decoder.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS ?+

## Declaration

```swift
required init(from decoder: any Decoder) throws
```

#### Discussion

Throws an error if reading from `decoder` fails, or if the data is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [func encode(to: any Encoder) throws](networkcompatibilitytoken/encode(to:).md)
  Writes the token’s data into an encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/init(from:))*