# DonationTimeRange

**Framework**: TipKit  
**Kind**: struct  
**Role**: Structure

A duration of time for filtering event donations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct DonationTimeRange
```

## Topics

### Type Properties
- [static var day: Tips.DonationTimeRange](./donationtimerange/day.md)
- [static var hour: Tips.DonationTimeRange](./donationtimerange/hour.md)
- [static var minute: Tips.DonationTimeRange](./donationtimerange/minute.md)
- [static var week: Tips.DonationTimeRange](./donationtimerange/week.md)
### Type Methods
- [static func days(Int) -> Tips.DonationTimeRange](./donationtimerange/days%28_%29.md)
- [static func hours(Int) -> Tips.DonationTimeRange](./donationtimerange/hours%28_%29.md)
- [static func minutes(Int) -> Tips.DonationTimeRange](./donationtimerange/minutes%28_%29.md)
- [static func weeks(Int) -> Tips.DonationTimeRange](./donationtimerange/weeks%28_%29.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Events
- [struct Event](./event.md)
  A repeatable user-defined action.
- [struct DonationLimit](./donationlimit.md)
  Specify the maximum number of donations for an event.
- [struct EmptyDonation](./emptydonation.md)
  An empty event donation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/donationtimerange)*