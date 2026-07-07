# value

**Framework**: StoreKit  
**Kind**: property

The entitlement value if the task is successful.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var value: Value? { get }
```

#### Discussion

This value is `nil` while the value is loading, or if it fails to load for any reason.

Use [`value`](entitlementtaskstate/value.md) as a convenience to access the entitlement value in code that doesn’t depend on the reason the value can’t be accessed if it fails to load.

## See Also

- [var transaction: VerificationResult<Transaction>?](entitlementtaskstate/transaction.md)
  The transaction value if the task is successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/entitlementtaskstate/value)*