# init(bytes:)

**Framework**: CryptoTokenKit  
**Kind**: init

Initializes a `TKSmartCardATR` object from a provided data object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init?(bytes: Data)
```

#### Return Value

A `TKSmartCardATR` object initialized with the parsed data. If `bytes` does not contain a valid ATR, returns `nil`.

## Parameters

- `bytes`: The ATR data to be parsed.

## See Also

- [init?(source: () -> Int32)](tksmartcardatr/init(source:).md)
  Initializes a `TKSmartCardATR` object from a provided data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/init(bytes:))*