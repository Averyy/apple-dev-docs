# init(source:)

**Framework**: CryptoTokenKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSource:(int (^)()) source;
```

#### Return Value

A `TKSmartCardATR` object initialized with the parsed data. If the byte stream produces an error or does not contain a valid ATR, returns `nil`.

## Parameters

- `source`: The block providing a stream of data for an ATR.

  The block takes no arguments and returns one byte. To indicate that an error occured, the block returns `-1`.

## See Also

### Creating a Smart Card ATR
- [init?(bytes: Data)](./init%28bytes%29.md)
  Initializes a `TKSmartCardATR` object from a provided data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/init(source:))*