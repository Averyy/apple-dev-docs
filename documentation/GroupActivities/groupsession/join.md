# join()

**Framework**: Group Activities  
**Kind**: method

Starts the shared activity on the current device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final func join()
```

## Mentions

- [Joining and managing a shared activity](joining-and-managing-a-shared-activity.md)
- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Discussion

Call this method to begin the delivery of synchronized data to the current device. Typically, you call this method when your app is ready to engage in an activity. For example, call it when you present your app’s UI for the activity. When your app successfully joins the session, the session changes the value in its [`state`](groupsession/state-swift.property.md) property to [`GroupSession.State.joined`](groupsession/state-swift.enum/joined.md).

## See Also

- [func leave()](groupsession/leave.md)
  Leaves the current activity and stops receiving synchronized data.
- [func end()](groupsession/end.md)
  Ends the activity for the entire group and stops the transfer of synchronized data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/join())*