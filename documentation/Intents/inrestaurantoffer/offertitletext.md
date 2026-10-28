# offerTitleText

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user-readable text that summarizes the offer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var offerTitleText: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * offerTitleText;
```

*macOS*

```objc
@property (atomic, copy) NSString * offerTitleText;
```

## Discussion

The string you specify in this property should be brief and communicate the overall intent of the offer. Use the [`offerDetailText`](./offerdetailtext.md) property to communicate the details of the offer.

## See Also

### Accessing the Offer Details
- [var offerDetailText: String](./offerdetailtext.md)
  The user-readable text containing the details of the offer.
- [var offerIdentifier: String](./offeridentifier.md)
  The unique identifier associated with the offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantoffer/offertitletext)*