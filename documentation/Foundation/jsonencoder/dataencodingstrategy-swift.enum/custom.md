# JSONEncoder.DataEncodingStrategy.custom(_:)

**Framework**: Foundation  
**Kind**: case

The strategy that encodes data using a user-defined function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@preconcurrency
case custom((Data, any Encoder) throws -> Void)
```

#### Discussion

If the user-defined function throws, the encoder uses an empty container in place of the data.

## Parameters

- `custom`: A closure that receives the data to encode and the encoder instance to encode to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonencoder/dataencodingstrategy-swift.enum/custom(_:))*