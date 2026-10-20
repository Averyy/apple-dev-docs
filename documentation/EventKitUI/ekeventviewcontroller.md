# EKEventViewController

**Framework**: EventKit UI  
**Kind**: class  
**Role**: Class

A view controller for displaying existing calendar and reminder events, and for optionally editing those events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class EKEventViewController
```

```objc
@interface EKEventViewController : UIViewController
```

#### Overview

The event view controller’s primary purpose is to present to the user a modal display containing the details of a calendar event. The view controller lets you set whether users may edit an event and, if the event is an invitation and the organizer is not the user, you can decide whether to show a preview of the event.

The event view controller includes delegates used to receive a notification when closing the view controller. The delegate must conform to the [`EKEventViewDelegate`](./ekeventviewdelegate.md) protocol.

## Topics

### Dismissing the Event Interface
- [var delegate: (any EKEventViewDelegate)?](./ekeventviewcontroller/delegate.md)
  The event view controller’s delegate.
- [protocol EKEventViewDelegate](./ekeventviewdelegate.md)
  Delegates used to display details for calendar events.
### Getting and Setting the Event
- [var event: EKEvent!](./ekeventviewcontroller/event.md)
  The event this view controller displays to the user.
### Displaying and Editing Event Previews
- [var allowsCalendarPreview: Bool](./ekeventviewcontroller/allowscalendarpreview.md)
  A Boolean that determines whether the user can preview the event in a calendar day.
- [var allowsEditing: Bool](./ekeventviewcontroller/allowsediting.md)
  A Boolean that determines whether the user may edit the event.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventviewcontroller)*