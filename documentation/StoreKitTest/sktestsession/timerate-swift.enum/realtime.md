# SKTestSession.TimeRate.realTime

**Framework**: StoreKit Test  
**Kind**: case

A rate of time in which the test environment runs in real time.

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
case realTime
```

#### Discussion

With this time rate, subscriptions in the testing environment renew in real time. For example, a weekly subscription renews in one week.

The time rate also affects the billing grace period and the billing retry period in the testing environment. The table below shows the real-time rates:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 6 days |
| Grace period for subscriptions with all other renewal periods | 16 days |
| Billing retry period | 60 days |

## See Also

- [SKTestSession.TimeRate.monthlyRenewalEveryHour](sktestsession/timerate-swift.enum/monthlyrenewaleveryhour.md)
  A rate of time in the test environment in which monthly subscriptions renew every hour.
- [SKTestSession.TimeRate.monthlyRenewalEveryThirtyMinutes](sktestsession/timerate-swift.enum/monthlyrenewaleverythirtyminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 30 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryFifteenMinutes](sktestsession/timerate-swift.enum/monthlyrenewaleveryfifteenminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 15 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryFiveMinutes](sktestsession/timerate-swift.enum/monthlyrenewaleveryfiveminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 5 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryThirtySeconds](sktestsession/timerate-swift.enum/monthlyrenewaleverythirtyseconds.md)
  A rate of time in the test environment in which monthly subscriptions renew every 30 seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/timerate-swift.enum/realtime)*