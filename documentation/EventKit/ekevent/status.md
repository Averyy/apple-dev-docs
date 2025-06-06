# status

**Framework**: EventKit  
**Kind**: property

The status of the event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var status: EKEventStatus { get }
```

#### Discussion

You should act based on an event’s status only if the status is [`EKEventStatus.canceled`](ekeventstatus/canceled.md), which indicates that the event has been canceled. Other statuses should be considered informational.

## See Also

- [enum EKEventStatus](ekeventstatus.md)
  The event’s status.
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
- [var birthdayContactIdentifier: String?](ekevent/birthdaycontactidentifier.md)
  The contact identifier of the person for this birthday event.
- [var structuredLocation: EKStructuredLocation?](ekevent/structuredlocation.md)
  The event’s location with a potential geocoordinate.
- [var birthdayPersonID: Int](ekevent/birthdaypersonid.md)
  The Address Book framework record identifier of the person for this birthday event.
- [var birthdayPersonUniqueID: String?](ekevent/birthdaypersonuniqueid.md)
  The Address Book framework record identifier of the person for this birthday event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekevent/status)*