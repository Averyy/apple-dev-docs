# DonationLimit

**Framework**: TipKit  
**Kind**: struct

Specify the maximum number of donations for an event.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct DonationLimit
```

## Topics

### Initializers
- [init(maximumCount: Int, maximumAge: Tips.DonationTimeRange?)](tips/donationlimit/init(maximumcount:maximumage:).md)
  Passed to an `Event` to specify the maximum number and maximum age of donations the event will persist and query.
### Instance Properties
- [let maximumAge: Tips.DonationTimeRange?](tips/donationlimit/maximumage.md)
  Maximum age of donations this event will persist and query. By default events have no maximum age.
- [let maximumCount: Int](tips/donationlimit/maximumcount.md)
  Maximum number of donations this event will persist and query.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Event](tips/event.md)
  A repeatable user-defined action.
- [struct DonationTimeRange](tips/donationtimerange.md)
  A duration of time for filtering event donations.
- [struct EmptyDonation](tips/emptydonation.md)
  An empty event donation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/donationlimit)*