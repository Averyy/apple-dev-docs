# TVBrowserViewController

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

A view controller that presents content in a browsable, full-screen format.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVBrowserViewController
```

```objc
@interface TVBrowserViewController : UIViewController
```

## Overview

Use this class to create a full-screen layout that supports full-screen browsing. This layout includes a built-in parallax effect that is triggered during the transition between cells.

![Screenshot of the full screen browser. Hidden cells lie on the left and right side of the currently displayed cell, with edges peeking out.](https://developer.apple.com/tutorials/images/com.apple.tvmlkit/media-3332104@2x.png)

## Topics

### Initializing the Browser View Controller
- [convenience init?(viewElement: TVViewElement)](./tvbrowserviewcontroller/init%28viewelement%29.md)
  Create a full-screen browser from a specified view element.
### Providing the Browser’s Data
- [var dataSource: (any TVBrowserViewControllerDataSource)?](./tvbrowserviewcontroller/datasource.md)
  The object that provides data to the full-screen browser.
- [protocol TVBrowserViewControllerDataSource](./tvbrowserviewcontrollerdatasource.md)
  Methods adopted by the object you use to represent the browser view.
### Managing Interactions with the Browser
- [var delegate: (any TVBrowserViewControllerDelegate)?](./tvbrowserviewcontroller/delegate.md)
  The object that acts as the delegate and handles callbacks for the browser view.
- [protocol TVBrowserViewControllerDelegate](./tvbrowserviewcontrollerdelegate.md)
  Methods for detecting events and performing actions on the browser view.
### Modifying the Browser Appearance
- [var cornerRadius: CGFloat](./tvbrowserviewcontroller/cornerradius.md)
  The corner radius, in points, of each full-screen browser item.
- [var interitemSpacing: CGFloat](./tvbrowserviewcontroller/interitemspacing.md)
  The spacing between full-screen browser items.
- [var maskInset: UIEdgeInsets](./tvbrowserviewcontroller/maskinset.md)
  The amount by which the content of the cell is inset.
### Accessing Browser Elements
- [var centeredViewElement: TVViewElement](./tvbrowserviewcontroller/centeredviewelement.md)
  The full screen browser item that is currently centered on the screen.
- [var viewElement: TVViewElement](./tvbrowserviewcontroller/viewelement.md)
  The view element that the full screen browser is constructed from.
### Managing Browser Transitions
- [class TVBrowserTransitionAnimator](./tvbrowsertransitionanimator.md)
  An object that provides animations to and from the full screen browser.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Views and View Controllers
- [class TVViewElement](./tvviewelement.md)
  A representation of a read-only DOM node.
- [protocol TVInterfaceCreating](./tvinterfacecreating.md)
  A protocol that defines methods used to create views and view controllers.
- [class TVInterfaceFactory](./tvinterfacefactory.md)
  A factory for the creation of views and view controllers.
- [class TVDocumentViewController](./tvdocumentviewcontroller.md)
  A view controller that represents a TVMLKit document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvbrowserviewcontroller)*