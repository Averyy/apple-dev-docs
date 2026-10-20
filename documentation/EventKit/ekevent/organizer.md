# organizer

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The organizer associated with the event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var organizer: EKParticipant? { get }
```

```objc
@property (nonatomic, readonly, nullable) EKParticipant * organizer;
```

#### Discussion

This property is `nil` if the event has no organizer.

## See Also

### Accessing Event Properties
- [var eventIdentifier: String!](./eventidentifier.md)
  A unique identifier for the event.
- [var availability: EKEventAvailability](./availability.md)
  The availability setting for the event.
- [var startDate: Date!](./startdate.md)
  The start date of the event.
- [var endDate: Date!](./enddate.md)
  The end date for the event.
- [var isAllDay: Bool](./isallday.md)
  A Boolean value that indicates whether the event is an all-day event.
- [var occurrenceDate: Date!](./occurrencedate.md)
  The original occurrence date of an event if it is part of a recurring series.
- [var isDetached: Bool](./isdetached.md)
  A Boolean value that indicates whether an event is a detached instance of a repeating event.
- [var status: EKEventStatus](./status.md)
  The status of the event.
- [var birthdayContactIdentifier: String?](./birthdaycontactidentifier.md)
  The contact identifier of the person for this birthday event.
- [var structuredLocation: EKStructuredLocation?](./structuredlocation.md)
  The event’s location with a potential geocoordinate.
- [var birthdayPersonID: Int](./birthdaypersonid.md)
  The Address Book framework record identifier of the person for this birthday event.
- [var birthdayPersonUniqueID: String?](./birthdaypersonuniqueid.md)
  The Address Book framework record identifier of the person for this birthday event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekevent/organizer)*