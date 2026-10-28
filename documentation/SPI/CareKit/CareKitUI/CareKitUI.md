---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui"
framework: "CareKit/CareKitUI"
---

# CareKitUI

**Framework**: CareKit/CareKitUI  
**Kind**: module  
**Role**: Framework

Manage and display patient care data on your app.

## Overview

CareKitUI provides the views that you use to display patient care data. The views are open and extensible subclasses of https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/uikit/uiview. Properties within the views are public and give you full control over the content.

## Topics

### Single care tasks
- [struct SimpleTaskView](./simpletaskview.md)
  A card that displays a header view and a completion view. The whole view is tappable.
- [class OCKSimpleTaskView](./ocksimpletaskview.md)
  A card that displays an `OCKHeaderView` and a circular checkmark button `completionButton`. In CareKit, this view is intended to display a particular event for a task. The state of the `completionButton` indicates the completion state of the event.
- [struct InstructionsTaskView](./instructionstaskview.md)
  A card that displays a header view, multi-line label, and a completion button.
- [class OCKInstructionsTaskView](./ockinstructionstaskview.md)
  A card that displays a header, multi-line label, and a completion button.
- [struct CircularCompletionView](./circularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state. The circle will encompass the frame of the provided `content`. To ensure the content is contained within the circle, make sure the content has a square frame.
- [class OCKCheckmarkButton](./ockcheckmarkbutton.md)
  A button that shows a checkmark in the selected state, and an empty ring in the deselected state.
- [struct RectangularCompletionView](./rectangularcompletionview.md)
  A view that denotes a completion state. The style of the view differs based on the completion state.
### Multiple care tasks
- [class OCKGridTaskView](./ockgridtaskview.md)
  A card that displays a header, grid of buttons, and a multi-line label In CareKit, this view is intended to display multiple events for a particular task. The state of each button in the grid indicates the completion state of the corresponding event.
- [class OCKChecklistTaskView](./ockchecklisttaskview.md)
  A card that displays a vertically stacked checklist of items. In CareKit, this view is intended to display multiple events for a particular task.
- [class OCKChecklistItemButton](./ockchecklistitembutton.md)
  A button with an icon and title label.
- [class OCKGridTaskCell](./ockgridtaskcell.md)
  A cell used in the `collectionView` of the `OCKGridTaskView`. The cell shows a circular `completionButton` that has an image and a `titleLabel`. The default image is a checkmark.
- [class OCKLabeledCheckmarkButton](./ocklabeledcheckmarkbutton.md)
  OCKCheckmarkButton button with a label.
### Log-based care tasks
- [class OCKButtonLogTaskView](./ockbuttonlogtaskview.md)
  A card that displays a header, multi-line label, a collection of log buttons, and a dynamic vertical stack of logged items. In CareKit, this view is intended to display a particular event for a task. When the log button is presses, a new outcome is created for the event.
- [class OCKLogTaskView](./ocklogtaskview.md)
  Base class for all log view. Shows an `OCKHeaderView` and a dynamic stack view of log items.
- [class OCKLogButtonCell](./ocklogbuttoncell.md)
- [class OCKLogItemButton](./ocklogitembutton.md)
### Read-only care tasks
- [struct NumericProgressTaskView](./numericprogresstaskview.md)
  A card that displays a header, instructions, and indicators for progress and goal values.
- [struct LabeledValueTaskView](./labeledvaluetaskview.md)
  A card that displays a header and a labeled value.
- [enum LabeledValueTaskViewStatus](./labeledvaluetaskviewstatus.md)
  The  status denoted by a `LabeledValueTaskView`.
### Care task details
- [class OCKDetailView](./ockdetailview.md)
  A scrollable view with an image header and text content.
### Contacts
- [class OCKSimpleContactView](./ocksimplecontactview.md)
  A card that displays information for a contact. The header is an `OCKHeaderView`.
- [class OCKDetailedContactView](./ockdetailedcontactview.md)
  A card that displays information for a contact.
- [class OCKAddressButton](./ockaddressbutton.md)
- [class OCKContactButton](./ockcontactbutton.md)
### Charts
- [class OCKCartesianChartView](./ockcartesianchartview.md)
- [class OCKCartesianGraphView](./ockcartesiangraphview.md)
  A view that displays a graphable view above an axis.
- [struct OCKDataSeries](./ockdataseries.md)
  Represents a single group of data to be plotted. In most cases, CareKit plots accept multiple data series, allowing for for several data series to be plotted on a single axis for easy comparison.
### Calendar
- [class OCKWeekCalendarView](./ockweekcalendarview.md)
  A horizontal row of seven selectable completion rings and corresponding labels.
- [class OCKCompletionRingButton](./ockcompletionringbutton.md)
  A selectable completion ring with an inner check view and a title label.
- [class OCKCompletionRingView](./ockcompletionringview.md)
  A fillable ring with an inner checkmark.
- [enum OCKCompletionState](./ockcompletionstate.md)
  A completion state that marks progress.
### Links
- [struct LinkView](./linkview.md)
  A card that displays multiple link buttons. Links buttons are capable of showing content in or out of app. Link buttons can be configured using a `Link`.
- [enum LinkItem](./linkitem.md)
  A link item tied to a button in the `LinkView`.
### Featured content
- [class OCKFeaturedContentView](./ockfeaturedcontentview.md)
  A card that displays a large background image.
- [protocol OCKFeaturedContentViewDelegate](./ockfeaturedcontentviewdelegate.md)
  Handles events for an `OCKFeaturedContentView`.
### Common view components
- [struct CardView](./cardview.md)
  A card whose content can be injected.
- [protocol OCKCardable](./ockcardable.md)
  Has the ability to display one’s self as a card. A card has a particular corner radius and shadow.
- [struct HeaderView](./headerview.md)
  Header used for most CareKit cards.
- [class OCKHeaderView](./ockheaderview.md)
  A title and detail label. The view can also be configured to show a separator, icon image, and a detail disclosure arrow.
- [class OCKStackView](./ockstackview.md)
  A stack view that supports animating showing/hiding arranged subviews, and has the option of dynamically creating separators when arranged subviews are added.
- [class OCKSeparatorView](./ockseparatorview.md)
  Horizontal separator view.
- [class OCKLabel](./ocklabel.md)
  A label that handles animating state changes and provides accessibility features.
- [class OCKLabeledButton](./ocklabeledbutton.md)
  A button with a filled background color.
- [class OCKAnimatedButton](./ockanimatedbutton.md)
  A highlightable and selectable button that can be animated. The `isHighlighted` state can be specified with options, and the `isSelected` state can be handled automatically when the button is tapped.
- [class OCKView](./ockview.md)
- [struct OCKResponsiveLayout](./ockresponsivelayout.md)
  Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.
### Task-interaction broadcasting
- [protocol OCKTaskDisplayable](./ocktaskdisplayable.md)
  Any object that can display and handle interactions with a task.
- [protocol OCKTaskViewDelegate](./ocktaskviewdelegate.md)
  A protocol that handles events related to a task object.
### Contact-interaction broadcasting
- [protocol OCKContactDisplayable](./ockcontactdisplayable.md)
  Objects that display and handle interactions with a contact.
- [protocol OCKContactViewDelegate](./ockcontactviewdelegate.md)
  A protocol that handles events related to a contact object.
### Chart-interaction broadcasting
- [protocol OCKChartDisplayable](./ockchartdisplayable.md)
  An object that displays and handles interactions with a chart.
- [protocol OCKChartViewDelegate](./ockchartviewdelegate.md)
  A protocol that handles chart object events.
### Calendar-interaction broadcasting
- [protocol OCKCalendarDisplayable](./ockcalendardisplayable.md)
  An object that can display and handle interactions with a calendar.
- [protocol OCKCalendarViewDelegate](./ockcalendarviewdelegate.md)
  A protocol that handles events related to a calendar object.
### Styles
- [protocol OCKStylable](./ockstylable.md)
- [struct OCKStyle](./ockstyle.md)
- [struct OCKAnimationStyle](./ockanimationstyle.md)
  Concrete object for animation constants.
- [struct OCKAppearanceStyle](./ockappearancestyle.md)
  Concrete object for appearance constants.
- [struct OCKColorStyle](./ockcolorstyle.md)
  Concrete object for color constants.
- [struct OCKDimensionStyle](./ockdimensionstyle.md)
  Concrete object for dimension constants.
- [protocol OCKStyler](./ockstyler.md)
  Defines styling constants.
- [protocol OCKAnimationStyler](./ockanimationstyler.md)
  Defines constants for values used during animations.
- [protocol OCKAppearanceStyler](./ockappearancestyler.md)
  Defines constants for view appearance styling.
- [protocol OCKColorStyler](./ockcolorstyler.md)
  Defines color constants.
- [protocol OCKDimensionStyler](./ockdimensionstyler.md)
  Defines constants for view dimension styling.
### Logging
- [struct OCKLog](./ocklog.md)
### Localization
- [class OCKLocalization](./ocklocalization.md)
  A hook for the free function `loc` to access the framework bundle for localizations
- [func loc(String, String, arguments: [CVarArg]) -> String](./loc%28_,_,arguments%29.md)
  A localization string wrapper to access framework specific strings
### Extended Modules
- [SwiftUICore](./swiftuicore.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui)*