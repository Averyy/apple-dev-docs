# init(options:)

**Framework**: ProximityReader  
**Kind**: init

Creates a payment card reader with the specified options.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
init(options: PaymentCardReader.Options = .init())
```

#### Discussion

Keep a strong reference to the returned object for the duration of the reader session.

## Parameters

- `options`: The configuration settings for the reader.

## See Also

- [PaymentCardReader.Options](paymentcardreader/options-swift.struct.md)
  Additional information you use to configure a payment card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/init(options:))*