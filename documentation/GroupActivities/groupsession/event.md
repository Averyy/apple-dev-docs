# GroupSession.Event

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

A session-related event to display in the system UI.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Event
```

Available when `ActivityType` conforms to `GroupActivity`.

#### Overview

Use this structure to specify the contents of custom activity-related events. The AV Foundation framework posts media-related events to the system on your app’s behalf; create an instance of this structure if your app posts additional events that don’t route through AV Foundation.

After creating an instance of this structure, post it to the system using the [`showNotice(_:)`](./shownotice%28_%29.md) method of [`GroupSession`](../groupsession.md).

## Topics

### Getting the event details
- [let originator: Participant](./event/originator.md)
  The participant that initiated the event.
### Initializers
- [init(originator: Participant, localizedDescription: String)](./event/init%28originator,localizeddescription%29.md)
### Instance Properties
- [var localizedDescription: String](./event/localizeddescription.md)
  A localized description of the event


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/event)*