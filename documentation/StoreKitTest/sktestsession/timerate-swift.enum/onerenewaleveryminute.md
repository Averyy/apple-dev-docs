# SKTestSession.TimeRate.oneRenewalEveryMinute

**Framework**: StoreKit Test  
**Kind**: case

A rate of time in the test environment in which subscriptions of any time length renew every minute.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
case oneRenewalEveryMinute
```

#### Discussion

This time rate renews subscriptions every minute in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 1 minute |
| Billing retry period | 2 minutes |

## See Also

- [SKTestSession.TimeRate.oneRenewalEveryFifteenMinutes](sktestsession/timerate-swift.enum/onerenewaleveryfifteenminutes.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 15 minutes.
- [SKTestSession.TimeRate.oneRenewalEveryFiveMinutes](sktestsession/timerate-swift.enum/onerenewaleveryfiveminutes.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 5 minutes.
- [SKTestSession.TimeRate.oneRenewalEveryThirtySeconds](sktestsession/timerate-swift.enum/onerenewaleverythirtyseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 30 seconds.
- [SKTestSession.TimeRate.oneRenewalEveryTenSeconds](sktestsession/timerate-swift.enum/onerenewaleverytenseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 10 seconds.
- [SKTestSession.TimeRate.oneRenewalEveryTwoSeconds](sktestsession/timerate-swift.enum/onerenewaleverytwoseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 2 seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/timerate-swift.enum/onerenewaleveryminute)*