# Automatic trait tracking

**Framework**: UIKit

Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.

#### Overview

Automatic trait tracking is a UIKit feature that eliminates the need to manually register for trait changes when you use traits in a supported method or closure. This feature reduces the amount of code you need to write and maintain, improves performance, and encourages the best practice of using traits within the scope of the supported APIs. For more information, see [`Adapting your app when traits change`](adapting-your-app-when-traits-change.md).

Some properties aren’t appropriate to change during [`layoutSubviews()`](uiview/layoutsubviews().md), for example, properties where setting the value has a side-effect of invalidating the view’s layout. Update these properties in a view’s [`updateProperties()`](uiview/updateproperties().md) method, or a view controller’s [`updateProperties()`](uiviewcontroller/updateproperties().md) method. These methods support automatic trait tracking, and automatic observation tracking on objects that use the [`Observable()`](https://developer.apple.com/documentation/Observation/Observable()) macro. Notify an object of other updates to its properties by calling [`setNeedsUpdateProperties()`](uiview/setneedsupdateproperties().md) on your view, or [`setNeedsUpdateProperties()`](uiviewcontroller/setneedsupdateproperties().md) on your view controller. Force an object to immediately update its properties by calling [`updatePropertiesIfNeeded()`](uiview/updatepropertiesifneeded().md) on your view, or [`updatePropertiesIfNeeded()`](uiviewcontroller/updatepropertiesifneeded().md) on your view controller. For more information on automatically observing property updates, see [`Updating views automatically with observation tracking`](updating-views-automatically-with-observation-tracking.md).

> ❗ **Important**:  Avoid causing excessive updates by avoiding changes in [`layoutSubviews()`](uiview/layoutsubviews().md) that update properties the object tracks in [`updateProperties()`](uiview/updateproperties().md), or that invalidate the view’s layout.

A complete list of APIs that support automatic trait tracking appears below.

## Topics

### Views
- [func updateProperties()](uiview/updateproperties.md)
  Configures the view’s content and styling properties before layout.
- [func setNeedsUpdateProperties()](uiview/setneedsupdateproperties.md)
  Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updatePropertiesIfNeeded()](uiview/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
- [func layoutSubviews()](uiview/layoutsubviews.md)
  Lays out subviews.
- [func updateConstraints()](uiview/updateconstraints.md)
  Updates constraints for the view.
- [func draw(CGRect)](uiview/draw(_:).md)
  Draws the view’s image within the passed-in rectangle.
- [UIView.Invalidations.Properties](uiview/invalidations/properties.md)
### View controllers
- [func updateProperties()](uiviewcontroller/updateproperties.md)
  Configures the view controller’s content and styling properties.
- [func setNeedsUpdateProperties()](uiviewcontroller/setneedsupdateproperties.md)
  Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [func updatePropertiesIfNeeded()](uiviewcontroller/updatepropertiesifneeded.md)
  Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [func viewWillLayoutSubviews()](uiviewcontroller/viewwilllayoutsubviews.md)
  Notifies the view controller that its view is about to lay out its subviews.
- [func viewDidLayoutSubviews()](uiviewcontroller/viewdidlayoutsubviews.md)
  Notifies the view controller when its view finishes laying out its subviews.
- [func updateViewConstraints()](uiviewcontroller/updateviewconstraints.md)
  Notifies the view controller when its view needs to update its constraints.
- [func updateContentUnavailableConfiguration(using: UIContentUnavailableConfigurationState)](uiviewcontroller/updatecontentunavailableconfiguration(using:).md)
  Updates the content-unavailable configuration for the provided state.
### Presentation controllers
- [func containerViewWillLayoutSubviews()](uipresentationcontroller/containerviewwilllayoutsubviews.md)
  Notifies the presentation controller that layout is about to begin on the views of the container view.
- [func containerViewDidLayoutSubviews()](uipresentationcontroller/containerviewdidlayoutsubviews.md)
  Notifies the presentation controller when layout ends on the views of the container view.
### Buttons
- [func updateConfiguration()](uibutton/updateconfiguration.md)
  Updates the button configuration in response to a button state change.
- [var configurationUpdateHandler: UIButton.ConfigurationUpdateHandler?](uibutton/configurationupdatehandler-swift.property.md)
  A closure that executes when the button state changes.
### Collection view cells
- [func updateConfiguration(using: UICellConfigurationState)](uicollectionviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UICollectionViewCell.ConfigurationUpdateHandler?](uicollectionviewcell/configurationupdatehandler-7rqbu.md)
  A block for handling updates to the cell’s configuration using the current state.
### Table view cells
- [func updateConfiguration(using: UICellConfigurationState)](uitableviewcell/updateconfiguration(using:).md)
  Updates the cell’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewCell.ConfigurationUpdateHandler?](uitableviewcell/configurationupdatehandler-974.md)
  A block for handling updates to the cell’s configuration using the current state.
### Table view headers and footers
- [func updateConfiguration(using: UIViewConfigurationState)](uitableviewheaderfooterview/updateconfiguration(using:).md)
  Updates the view’s configuration using the current state.
- [var configurationUpdateHandler: UITableViewHeaderFooterView.ConfigurationUpdateHandler?](uitableviewheaderfooterview/configurationupdatehandler-49slo.md)
  A block for handling updates to the view’s configuration using the current state.
### Collection view compositional layouts
- [typealias UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.

## See Also

- [class UITraitCollection](uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [protocol UITraitEnvironment](uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/automatic-trait-tracking)*