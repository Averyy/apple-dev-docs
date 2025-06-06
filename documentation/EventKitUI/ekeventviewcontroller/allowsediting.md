# allowsEditing

**Framework**: EventKit UI  
**Kind**: property

A Boolean that determines whether the user may edit the event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsEditing: Bool { get set }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false) (the default), the event is not editable. If [`true`](https://developer.apple.com/documentation/swift/true), an Edit button appears, allowing the user to change properties of the event. This property applies only to events in calendars created by the user. For example, it doesn’t apply to invitations sent by another user.

## See Also

- [var allowsCalendarPreview: Bool](ekeventviewcontroller/allowscalendarpreview.md)
  A Boolean that determines whether the user can preview the event in a calendar day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller/allowsediting)*