# eventStore

**Framework**: EventKit UI  
**Kind**: property

The event store used to save the event.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var eventStore: EKEventStore! { get set }
```

#### Discussion

This property must be set before displaying the view.

## See Also

- [var event: EKEvent?](ekeventeditviewcontroller/event.md)
  The event the user creates or edits using this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller/eventstore)*