# structuredLocation

**Framework**: EventKit  
**Kind**: property

The event’s location with a potential geocoordinate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var structuredLocation: EKStructuredLocation? { get set }
```

## See Also

- [var eventIdentifier: String!](ekevent/eventidentifier.md)
  A unique identifier for the event.
- [var availability: EKEventAvailability](ekevent/availability.md)
  The availability setting for the event.
- [var startDate: Date!](ekevent/startdate.md)
  The start date of the event.
- [var endDate: Date!](ekevent/enddate.md)
  The end date for the event.
- [var isAllDay: Bool](ekevent/isallday.md)
  A Boolean value that indicates whether the event is an all-day event.
- [var occurrenceDate: Date!](ekevent/occurrencedate.md)
  The original occurrence date of an event if it is part of a recurring series.
- [var isDetached: Bool](ekevent/isdetached.md)
  A Boolean value that indicates whether an event is a detached instance of a repeating event.
- [var organizer: EKParticipant?](ekevent/organizer.md)
  The organizer associated with the event.
- [var status: EKEventStatus](ekevent/status.md)
  The status of the event.
- [var birthdayContactIdentifier: String?](ekevent/birthdaycontactidentifier.md)
  The contact identifier of the person for this birthday event.
- [var birthdayPersonID: Int](ekevent/birthdaypersonid.md)
  The Address Book framework record identifier of the person for this birthday event.
- [var birthdayPersonUniqueID: String?](ekevent/birthdaypersonuniqueid.md)
  The Address Book framework record identifier of the person for this birthday event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekevent/structuredlocation)*