# GroupActivitySharingController

**Framework**: Group Activities  
**Kind**: class  
**Role**: Class

An iOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@objc class GroupActivitySharingController
```

#### Overview

A [`GroupActivitySharingController`](./groupactivitysharingcontroller-ybcy.md) helps you start a SharePlay activity, even when a FaceTime call isn’t currently active. When presented, the view controller prompts the person to start the activity you provided. If no FaceTime call is active, the view controller also displays a people picker to let the person select the participants for the activity. When they choose to start the activity, the view controller automatically starts the FaceTime call as needed and joins your app to the activity.

If your app’s interface includes controls to start SharePlay activities, present this view controller in response to interactions with those controls. Initialize the [`GroupActivitySharingController`](./groupactivitysharingcontroller-ybcy.md) object with the activity you want to start. After you present it, the view controller handles all further interactions. It manages the interface that appears onscreen and responds when someone chooses to start or cancel the activity. It starts the FaceTime call if one isn’t currently active. It also dismisses itself and returns control back to your app, updating its [`result`](./groupactivitysharingcontroller-ybcy/result.md) property to let you know what happened.

## Topics

### Creating the group activity sharing controller
- [init<ActivityType>(ActivityType) throws](./groupactivitysharingcontroller-ybcy/init%28_%29.md)
  Initializes the sharing controller with the specified activity and type information.
- [init<ActivityType>(preparationHandler: () async throws -> ActivityType)](./groupactivitysharingcontroller-ybcy/init%28preparationhandler%29.md)
  Initializes the SharePlay sharing controller with a closure that creates the activity object.
### Getting the result
- [var result: GroupActivitySharingResult](./groupactivitysharingcontroller-ybcy/result.md)
  The result of a request to share a group activity.
- [enum GroupActivitySharingResult](./groupactivitysharingresult-2ijfu.md)
  The result of a request to share a group activity in iOS.
### Responding to view-related events
- [func viewDidLoad()](./groupactivitysharingcontroller-ybcy/viewdidload%28%29.md)
  Notifies the view controller that the system added a view to a view hierarchy.
- [func viewWillAppear(Bool)](./groupactivitysharingcontroller-ybcy/viewwillappear%28_%29.md)
  Notifies the view controller that the system is going to add a view to a view hierarchy.
### Instance Properties
- [var modalPresentationStyle: UIModalPresentationStyle](./groupactivitysharingcontroller-ybcy/modalpresentationstyle.md)
  The presentation style for the view controller.
- [var preferredContainerBackgroundStyle: UIContainerBackgroundStyle](./groupactivitysharingcontroller-ybcy/preferredcontainerbackgroundstyle.md)

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Interface presentation
- [Presenting SharePlay activities from your app’s UI](./promoting-shareplay-activities-from-your-apps-ui.md)
  Make it easy for people to start activities from your app’s UI, from the system share sheet, or using AirPlay over AirDrop.
- [class GroupActivitySharingController](./groupactivitysharingcontroller-4gtfk.md)
  A macOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitysharingcontroller-ybcy)*