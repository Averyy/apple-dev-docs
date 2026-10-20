# PaymentCardReader.Options

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

Additional information you use to configure a payment card reader.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct Options
```

## Topics

### Creating an options structure
- [init(vasMerchants: [VASRequest.Merchant])](./options-swift.struct/init%28vasmerchants%29.md)
  Creates a new options structure with the specified list of merchants.
### Getting the list of merchants
- [var vasMerchants: [VASRequest.Merchant]](./options-swift.struct/vasmerchants.md)
  A global list of merchants to use when reading loyalty cards.
### Setting read behaviors
- [var includeErrorInReadResult: Bool](./options-swift.struct/includeerrorinreadresult.md)
  A Boolean value that indicates whether the framework returns a result instead of throwing an error when some data is retrievable.
- [var returnReadResultImmediately: Bool](./options-swift.struct/returnreadresultimmediately.md)
  A Boolean value that indicates whether the framework returns a result as soon as possible before closing the system UI.
### Initializers
- [init()](./options-swift.struct/init%28%29.md)
  Creates a new options structure with default values

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a payment reader
- [init(options: PaymentCardReader.Options)](./init%28options%29.md)
  Creates a payment card reader with the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/options-swift.struct)*