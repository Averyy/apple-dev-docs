# UIPickerView

**Framework**: UIKit  
**Kind**: class

A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPickerView
```

#### Overview

A picker view displays one or more wheels that the user manipulates to select items. Each wheel — known as a  — has a series of indexed rows representing the selectable items. Each row displays a string or view so that the user can identify the item on that row. Users select items by rotating the wheels to the desired values, which align with a selection indicator.

> **Note**:  The [`UIDatePicker`](uidatepicker.md) class uses a custom subclass of [`UIPickerView`](uipickerview.md) to display dates and times. To see an example, tap the add (”+”) button in the Alarm pane of the Clock app.

You provide the data to display in your picker view using a picker data source (an object that adopts the [`UIPickerViewDataSource`](uipickerviewdatasource.md) protocol). Use your picker view delegate (an object that adopts the [`UIPickerViewDelegate`](uipickerviewdelegate.md) protocol) to provide views for displaying your data and responding to user selections.

> ❗ **Important**:  [`UIPickerView`](uipickerview.md) and its descendants aren’t available when the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md).

## Topics

### Providing the picker data
- [var dataSource: (any UIPickerViewDataSource)?](uipickerview/datasource.md)
  The data source for the picker view.
- [protocol UIPickerViewDataSource](uipickerviewdatasource.md)
  The interface for a picker view’s data source.
### Customizing the picker behavior
- [var delegate: (any UIPickerViewDelegate)?](uipickerview/delegate.md)
  The delegate for the picker view.
- [protocol UIPickerViewDelegate](uipickerviewdelegate.md)
  The interface for a picker view’s delegate.
### Getting the dimensions of the picker view
- [var numberOfComponents: Int](uipickerview/numberofcomponents.md)
  The number of components for the picker view.
- [func numberOfRows(inComponent: Int) -> Int](uipickerview/numberofrows(incomponent:).md)
  Returns the number of rows for a component.
- [func rowSize(forComponent: Int) -> CGSize](uipickerview/rowsize(forcomponent:).md)
  Returns the size of a row for a component.
### Reloading the picker view
- [func reloadAllComponents()](uipickerview/reloadallcomponents.md)
  Reloads all components of the picker view.
- [func reloadComponent(Int)](uipickerview/reloadcomponent(_:).md)
  Reloads a particular component of the picker view.
### Selecting rows in the view picker
- [func selectRow(Int, inComponent: Int, animated: Bool)](uipickerview/selectrow(_:incomponent:animated:).md)
  Selects a row in a specified component of the picker view.
- [func selectedRow(inComponent: Int) -> Int](uipickerview/selectedrow(incomponent:).md)
  Returns the index of the selected row in a given component.
### Returning the view for a row and component
- [func view(forRow: Int, forComponent: Int) -> UIView?](uipickerview/view(forrow:forcomponent:).md)
  Returns the view used by the picker view for a given row and component.
### Managing the appearance of the picker view
- [var showsSelectionIndicator: Bool](uipickerview/showsselectionindicator.md)
  A Boolean value that determines whether the selection indicator is displayed.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIActivityIndicatorView](uiactivityindicatorview.md)
  A view that shows that a task is in progress.
- [class UICalendarView](uicalendarview.md)
  A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [class UIContentUnavailableView](uicontentunavailableview.md)
  A view that indicates there’s no content to display.
- [class UIImageView](uiimageview.md)
  A view that displays a single image or a sequence of animated images in your interface.
- [class UIProgressView](uiprogressview.md)
  A view that depicts the progress of a task over time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview)*