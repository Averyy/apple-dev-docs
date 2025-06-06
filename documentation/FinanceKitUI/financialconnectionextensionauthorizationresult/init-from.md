# init(from:)

**Framework**: FinanceKitUI  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/financialconnectionextensionauthorizationresult/init(from:))*