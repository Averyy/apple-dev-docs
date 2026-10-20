# init(from:)

**Framework**: Combine  
**Kind**: init  
**Role**: Initializer

Creates a demand instance from a decoder.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

## Parameters

- `decoder`: The decoder of a previously-encoded [`Subscribers.Demand`](../demand.md) instance.

## See Also

### Encoding and decoding
- [func encode(to: any Encoder) throws](./encode%28to%29.md)
  Encodes the demand to the provide encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/subscribers/demand/init(from:))*