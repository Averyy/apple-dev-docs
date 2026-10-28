# UIContentContainer

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods for adapting the contents of your view controllers to size and trait changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UIContentContainer : NSObjectProtocol
```

```objc
@protocol UIContentContainer <NSObject>
```

## Overview

The methods of this protocol handle size-related transitions that are related to changes in the current trait environment or view controller hierarchy. When the parent view controller changes, or when trait changes occur that affect the size of a view controller, UIKit calls these methods to give the affected objects a chance to respond appropriately.

All [`UIViewController`](./uiviewcontroller.md) and [`UIPresentationController`](./uipresentationcontroller.md) objects provide default implementations for the methods of this protocol. When creating your own custom view controller or presentation controller, you can override the default implementations to make adjustments to your content. For example, you might use these methods to adjust the size or position of any child view controllers.

When overriding the methods of this protocol, call `super` to let UIKit perform any default behaviors. View controllers and presentation controllers perform their own adjustments when these methods are called. Calling `super` ensures that UIKit is able to continue adjusting other parts of your user interface.

## Topics

### Responding to environment changes
- [func viewWillTransition(to: CGSize, with: any UIViewControllerTransitionCoordinator)](./uicontentcontainer/viewwilltransition%28to,with%29.md)
  Notifies the container that the size of its view is about to change.
- [func willTransition(to: UITraitCollection, with: any UIViewControllerTransitionCoordinator)](./uicontentcontainer/willtransition%28to,with%29.md)
  Notifies the container that its trait collection changed.
### Responding to changes in child view controllers
- [func size(forChildContentContainer: any UIContentContainer, withParentContainerSize: CGSize) -> CGSize](./uicontentcontainer/size%28forchildcontentcontainer,withparentcontainersize%29.md)
  Returns the size of the specified child view controller’s content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](./uicontentcontainer/preferredcontentsizedidchange%28forchildcontentcontainer%29.md)
  Notifies an interested controller that the preferred content size of one of its children changed.
- [func systemLayoutFittingSizeDidChange(forChildContentContainer: any UIContentContainer)](./uicontentcontainer/systemlayoutfittingsizedidchange%28forchildcontentcontainer%29.md)
  Notifies the container that a child view controller was resized using Auto Layout.
- [var preferredContentSize: CGSize](./uicontentcontainer/preferredcontentsize.md)
  The preferred size for the container’s content.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIActivityViewController](./uiactivityviewcontroller.md)
- [UIAlertController](./uialertcontroller.md)
- [UIArrangementViewController](./uiarrangementviewcontroller.md)
- [UICloudSharingController](./uicloudsharingcontroller.md)
- [UICollectionViewController](./uicollectionviewcontroller.md)
- [UIColorPickerViewController](./uicolorpickerviewcontroller.md)
- [UIDocumentBrowserViewController](./uidocumentbrowserviewcontroller.md)
- [UIDocumentMenuViewController](./uidocumentmenuviewcontroller.md)
- [UIDocumentPickerExtensionViewController](./uidocumentpickerextensionviewcontroller.md)
- [UIDocumentPickerViewController](./uidocumentpickerviewcontroller.md)
- [UIDocumentViewController](./uidocumentviewcontroller.md)
- [UIFontPickerViewController](./uifontpickerviewcontroller.md)
- [UIImagePickerController](./uiimagepickercontroller.md)
- [UIInputViewController](./uiinputviewcontroller.md)
- [UINavigationController](./uinavigationcontroller.md)
- [UIPageViewController](./uipageviewcontroller.md)
- [UIPopoverPresentationController](./uipopoverpresentationcontroller.md)
- [UIPresentationController](./uipresentationcontroller.md)
- [UIReferenceLibraryViewController](./uireferencelibraryviewcontroller.md)
- [UISearchContainerViewController](./uisearchcontainerviewcontroller.md)
- [UISearchController](./uisearchcontroller.md)
- [UISheetPresentationController](./uisheetpresentationcontroller.md)
- [UISplitViewController](./uisplitviewcontroller.md)
- [UITabBarController](./uitabbarcontroller.md)
- [UITableViewController](./uitableviewcontroller.md)
- [UITextFormattingViewController](./uitextformattingviewcontroller.md)
- [UIVideoEditorController](./uivideoeditorcontroller.md)
- [UIViewController](./uiviewcontroller.md)

## See Also

### Content view controllers
- [Displaying and managing views with a view controller](./displaying-and-managing-views-with-a-view-controller.md)
  Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.
- [Showing and hiding view controllers](./showing-and-hiding-view-controllers.md)
  Display view controllers using different techniques, and pass data between them during transitions.
- [class UIViewController](./uiviewcontroller.md)
  An object that manages a view hierarchy for your UIKit app.
- [class UITableViewController](./uitableviewcontroller.md)
  A view controller that specializes in managing a table view.
- [class UICollectionViewController](./uicollectionviewcontroller.md)
  A view controller that specializes in managing a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentcontainer)*