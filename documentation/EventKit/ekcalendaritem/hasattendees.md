# hasAttendees

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the calendar item has attendees.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasAttendees: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasAttendees;
```

#### Discussion

If [`true`](../../Swift/true.md), the calendar item has attendees; otherwise it does not.

## See Also

### Displaying Attendees
- [var attendees: [EKParticipant]?](./attendees.md)
  The attendees associated with the calendar item, as an array of [`EKParticipant`](../ekparticipant.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/hasattendees)*