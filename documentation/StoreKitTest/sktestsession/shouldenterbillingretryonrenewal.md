# shouldEnterBillingRetryOnRenewal

**Framework**: StoreKit Test  
**Kind**: property

A Boolean value that indicates whether the testing environment enters a billing retry state when an auto-renewable subscription renews.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+
- watchOS 8.5+

## Declaration

```swift
var shouldEnterBillingRetryOnRenewal: Bool { get set }
```

#### Discussion

The default value is `false`.

While this property is enabled, all renewals of auto-renewable subscriptions in the test environment fail due to a simulated billing issue and enter a billing retry state. To resolve the simulated billing issue, call [`resolveIssueForTransaction(identifier:)`](sktestsession/resolveissuefortransaction(identifier:).md) for the affected auto-renewable subscription.

The [`timeRate`](sktestsession/timerate-swift.property.md) value determines the length of the billing retry period in the testing environment.

## See Also

- [var billingGracePeriodIsEnabled: Bool](sktestsession/billinggraceperiodisenabled.md)
  A Boolean value that indicates whether the test environment simulates a billing grace period for auto-renewable subscriptions.
- [func resolveIssueForTransaction(identifier: Int) throws](sktestsession/resolveissuefortransaction(identifier:).md)
  Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/shouldenterbillingretryonrenewal)*