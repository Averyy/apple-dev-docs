# init(maximumCount:maximumAge:)

**Framework**: TipKit  
**Kind**: init

Passed to an `Event` to specify the maximum number and maximum age of donations the event will persist and query.

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
init(maximumCount: Int, maximumAge: Tips.DonationTimeRange? = nil)
```

## Parameters

- `maximumCount`: Maximum number of donations this event will persist and query.
- `maximumAge`: Maximum age of donations this event will persist and query. By default events have no maximum age.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tips/donationlimit/init(maximumcount:maximumage:))*