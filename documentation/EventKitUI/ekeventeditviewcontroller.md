# EKEventEditViewController

**Framework**: EventKit UI  
**Kind**: class  
**Role**: Class

A view controller for creating, editing, and deleting calendar events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class EKEventEditViewController
```

```objc
@interface EKEventEditViewController : UINavigationController
```

#### Overview

Presented modally, the event edit view controller provides a way for users to add new events, as well as edit or delete events from their calendar. New events are added to the user’s default calendar unless they choose another calendar in the UI.

The controller includes delegates to receive a notification when the user saves an edit or deletes an event, or cancels from an edit session. The delegate must conform to [`EKEventEditViewDelegate`](./ekeventeditviewdelegate.md).

## Topics

### Managing the Event Editing Interface
- [var editViewDelegate: (any EKEventEditViewDelegate)?](./ekeventeditviewcontroller/editviewdelegate.md)
  The delegate to notify when editing an event.
- [protocol EKEventEditViewDelegate](./ekeventeditviewdelegate.md)
  A notification sent to the delegate when the user finishes editing an event.
### Creating and Saving Events
- [var event: EKEvent?](./ekeventeditviewcontroller/event.md)
  The event the user creates or edits using this view controller.
- [var eventStore: EKEventStore!](./ekeventeditviewcontroller/eventstore.md)
  The event store used to save the event.
### Canceling Edits to Events
- [func cancelEditing()](./ekeventeditviewcontroller/cancelediting%28%29.md)
  Ends the editing session and discards any changes that were made to the event.

## Relationships

### Inherits From
- [UINavigationController](../UIKit/uinavigationcontroller.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller)*