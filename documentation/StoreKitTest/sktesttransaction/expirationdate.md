# expirationDate

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The date a subscription expires.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var expirationDate: Date? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDate * expirationDate;
```

## Discussion

The test environment sets the expiration date based on the subscription settings in your active StoreKit configuration file.

## See Also

### Getting Dates
- [var purchaseDate: Date](./purchasedate.md)
  The date of purchase for the transaction.
- [var cancelDate: Date?](./canceldate.md)
  The date when the system refunded the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/expirationdate)*