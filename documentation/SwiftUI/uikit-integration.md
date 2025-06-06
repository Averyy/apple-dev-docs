# UIKit integration

**Framework**: SwiftUI

Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.

#### Overview

Integrate SwiftUI with your app’s existing content using hosting controllers to add SwiftUI views into UIKit interfaces. A hosting controller wraps a set of SwiftUI views in a form that you can then add to your storyboard-based app.

![None](https://docs-assets.developer.apple.com/published/74ee52cce15bcc5332715296b5d568d9/uikit-integration-hero%402x.png)

You can also add UIKit views and view controllers to your SwiftUI interfaces. A representable object wraps the designated view or view controller, and facilitates communication between the wrapped object and your SwiftUI views.

For design guidance, see the following sections in the Human Interface Guidelines:

- [`Designing for iOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-ios)
- [`Designing for iPadOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-ipados)
- [`Designing for tvOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-tvos)

## Topics

### Displaying SwiftUI views in UIKit
- [Using SwiftUI with UIKit](../UIKit/using-swiftui-with-uikit.md)
  Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class UIHostingController](uihostingcontroller.md)
  A UIKit view controller that manages a SwiftUI view hierarchy.
- [struct UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md)
  Options for how a hosting controller tracks its content’s size.
- [struct UIHostingConfiguration](uihostingconfiguration.md)
  A content configuration suitable for hosting a hierarchy of SwiftUI views.
### Adding UIKit views to SwiftUI view hierarchies
- [protocol UIViewRepresentable](uiviewrepresentable.md)
  A wrapper for a UIKit view that you use to integrate that view into your SwiftUI view hierarchy.
- [struct UIViewRepresentableContext](uiviewrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your UIKit view.
- [protocol UIViewControllerRepresentable](uiviewcontrollerrepresentable.md)
  A view that represents a UIKit view controller.
- [struct UIViewControllerRepresentableContext](uiviewcontrollerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your UIKit view controller.
### Integrate gesture recognizer into SwiftUI view hierarchies
- [protocol UIGestureRecognizerRepresentable](uigesturerecognizerrepresentable.md)
  A wrapper for a `UIGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [struct UIGestureRecognizerRepresentableContext](uigesturerecognizerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
- [struct UIGestureRecognizerRepresentableCoordinateSpaceConverter](uigesturerecognizerrepresentablecoordinatespaceconverter.md)
  A proxy structure used to convert locations to/from coordinate spaces in the hierarchy of the SwiftUI view associated with a [`UIGestureRecognizerRepresentable`](uigesturerecognizerrepresentable.md).
### Sharing configuration information
- [protocol UITraitBridgedEnvironmentKey](uitraitbridgedenvironmentkey.md)
  An environment key that is bridged to a UIKit trait.
### Hosting an ornament in UIKit
- [class UIHostingOrnament](uihostingornament.md)
  A model that represents an ornament suitable for being hosted in UIKit.
- [class UIOrnament](uiornament.md)
  The abstract base class that represents an ornament.

## See Also

- [AppKit integration](appkit-integration.md)
  Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.
- [WatchKit integration](watchkit-integration.md)
  Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
- [Technology-specific views](technology-specific-views.md)
  Use SwiftUI views that other Apple frameworks provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uikit-integration)*