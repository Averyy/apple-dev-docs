# EKParticipant

**Framework**: EventKit  
**Kind**: class

A class that represents person, group, or room invited to a calendar event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class EKParticipant
```

#### Overview

Do not create `EKParticipant` objects directly. Instead, use the property attendees on [`EKCalendarItem`](ekcalendaritem.md) to return an array of `EKParticipant` objects.

EventKit cannot add participants to an event nor change participant information. Use the properties in this class to get information about a participant.

A participant can be a person, group, room, or other resource.

## Topics

### Defining Participants
- [enum EKParticipantRole](ekparticipantrole.md)
  The participant’s role for an event.
- [enum EKParticipantType](ekparticipanttype.md)
  The type of participant.
- [enum EKParticipantStatus](ekparticipantstatus.md)
  The participant’s attendance status for an event.
- [enum EKParticipantScheduleStatus](ekparticipantschedulestatus.md)
  The participant’s scheduled status.
### Accessing Participant Properties
- [var isCurrentUser: Bool](ekparticipant/iscurrentuser.md)
  A Boolean value indicating whether this participant represents the owner of this account.
- [var name: String?](ekparticipant/name.md)
  The participant’s name.
- [var participantRole: EKParticipantRole](ekparticipant/participantrole.md)
  The participant’s role in the event.
- [var participantStatus: EKParticipantStatus](ekparticipant/participantstatus.md)
  The participant’s attendance status.
- [var participantType: EKParticipantType](ekparticipant/participanttype.md)
  The participant’s type.
- [var url: URL](ekparticipant/url.md)
  The URL representing this participant.
- [var contactPredicate: NSPredicate](ekparticipant/contactpredicate.md)
  A predicate to use with the Contacts framework to retrieve the corresponding contact instance.
### Finding Participant Address Book Records
- [func abRecord(with: ABAddressBook) -> ABRecord?](ekparticipant/abrecord(with:).md)
  Returns the address book record that represents the participant.
- [func abPerson(in: ABAddressBook) -> ABPerson?](ekparticipant/abperson(in:).md)
  Returns the address book record that represents the participant.
- [typealias ABAddressBook](abaddressbook.md)
  A reference to an ABAddressBook object.
- [typealias ABRecord](abrecord.md)
  A reference to an ABRecord object or any of its derivedopaque types.

## Relationships

### Inherits From
- [EKObject](ekobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class EKCalendar](ekcalendar.md)
  A class that represents a calendar in EventKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekparticipant)*