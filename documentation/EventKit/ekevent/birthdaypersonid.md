# birthdayPersonID

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The Address Book framework record identifier of the person for this birthday event.

**Availability**:
- iOS 5.0+ - Deprecated in 9.0
- iPadOS 5.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use birthdayContactIdentifier instead

## Declaration

```swift
var birthdayPersonID: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger birthdayPersonID;
```

#### Discussion

This property is only set if this is a birthday event; otherwise the property is `nil`.

##### Special Considerations

> **Note**:  This property is equivalent to the [`birthdayPersonUniqueID`](./birthdaypersonuniqueid.md) property in macOS.

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
- [var organizer: EKParticipant?](./organizer.md)
  The organizer associated with the event.
- [var status: EKEventStatus](./status.md)
  The status of the event.
- [var birthdayContactIdentifier: String?](./birthdaycontactidentifier.md)
  The contact identifier of the person for this birthday event.
- [var structuredLocation: EKStructuredLocation?](./structuredlocation.md)
  The event’s location with a potential geocoordinate.
- [var birthdayPersonUniqueID: String?](./birthdaypersonuniqueid.md)
  The Address Book framework record identifier of the person for this birthday event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekevent/birthdaypersonid)*