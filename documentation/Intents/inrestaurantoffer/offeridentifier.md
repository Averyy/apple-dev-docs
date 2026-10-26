# offerIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier associated with the offer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var offerIdentifier: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * offerIdentifier;
```

*macOS*

```objc
@property (atomic, copy) NSString * offerIdentifier;
```

#### Discussion

For each offer, your company or the restaurant must provide a unique identifier for the offer. Use the identifier to validate the offer in your system. You can also pass the identifier to the restaurant if it has a system for validating special offers.

## See Also

### Accessing the Offer Details
- [var offerTitleText: String](./offertitletext.md)
  The user-readable text that summarizes the offer.
- [var offerDetailText: String](./offerdetailtext.md)
  The user-readable text containing the details of the offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrestaurantoffer/offeridentifier)*