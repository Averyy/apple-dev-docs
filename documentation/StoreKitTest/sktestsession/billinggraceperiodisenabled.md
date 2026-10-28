# billingGracePeriodIsEnabled

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the test environment simulates a billing grace period for auto-renewable subscriptions.

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
var billingGracePeriodIsEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL billingGracePeriodEnabled;
```

## Discussion

The default value is `false`. The value of this property has no effect when [`shouldEnterBillingRetryOnRenewal`](./shouldenterbillingretryonrenewal.md) is `false`.

In the production environment, you indicate whether your app supports a billing grace period by setting it in App Store Connect. In the testing environment, you indicate that your app supports it by setting the [`billingGracePeriodIsEnabled`](./billinggraceperiodisenabled.md) property to `true`.

To test how your app handles a grace period when a subscription enters a billing retry state, enable [`shouldEnterBillingRetryOnRenewal`](./shouldenterbillingretryonrenewal.md) and [`billingGracePeriodIsEnabled`](./billinggraceperiodisenabled.md). All subscriptions fail to renew with a simulated billing issue until you set [`shouldEnterBillingRetryOnRenewal`](./shouldenterbillingretryonrenewal.md) to `false`. To resolve a billing issue in the testing environment, call [`resolveIssueForTransaction(identifier:)`](./resolveissuefortransaction%28identifier%29.md).

For more information about billing grace periods and enabling them in the production environment, see [Reducing Involuntary Subscriber Churn](../../StoreKit/reducing-involuntary-subscriber-churn.md) and [Enable billing grace period for auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev58bda3212).

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](./resettodefaultstate%28%29.md) to revert all settings to those in the configuration file.

## See Also

### Testing billing retry and grace period
- [var shouldEnterBillingRetryOnRenewal: Bool](./shouldenterbillingretryonrenewal.md)
  A Boolean value that indicates whether the testing environment enters a billing retry state when an auto-renewable subscription renews.
- [func resolveIssueForTransaction(identifier: Int) throws](./resolveissuefortransaction%28identifier%29.md)
  Simulates resolving an issue when you test interrupted purchases or billing retry scenarios.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/billinggraceperiodisenabled)*