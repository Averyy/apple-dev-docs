# status

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) EKEventStatus status;
```

## Discussion

You should act based on an event’s status only if the status is [`EKEventStatus.canceled`](../ekeventstatus/canceled.md), which indicates that the event has been canceled. Other statuses should be considered informational.

## See Also

### Related Documentation
- [enum EKEventStatus](../ekeventstatus.md)
  The event’s status.
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
- [var organizer: EKParticipant?](./organizer.md)
  The organizer associated with the event.
- [var birthdayContactIdentifier: String?](./birthdaycontactidentifier.md)
  The contact identifier of the person for this birthday event.
- [var structuredLocation: EKStructuredLocation?](./structuredlocation.md)
  The event’s location with a potential geocoordinate.
- [var birthdayPersonID: Int](./birthdaypersonid.md)
  The Address Book framework record identifier of the person for this birthday event.
- [var birthdayPersonUniqueID: String?](./birthdaypersonuniqueid.md)
  The Address Book framework record identifier of the person for this birthday event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekevent/status)*