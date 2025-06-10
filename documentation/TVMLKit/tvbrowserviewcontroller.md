# TVBrowserViewController

**Framework**: TVMLKit  
**Kind**: class

A view controller that presents content in a browsable, full-screen format.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
class TVBrowserViewController
```

#### Overview

Use this class to create a full-screen layout that supports full-screen browsing. This layout includes a built-in parallax effect that is triggered during the transition between cells.

![Screenshot of the full screen browser. Hidden cells lie on the left and right side of the currently displayed cell, with edges peeking out.](https://docs-assets.developer.apple.com/published/2f5e58a70ebd8fd24d54f039c9b15ca2/media-3332104%402x.png)

## Topics

### Initializing the Browser View Controller
- [convenience init?(viewElement: TVViewElement)](tvbrowserviewcontroller/init(viewelement:).md)
  Create a full-screen browser from a specified view element.
### Providing the Browser’s Data
- [var dataSource: (any TVBrowserViewControllerDataSource)?](tvbrowserviewcontroller/datasource.md)
  The object that provides data to the full-screen browser.
- [protocol TVBrowserViewControllerDataSource](tvbrowserviewcontrollerdatasource.md)
  Methods adopted by the object you use to represent the browser view.
### Managing Interactions with the Browser
- [var delegate: (any TVBrowserViewControllerDelegate)?](tvbrowserviewcontroller/delegate.md)
  The object that acts as the delegate and handles callbacks for the browser view.
- [protocol TVBrowserViewControllerDelegate](tvbrowserviewcontrollerdelegate.md)
  Methods for detecting events and performing actions on the browser view.
### Modifying the Browser Appearance
- [var cornerRadius: CGFloat](tvbrowserviewcontroller/cornerradius.md)
  The corner radius, in points, of each full-screen browser item.
- [var interitemSpacing: CGFloat](tvbrowserviewcontroller/interitemspacing.md)
  The spacing between full-screen browser items.
- [var maskInset: UIEdgeInsets](tvbrowserviewcontroller/maskinset.md)
  The amount by which the content of the cell is inset.
### Accessing Browser Elements
- [var centeredViewElement: TVViewElement](tvbrowserviewcontroller/centeredviewelement.md)
  The full screen browser item that is currently centered on the screen.
- [var viewElement: TVViewElement](tvbrowserviewcontroller/viewelement.md)
  The view element that the full screen browser is constructed from.
### Managing Browser Transitions
- [class TVBrowserTransitionAnimator](tvbrowsertransitionanimator.md)
  An object that provides animations to and from the full screen browser.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class TVViewElement](tvviewelement.md)
  A representation of a read-only DOM node.
- [protocol TVInterfaceCreating](tvinterfacecreating.md)
  A protocol that defines methods used to create views and view controllers.
- [class TVInterfaceFactory](tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVDocumentViewController](tvdocumentviewcontroller.md)
  A view controller that represents a TVMLKit document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontroller)*