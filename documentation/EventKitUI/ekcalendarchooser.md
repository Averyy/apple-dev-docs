# EKCalendarChooser

**Framework**: EventKit UI  
**Kind**: class

A view controller for determining whether a user may select one or more calendars.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class EKCalendarChooser
```

#### Overview

Use the calendar chooser view controller to allow users to select one or more calendars when creating or editing a calendar event. The calendar chooser also lets you specify whether to display all calendars, or only those that may be written to. The view controller can be pushed on a navigation stack or presented modally.

Use a delegate that conforms to [`EKCalendarChooserDelegate`](ekcalendarchooserdelegate.md) to receive callbacks when the user selects calendars or cancels an operation.

## Topics

### Initializing Calendar Choosers
- [init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, eventStore: EKEventStore)](ekcalendarchooser/init(selectionstyle:displaystyle:eventstore:).md)
  Initializes a newly created calendar chooser.
- [init(selectionStyle: EKCalendarChooserSelectionStyle, displayStyle: EKCalendarChooserDisplayStyle, entityType: EKEntityType, eventStore: EKEventStore)](ekcalendarchooser/init(selectionstyle:displaystyle:entitytype:eventstore:).md)
  Initializes a newly created calendar chooser for a specific entity type.
### Managing Calendar Selection
- [var delegate: (any EKCalendarChooserDelegate)?](ekcalendarchooser/delegate.md)
  The calendar chooser’s delegate.
- [protocol EKCalendarChooserDelegate](ekcalendarchooserdelegate.md)
  Methods a calendar chooser’s delegate may use to receive notifications.
### Selecting a Calendar Type
- [var selectedCalendars: Set<EKCalendar>](ekcalendarchooser/selectedcalendars.md)
  The calendars selected by the user.
- [var selectionStyle: EKCalendarChooserSelectionStyle](ekcalendarchooser/selectionstyle.md)
  Determines whether to allow selection of multiple calendars.
- [enum EKCalendarChooserSelectionStyle](ekcalendarchooserselectionstyle.md)
  Indicates whether users may select a single calendar, or multiple calendars.
- [enum EKCalendarChooserDisplayStyle](ekcalendarchooserdisplaystyle.md)
  Indicates whether to display all calendars or writable calendars only.
### Changing the Appearance
- [var showsCancelButton: Bool](ekcalendarchooser/showscancelbutton.md)
  A Boolean that determines whether to display a Cancel button.
- [var showsDoneButton: Bool](ekcalendarchooser/showsdonebutton.md)
  A Boolean that determines whether to display a Done button.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/eventkitui/ekcalendarchooser)*