# state

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The state of the transaction in the test environment.

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
var state: SKPaymentTransactionState { get }
```

```objc
@property (nonatomic, readonly) SKPaymentTransactionState state;
```

## Discussion

The transaction states in the test environment are the same states that StoreKit uses in production.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/state)*