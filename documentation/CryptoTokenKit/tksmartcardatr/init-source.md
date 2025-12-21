# init(source:)

**Framework**: CryptoTokenKit  
**Kind**: init

Initializes a `TKSmartCardATR` object from a provided data source.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init?(source: @escaping () -> Int32)
```

#### Return Value

A `TKSmartCardATR` object initialized with the parsed data. If the byte stream produces an error or does not contain a valid ATR, returns `nil`.

## Parameters

- `source`: The block takes no arguments and returns one byte. To indicate that an error occured, the block returns  .

## See Also

- [init?(bytes: Data)](tksmartcardatr/init(bytes:).md)
  Initializes a `TKSmartCardATR` object from a provided data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/init(source:))*