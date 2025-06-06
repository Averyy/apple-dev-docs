# failureError

**Framework**: StoreKit Test  
**Kind**: property

The error code that transactions return when you enable failing transactions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
var failureError: SKError.Code { get set }
```

#### Discussion

You can force an error by setting [`failTransactionsEnabled`](sktestsession/failtransactionsenabled.md) to `true` and setting [`failureError`](sktestsession/failureerror.md) value to one of these supported error codes: [`SKError.Code.unknown`](https://developer.apple.com/documentation/StoreKit/SKError/Code/unknown), [`SKError.Code.invalidOfferIdentifier`](https://developer.apple.com/documentation/StoreKit/SKError/Code/invalidOfferIdentifier), [`SKError.Code.invalidSignature`](https://developer.apple.com/documentation/StoreKit/SKError/Code/invalidSignature), [`SKError.Code.missingOfferParams`](https://developer.apple.com/documentation/StoreKit/SKError/Code/missingOfferParams), [`SKError.Code.invalidOfferPrice`](https://developer.apple.com/documentation/StoreKit/SKError/Code/invalidOfferPrice).

Use these settings to test your how your app responds to failed transactions.

## See Also

- [var failTransactionsEnabled: Bool](sktestsession/failtransactionsenabled.md)
  A Boolean value that determines whether transactions fail in the testing environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/failureerror)*