# SKTestSession.TimeRate.oneRenewalEveryFifteenMinutes

**Framework**: StoreKit Test  
**Kind**: case  
**Role**: Case

A rate of time in the test environment in which subscriptions of any time length renew every 15 minutes.

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
case oneRenewalEveryFifteenMinutes
```

```c
SKTestTimeRateOneRenewalEveryFifteenMinutes
```

#### Discussion

This time rate renews subscriptions every fifteen minutes in the testing environment, regardless of actual renewal periods for each subscription.

The sandbox environment does not support this subscription renewal rate.

This time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time Period |
| --- | --- |
| Grace period for subscriptions with all renewal periods | 15 minutes |
| Billing retry period | 30 minutes |

## See Also

### Fixed time rates for subscription renewals
- [SKTestSession.TimeRate.oneRenewalEveryFiveMinutes](./onerenewaleveryfiveminutes.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 5 minutes.
- [SKTestSession.TimeRate.oneRenewalEveryMinute](./onerenewaleveryminute.md)
  A rate of time in the test environment in which subscriptions of any time length renew every minute.
- [SKTestSession.TimeRate.oneRenewalEveryThirtySeconds](./onerenewaleverythirtyseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 30 seconds.
- [SKTestSession.TimeRate.oneRenewalEveryTenSeconds](./onerenewaleverytenseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 10 seconds.
- [SKTestSession.TimeRate.oneRenewalEveryTwoSeconds](./onerenewaleverytwoseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 2 seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/timerate-swift.enum/onerenewaleveryfifteenminutes)*