# SKTestSession.TimeRate.monthlyRenewalEveryThirtyMinutes

**Framework**: StoreKit Test  
**Kind**: case

A rate of time in the test environment in which monthly subscriptions renew every 30 minutes.

**Availability**:
- iOS 15.2+
- iPadOS 15.2+
- Mac Catalyst 15.2+
- macOS 12.1+
- tvOS 15.2+
- visionOS 1.0+
- watchOS 8.3+

## Declaration

```swift
case monthlyRenewalEveryThirtyMinutes
```

#### Discussion

The following table shows how this time rate affects subscriptions with various renewal periods in the testing environment:

| Subscription renewal period | Renewal time |
| --- | --- |
| Weekly | 10 minutes |
| Monthly | 30 minutes |
| Bimonthly | 1 hour |
| Quarterly | 1 hour 30 minutes |
| Semiannually | 3 hours |
| Annually | 6 hours |

The sandbox environment also supports this subscription renewal rate. For more information about renewal rates in the sandbox environment, see [`Test in-app purchases`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev7e89e149d).

The time rate also affects the billing grace period and the billing retry period in the testing environment, as the table below shows:

| Type | Time period |
| --- | --- |
| Grace period for subscriptions with a weekly renewal period | 8 minutes 34 seconds |
| Grace period for subscriptions with all other renewal periods | 15 minutes |
| Billing retry period | 1 hour |

## See Also

- [SKTestSession.TimeRate.realTime](sktestsession/timerate-swift.enum/realtime.md)
  A rate of time in which the test environment runs in real time.
- [SKTestSession.TimeRate.monthlyRenewalEveryHour](sktestsession/timerate-swift.enum/monthlyrenewaleveryhour.md)
  A rate of time in the test environment in which monthly subscriptions renew every hour.
- [SKTestSession.TimeRate.monthlyRenewalEveryFifteenMinutes](sktestsession/timerate-swift.enum/monthlyrenewaleveryfifteenminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 15 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryFiveMinutes](sktestsession/timerate-swift.enum/monthlyrenewaleveryfiveminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 5 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryThirtySeconds](sktestsession/timerate-swift.enum/monthlyrenewaleverythirtyseconds.md)
  A rate of time in the test environment in which monthly subscriptions renew every 30 seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/timerate-swift.enum/monthlyrenewaleverythirtyminutes)*