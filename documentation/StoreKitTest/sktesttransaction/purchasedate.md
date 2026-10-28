# purchaseDate

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The date of purchase for the transaction.

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
var purchaseDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * purchaseDate;
```

## Discussion

The purchase date applies to any type of Apple In-App Purchase.

## See Also

### Getting Dates
- [var cancelDate: Date?](./canceldate.md)
  The date when the system refunded the transaction.
- [var expirationDate: Date?](./expirationdate.md)
  The date a subscription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/purchasedate)*