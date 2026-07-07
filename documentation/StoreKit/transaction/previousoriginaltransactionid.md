# previousOriginalTransactionID

**Framework**: StoreKit  
**Kind**: property

The original transaction ID of the subscription this one replaced when a customer switched between a standalone auto-renewable subscription and a subscription bundle (in either direction).

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
var previousOriginalTransactionID: UInt64? { get }
```

#### Discussion

For a bundle transaction, this is the standalone subscription’s original transaction ID, while for a standalone transaction, this is the bundle’s original transaction ID. This field is `nil` if no such switch occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/previousoriginaltransactionid)*