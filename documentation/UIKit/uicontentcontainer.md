# UIContentContainer

**Framework**: UIKit  
**Kind**: protocol

A set of methods for adapting the contents of your view controllers to size and trait changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIContentContainer : NSObjectProtocol
```

#### Overview

The methods of this protocol handle size-related transitions that are related to changes in the current trait environment or view controller hierarchy. When the parent view controller changes, or when trait changes occur that affect the size of a view controller, UIKit calls these methods to give the affected objects a chance to respond appropriately.

All [`UIViewController`](uiviewcontroller.md) and [`UIPresentationController`](uipresentationcontroller.md) objects provide default implementations for the methods of this protocol. When creating your own custom view controller or presentation controller, you can override the default implementations to make adjustments to your content. For example, you might use these methods to adjust the size or position of any child view controllers.

When overriding the methods of this protocol, call `super` to let UIKit perform any default behaviors. View controllers and presentation controllers perform their own adjustments when these methods are called. Calling `super` ensures that UIKit is able to continue adjusting other parts of your user interface.

## Topics

### Responding to environment changes
- [func viewWillTransition(to: CGSize, with: any UIViewControllerTransitionCoordinator)](uicontentcontainer/viewwilltransition(to:with:).md)
  Notifies the container that the size of its view is about to change.
- [func willTransition(to: UITraitCollection, with: any UIViewControllerTransitionCoordinator)](uicontentcontainer/willtransition(to:with:).md)
  Notifies the container that its trait collection changed.
### Responding to changes in child view controllers
- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:).md)
  Returns the size of the specified child view controller’s content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer:).md)
  Notifies an interested controller that the preferred content size of one of its children changed.
- [func systemLayoutFittingSizeDidChange(forChildContentContainer: any UIContentContainer)](uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:).md)
  Notifies the container that a child view controller was resized using Auto Layout.
- [var preferredContentSize: CGSize](uicontentcontainer/preferredcontentsize.md)
  The preferred size for the container’s content.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UIActivityViewController](uiactivityviewcontroller.md)
- [UIAlertController](uialertcontroller.md)
- [UICloudSharingController](uicloudsharingcontroller.md)
- [UICollectionViewController](uicollectionviewcontroller.md)
- [UIColorPickerViewController](uicolorpickerviewcontroller.md)
- [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md)
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md)
- [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md)
- [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md)
- [UIDocumentViewController](uidocumentviewcontroller.md)
- [UIFontPickerViewController](uifontpickerviewcontroller.md)
- [UIImagePickerController](uiimagepickercontroller.md)
- [UIInputViewController](uiinputviewcontroller.md)
- [UINavigationController](uinavigationcontroller.md)
- [UIPageViewController](uipageviewcontroller.md)
- [UIPopoverPresentationController](uipopoverpresentationcontroller.md)
- [UIPresentationController](uipresentationcontroller.md)
- [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md)
- [UISearchContainerViewController](uisearchcontainerviewcontroller.md)
- [UISearchController](uisearchcontroller.md)
- [UISheetPresentationController](uisheetpresentationcontroller.md)
- [UISplitViewController](uisplitviewcontroller.md)
- [UITabBarController](uitabbarcontroller.md)
- [UITableViewController](uitableviewcontroller.md)
- [UITextFormattingViewController](uitextformattingviewcontroller.md)
- [UIVideoEditorController](uivideoeditorcontroller.md)
- [UIViewController](uiviewcontroller.md)

## See Also

- [Automatic trait tracking](automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [Responding to changing display modes on Apple TV](responding-to-changing-display-modes-on-apple-tv.md)
  Change images and resources dynamically when the screen gamut on your device changes.
- [class UITraitCollection](uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [protocol UITraitEnvironment](uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [protocol UITraitChangeObservable](uitraitchangeobservable-67e94.md)
  A type that calls your code in reaction to changes in the trait environment.
- [protocol UIMutableTraits](uimutabletraits-13ja5.md)
  A mutable container of traits.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer)*