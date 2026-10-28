# timeRate

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The rate at which time passes for subscriptions in the test environment as compared to real time.

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
var timeRate: SKTestSession.TimeRate { get set }
```

```objc
@property (nonatomic, assign) SKTestTimeRate timeRate;
```

## Discussion

Use the [`timeRate`](./timerate-swift.property.md) value when you test auto-renewable subscriptions to speed up or slow down the time it takes for subscriptions to renew in the test environment. The default value is [`SKTestSession.TimeRate.realTime`](./timerate-swift.enum/realtime.md). For maximum accelerated time, use [`SKTestSession.TimeRate.oneRenewalEveryTwoSeconds`](./timerate-swift.enum/onerenewaleverytwoseconds.md).

To test subscription renewals, you can also call [`forceRenewalOfSubscription(productIdentifier:)`](./forcerenewalofsubscription%28productidentifier%29.md) to prompt a subscription to renew immediately.

The time rate also affects the length of the billing retry period and the billing grace period in the test environment. See the [`SKTestSession.TimeRate`](./timerate-swift.enum.md) enumeration for the actual time values of each case.

Changing this property overrides its setting in the StoreKit configuration file for this test session. Call [`resetToDefaultState()`](./resettodefaultstate%28%29.md) to revert all settings to those in the configuration file.

## See Also

### Testing subscription renewals
- [SKTestSession.TimeRate](./timerate-swift.enum.md)
  The values for rates of time passing in the test environment.
- [func enableAutoRenewForTransaction(identifier: Int) throws](./enableautorenewfortransaction%28identifier%29.md)
  Enables auto-renewing for an auto-renewable subscription in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](./disableautorenewfortransaction%28identifier%29.md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func forceRenewalOfSubscription(productIdentifier: String) throws](./forcerenewalofsubscription%28productidentifier%29.md)
  Ends the previous subscription period and begins the next period in the test environment.
- [func expireSubscription(productIdentifier: String) throws](./expiresubscription%28productidentifier%29.md)
  Causes the identified auto-renewable subscription to expire immediately in the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/timerate-swift.property)*