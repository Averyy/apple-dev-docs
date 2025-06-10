# EKEventEditViewController

**Framework**: EventKit UI  
**Kind**: class

A view controller for creating, editing, and deleting calendar events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class EKEventEditViewController
```

#### Overview

Presented modally, the event edit view controller provides a way for users to add new events, as well as edit or delete events from their calendar. New events are added to the user’s default calendar unless they choose another calendar in the UI.

The controller includes delegates to receive a notification when the user saves an edit or deletes an event, or cancels from an edit session. The delegate must conform to [`EKEventEditViewDelegate`](ekeventeditviewdelegate.md).

## Topics

### Managing the Event Editing Interface
- [var editViewDelegate: (any EKEventEditViewDelegate)?](ekeventeditviewcontroller/editviewdelegate.md)
  The delegate to notify when editing an event.
- [protocol EKEventEditViewDelegate](ekeventeditviewdelegate.md)
  A notification sent to the delegate when the user finishes editing an event.
### Creating and Saving Events
- [var event: EKEvent?](ekeventeditviewcontroller/event.md)
  The event the user creates or edits using this view controller.
- [var eventStore: EKEventStore!](ekeventeditviewcontroller/eventstore.md)
  The event store used to save the event.
### Canceling Edits to Events
- [func cancelEditing()](ekeventeditviewcontroller/cancelediting.md)
  Ends the editing session and discards any changes that were made to the event.

## Relationships

### Inherits From
- [UINavigationController](../UIKit/UINavigationController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekeventeditviewcontroller)*