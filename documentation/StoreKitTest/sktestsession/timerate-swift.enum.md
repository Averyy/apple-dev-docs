# SKTestSession.TimeRate

**Framework**: StoreKit Test  
**Kind**: enum  
**Role**: Enumeration

The values for rates of time passing in the test environment.

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
enum TimeRate
```

```c
enum SKTestTimeRate : NSInteger;
```

#### Overview

The time rates that affect subscription renewals in the test environment match those in the sandbox environment with these exceptions:

- Only the test environment supports the [`SKTestSession.TimeRate.monthlyRenewalEveryThirtySeconds`](./timerate-swift.enum/monthlyrenewaleverythirtyseconds.md) time rate.
- Only the test environment supports the fixed time rate options: [`SKTestSession.TimeRate.oneRenewalEveryFifteenMinutes`](./timerate-swift.enum/onerenewaleveryfifteenminutes.md), [`SKTestSession.TimeRate.oneRenewalEveryFiveMinutes`](./timerate-swift.enum/onerenewaleveryfiveminutes.md), [`SKTestSession.TimeRate.oneRenewalEveryMinute`](./timerate-swift.enum/onerenewaleveryminute.md), [`SKTestSession.TimeRate.oneRenewalEveryThirtySeconds`](./timerate-swift.enum/onerenewaleverythirtyseconds.md), [`SKTestSession.TimeRate.oneRenewalEveryTenSeconds`](./timerate-swift.enum/onerenewaleverytenseconds.md), and [`SKTestSession.TimeRate.oneRenewalEveryTwoSeconds`](./timerate-swift.enum/onerenewaleverytwoseconds.md).
- Only the sandbox environment supports a monthly renewal in 3 minutes.

For more information about time rates in the sandbox environment, see [Test Apple In-App Purchases](https://developer.apple.com/help/app-store-connect/test-in-app-purchases-main/test-in-app-purchases).

The time rates also affect the lengths of the billing retry period and the billing grace period in the testing environment. See the individual enumeration cases for the actual time values of the subscription renewal rates, billing retry periods, and billing grace periods.

## Topics

### Fixed time rates for subscription renewals
- [SKTestSession.TimeRate.oneRenewalEveryFifteenMinutes](./timerate-swift.enum/onerenewaleveryfifteenminutes.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 15 minutes.
- [SKTestSession.TimeRate.oneRenewalEveryFiveMinutes](./timerate-swift.enum/onerenewaleveryfiveminutes.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 5 minutes.
- [SKTestSession.TimeRate.oneRenewalEveryMinute](./timerate-swift.enum/onerenewaleveryminute.md)
  A rate of time in the test environment in which subscriptions of any time length renew every minute.
- [SKTestSession.TimeRate.oneRenewalEveryThirtySeconds](./timerate-swift.enum/onerenewaleverythirtyseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 30 seconds.
- [SKTestSession.TimeRate.oneRenewalEveryTenSeconds](./timerate-swift.enum/onerenewaleverytenseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 10 seconds.
- [SKTestSession.TimeRate.oneRenewalEveryTwoSeconds](./timerate-swift.enum/onerenewaleverytwoseconds.md)
  A rate of time in the test environment in which subscriptions of any time length renew every 2 seconds.
### Scaled time rates for subscription renewals
- [SKTestSession.TimeRate.realTime](./timerate-swift.enum/realtime.md)
  A rate of time in which the test environment runs in real time.
- [SKTestSession.TimeRate.monthlyRenewalEveryHour](./timerate-swift.enum/monthlyrenewaleveryhour.md)
  A rate of time in the test environment in which monthly subscriptions renew every hour.
- [SKTestSession.TimeRate.monthlyRenewalEveryThirtyMinutes](./timerate-swift.enum/monthlyrenewaleverythirtyminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 30 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryFifteenMinutes](./timerate-swift.enum/monthlyrenewaleveryfifteenminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 15 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryFiveMinutes](./timerate-swift.enum/monthlyrenewaleveryfiveminutes.md)
  A rate of time in the test environment in which monthly subscriptions renew every 5 minutes.
- [SKTestSession.TimeRate.monthlyRenewalEveryThirtySeconds](./timerate-swift.enum/monthlyrenewaleverythirtyseconds.md)
  A rate of time in the test environment in which monthly subscriptions renew every 30 seconds.
### Deprecated
- [SKTestSession.TimeRate.oneHourIsOneDay](./timerate-swift.enum/onehourisoneday.md)
  A rate of time in which 1 hour in the test environment represents one day.
- [SKTestSession.TimeRate.thirtyMinutesIsOneDay](./timerate-swift.enum/thirtyminutesisoneday.md)
  A rate of time in which 30 minutes in the test environment represents one day.
- [SKTestSession.TimeRate.fiveMinutesIsOneDay](./timerate-swift.enum/fiveminutesisoneday.md)
  A rate of time in which 5 minutes in the test environment represents one day.
- [SKTestSession.TimeRate.oneMinuteIsOneDay](./timerate-swift.enum/oneminuteisoneday.md)
  A rate of time in which 1 minute in the test environment represents one day.
- [SKTestSession.TimeRate.thirtySecondsIsOneDay](./timerate-swift.enum/thirtysecondsisoneday.md)
  A rate of time in which 30 seconds in the test environment represents one day.
- [SKTestSession.TimeRate.oneSecondIsOneDay](./timerate-swift.enum/onesecondisoneday.md)
  A rate of time in which 1 second in the test environment represents one day.
### Initializers
- [init?(rawValue: Int)](./timerate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Testing subscription renewals
- [var timeRate: SKTestSession.TimeRate](./timerate-swift.property.md)
  The rate at which time passes for subscriptions in the test environment as compared to real time.
- [func enableAutoRenewForTransaction(identifier: Int) throws](./enableautorenewfortransaction%28identifier%29.md)
  Enables auto-renewing for an auto-renewable subscription in the test environment.
- [func disableAutoRenewForTransaction(identifier: Int) throws](./disableautorenewfortransaction%28identifier%29.md)
  Disables auto-renewing for an auto-renewable subscription in the test environment.
- [func forceRenewalOfSubscription(productIdentifier: String) throws](./forcerenewalofsubscription%28productidentifier%29.md)
  Ends the previous subscription period and begins the next period in the test environment.
- [func expireSubscription(productIdentifier: String) throws](./expiresubscription%28productidentifier%29.md)
  Causes the identified auto-renewable subscription to expire immediately in the test environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktestsession/timerate-swift.enum)*