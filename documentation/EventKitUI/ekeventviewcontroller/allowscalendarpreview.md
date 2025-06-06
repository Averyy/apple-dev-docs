# allowsCalendarPreview

**Framework**: EventKit UI  
**Kind**: property

A Boolean that determines whether the user can preview the event in a calendar day.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsCalendarPreview: Bool { get set }
```

#### Discussion

If the event is an invitation and this property is [`true`](https://developer.apple.com/documentation/swift/true), then a table cell appears allowing the user to preview the event along with other events on the same day. If [`false`](https://developer.apple.com/documentation/swift/false) (the default), the calendar day preview does not appear. This property applies only to invitations.

## See Also

- [var allowsEditing: Bool](ekeventviewcontroller/allowsediting.md)
  A Boolean that determines whether the user may edit the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller/allowscalendarpreview)*