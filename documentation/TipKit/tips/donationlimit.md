# DonationLimit

**Framework**: TipKit  
**Kind**: struct  
**Role**: Structure

Specify the maximum number of donations for an event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct DonationLimit
```

## Topics

### Initializers
- [init(maximumCount: Int, maximumAge: Tips.DonationTimeRange?)](./donationlimit/init%28maximumcount,maximumage%29.md)
  Passed to an `Event` to specify the maximum number and maximum age of donations the event will persist and query.
### Instance Properties
- [let maximumAge: Tips.DonationTimeRange?](./donationlimit/maximumage.md)
  Maximum age of donations this event will persist and query. By default events have no maximum age.
- [let maximumCount: Int](./donationlimit/maximumcount.md)
  Maximum number of donations this event will persist and query.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Events
- [struct Event](./event.md)
  A repeatable user-defined action.
- [struct DonationTimeRange](./donationtimerange.md)
  A duration of time for filtering event donations.
- [struct EmptyDonation](./emptydonation.md)
  An empty event donation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/donationlimit)*