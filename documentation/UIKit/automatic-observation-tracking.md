# Automatic observation tracking

**Framework**: UIKit

Simplify updating views when data changes by making updates in methods that support automatic observation tracking.

#### Overview

Use automatic observation tracking to update your views in response to model object changes without manually invalidating views. Mark your model classes with the [`Observable`](https://developer.apple.com/documentation/Observation/Observable) macro, then read model properties in methods like [`updateProperties()`](uiview/updateproperties().md) or [`layoutSubviews()`](uiview/layoutsubviews().md). UIKit tracks which properties you access and automatically calls these methods again when those properties change. This approach eliminates the need to manually call methods like [`setNeedsLayout()`](uiview/setneedslayout().md) or [`setNeedsDisplay()`](uiview/setneedsdisplay().md) after updating model data, reducing opportunities for bugs and outdated displays.

These methods support automatic observation tracking in views, view controllers, presentation controllers, buttons, collection view cells, table view cells, and table view headers and footers. For more information, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

## Topics

### Observing data in views
- [func updateProperties()](uiview/updateproperties.md)
  Configures the view’s content and styling properties before layout.
- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.
### Observing data in view controllers
- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Configures the view controller’s content and styling properties.
- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](uiviewcontroller/viewdidlayoutsubviews.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.
### Observing data in presentation controllers
- [func containerViewWillLayoutSubviews()](uipresentationcontroller/containerviewwilllayoutsubviews.md)
  Notifies the presentation controller that layout is about to begin on the views of the container view.
- [func containerViewDidLayoutSubviews()](uipresentationcontroller/containerviewdidlayoutsubviews.md)
  Notifies the presentation controller when layout ends on the views of the container view.
### Observing data in buttons
- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
### Observing data in collection view cells
- [func updateConfiguration(using: UICellConfigurationState)](uicollectionviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](uicollectionviewcell/configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
### Observing data in table view cells
- [func updateConfiguration(using: UICellConfigurationState)](uitableviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.
### Observing data in table header and footer views
- [func updateConfiguration(using: UIViewConfigurationState)](uitableviewheaderfooterview/updateconfiguration(using:).md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](uitableviewheaderfooterview/configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.

## See Also

- [Updating views automatically with observation tracking](updating-views-automatically-with-observation-tracking.md)
  Use Swift Observation and UIKit’s automatic tracking to update your views in response to model data updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/automatic-observation-tracking)*