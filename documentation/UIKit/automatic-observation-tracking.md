# Automatic observation tracking

**Framework**: UIKit  
**Role**: API Collection

Simplify updating views when data changes by making updates in methods that support automatic observation tracking.

#### Overview

Use automatic observation tracking to update your views in response to model object changes without manually invalidating views. Mark your model classes with the [`Observable`](../Observation/observable.md) macro, then read model properties in methods like [`updateProperties()`](./uiview/updateproperties%28%29.md) or [`layoutSubviews()`](./uiview/layoutsubviews%28%29.md). UIKit tracks which properties you access and automatically calls these methods again when those properties change. This approach eliminates the need to manually call methods like [`setNeedsLayout()`](./uiview/setneedslayout%28%29.md) or [`setNeedsDisplay()`](./uiview/setneedsdisplay%28%29.md) after updating model data, reducing opportunities for bugs and outdated displays.

These methods support automatic observation tracking in views, view controllers, presentation controllers, buttons, collection view cells, table view cells, and table view headers and footers. For more information, see [Updating views automatically with observation tracking in UIKit](./updating-views-automatically-with-observation-tracking-in-uikit.md).

## Topics

### Observing data in views
- [func updateProperties()](./uiview/updateproperties%28%29.md)
  Configures the view’s content and styling properties before layout.
- [func layoutSubviews()](./uiview/layoutsubviews%28%29.md)
  Lays out subviews.
- [func updateConstraints()](./uiview/updateconstraints%28%29.md)
  Updates constraints for the view.
- [func draw(CGRect)](./uiview/draw%28_%29.md)
  Draws the view’s image within the passed-in rectangle.
### Observing data in view controllers
- [func updateProperties()](./uiviewcontroller/updateproperties%28%29.md)
  Configures the view controller’s content and styling properties.
- [func viewWillLayoutSubviews()](./uiviewcontroller/viewwilllayoutsubviews%28%29.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](./uiviewcontroller/viewdidlayoutsubviews%28%29.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](./uiviewcontroller/updateviewconstraints%28%29.md)
  Notifies the view controller when its view needs to update its constraints.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](./uiviewcontroller/updatecontentunavailableconfiguration%28using%29.md)
  Updates the content-unavailable configuration for the provided state.
### Observing data in presentation controllers
- [func containerViewWillLayoutSubviews()](./uipresentationcontroller/containerviewwilllayoutsubviews%28%29.md)
  Notifies the presentation controller that layout is about to begin on the views of the container view.
- [func containerViewDidLayoutSubviews()](./uipresentationcontroller/containerviewdidlayoutsubviews%28%29.md)
  Notifies the presentation controller when layout ends on the views of the container view.
### Observing data in buttons
- [func updateConfiguration()](./uibutton/updateconfiguration%28%29.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](./uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
### Observing data in collection view cells
- [func updateConfiguration(using: UICellConfigurationState)](./uicollectionviewcell/updateconfiguration%28using%29.md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](./uicollectionviewcell/configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
### Observing data in table view cells
- [func updateConfiguration(using: UICellConfigurationState)](./uitableviewcell/updateconfiguration%28using%29.md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](./uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.
### Observing data in table header and footer views
- [func updateConfiguration(using: UIViewConfigurationState)](./uitableviewheaderfooterview/updateconfiguration%28using%29.md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](./uitableviewheaderfooterview/configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.
### Observing data in collection view layouts
- [typealias UICollectionViewCompositionalLayoutSectionProvider](./uicollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider)](./uicollectionviewcompositionallayout/init%28sectionprovider%29.md)
  Creates a compositional layout object with a section provider to supply the layout’s sections.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider, configuration: UICollectionViewCompositionalLayoutConfiguration)](./uicollectionviewcompositionallayout/init%28sectionprovider,configuration%29.md)
  Creates a compositional layout object with a section provider and an additional configuration.

## See Also

### Data observation
- [Updating views automatically with observation tracking in UIKit](./updating-views-automatically-with-observation-tracking-in-uikit.md)
  Use Swift Observation and automatic tracking to update your views in response to model data updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/automatic-observation-tracking)*