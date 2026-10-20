# canMakePayments()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

A method that indicates whether the person can make purchases.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use AppStore.canMakePayments.

## Declaration

```swift
class func canMakePayments() -> Bool
```

```objc
+ (BOOL) canMakePayments;
```

#### Discussion

The Boolean value that this method returns is identical to the value of the type property [`canMakePayments`](../appstore/canmakepayments.md) in the [`AppStore`](../appstore.md) object. For more information about using and interpreting this value, see the type property page [`canMakePayments`](../appstore/canmakepayments.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/canmakepayments())*