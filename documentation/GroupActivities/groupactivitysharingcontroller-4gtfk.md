# GroupActivitySharingController

**Framework**: Group Activities  
**Kind**: class

A macOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@objc class GroupActivitySharingController
```

#### Overview

A [`GroupActivitySharingController`](groupactivitysharingcontroller-4gtfk.md) helps you start a SharePlay activity, even when a FaceTime call isn’t currently active. When presented, the view controller prompts the person to start the activity you provided. If no FaceTime call is active, the view controller also displays a people picker to let the person select the participants for the activity. When they choose to start the activity, the view controller automatically starts the FaceTime call as needed and joins your app to the activity.

If your app’s interface includes controls to start SharePlay activities, present this view controller in response to interactions with those controls. Initialize the [`GroupActivitySharingController`](groupactivitysharingcontroller-4gtfk.md) object with the activity you want to start. After you present it, the view controller handles all further interactions. It manages the interface that appears onscreen and responds when someone chooses to start or cancel the activity. It starts the FaceTime call if one isn’t currently active. It also dismisses itself and returns control back to your app, updating its [`result`](groupactivitysharingcontroller-4gtfk/result.md) property to let you know what happened.

## Topics

### Creating the group activity sharing controller
- [init<ActivityType>(ActivityType) throws](groupactivitysharingcontroller-4gtfk/init(_:).md)
  Initializes the sharing controller with the specified activity and type information.
- [init<ActivityType>(preparationHandler: () async throws -> ActivityType)](groupactivitysharingcontroller-4gtfk/init(preparationhandler:).md)
  Initializes the SharePlay sharing controller with a closure that creates the activity object.
### Getting the result
- [var result: GroupActivitySharingResult](groupactivitysharingcontroller-4gtfk/result.md)
  The result of a request to share a group activity.
- [enum GroupActivitySharingResult](groupactivitysharingresult-1gln2.md)
  The result of a request to share a group activity in macOS.
### Responding to view-related events
- [func viewDidLoad()](groupactivitysharingcontroller-4gtfk/viewdidload.md)
  Notifies the view controller that the system added a view to a view hierarchy.
### Instance Methods
- [func loadView()](groupactivitysharingcontroller-4gtfk/loadview.md)
- [func viewWillAppear()](groupactivitysharingcontroller-4gtfk/viewwillappear.md)
  Notifies the view controller that the system is going to add a view to a view hierarchy.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)

## See Also

- [Presenting SharePlay activities from your app’s UI](promoting-shareplay-activities-from-your-apps-ui.md)
  Make it easy for people to start activities from your app’s UI, from the system share sheet, or using AirPlay over AirDrop.
- [class GroupActivitySharingController](groupactivitysharingcontroller-ybcy.md)
  An iOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitysharingcontroller-4gtfk)*