# attendees

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The attendees associated with the calendar item, as an array of [`EKParticipant`](../ekparticipant.md) objects.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var attendees: [EKParticipant]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<__kindof EKParticipant *> * attendees;
```

## Discussion

This property is read-only; it is not possible to add attendees with Event Kit. This property is `nil` if the calendar item has no attendees.

## See Also

### Displaying Attendees
- [var hasAttendees: Bool](./hasattendees.md)
  A Boolean value that indicates whether the calendar item has attendees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/attendees)*