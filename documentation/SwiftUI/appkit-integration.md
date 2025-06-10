# AppKit integration

**Framework**: SwiftUI

Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.

#### Overview

Integrate SwiftUI with your app’s existing content using hosting controllers to add SwiftUI views into AppKit interfaces. A hosting controller wraps a set of SwiftUI views in a form that you can then add to your storyboard-based app.

![None](https://docs-assets.developer.apple.com/published/afddaf77e2520d7c1a298575a9bbf6d5/appkit-integration-hero%402x.png)

You can also add AppKit views and view controllers to your SwiftUI interfaces. A representable object wraps the designated view or view controller, and facilitates communication between the wrapped object and your SwiftUI views.

For design guidance, see [`Designing for macOS`](https://developer.apple.com/design/Human-Interface-Guidelines/designing-for-macos) in the Human Interface Guidelines.

## Topics

### Displaying SwiftUI views in AppKit
- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class NSHostingController](nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingView](nshostingview.md)
  An AppKit view that hosts a SwiftUI view hierarchy.
- [class NSHostingMenu](nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSizingOptions](nshostingsizingoptions.md)
  Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [class NSHostingSceneRepresentation](nshostingscenerepresentation.md)
  An AppKit type that hosts and can present SwiftUI scenes
- [struct NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md)
  Options for how hosting views and controllers manage aspects of the associated window.
### Adding AppKit views to SwiftUI view hierarchies
- [protocol NSViewRepresentable](nsviewrepresentable.md)
  A wrapper that you use to integrate an AppKit view into your SwiftUI view hierarchy.
- [struct NSViewRepresentableContext](nsviewrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your AppKit view.
- [protocol NSViewControllerRepresentable](nsviewcontrollerrepresentable.md)
  A wrapper that you use to integrate an AppKit view controller into your SwiftUI interface.
- [struct NSViewControllerRepresentableContext](nsviewcontrollerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update your AppKit view controller.
### Adding AppKit gesture recognizers into SwiftUI view hierarchies
- [protocol NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md)
  A wrapper for an `NSGestureRecognizer` that you use to integrate that gesture recognizer into your SwiftUI hierarchy.
- [struct NSGestureRecognizerRepresentableContext](nsgesturerecognizerrepresentablecontext.md)
  Contextual information about the state of the system that you use to create and update a represented gesture recognizer.
- [struct NSGestureRecognizerRepresentableCoordinateSpaceConverter](nsgesturerecognizerrepresentablecoordinatespaceconverter.md)
  A structure used to convert locations to and from coordinate spaces in the hierarchy of the SwiftUI view associated with an [`NSGestureRecognizerRepresentable`](nsgesturerecognizerrepresentable.md).

## See Also

- [UIKit integration](uikit-integration.md)
  Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.
- [WatchKit integration](watchkit-integration.md)
  Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.
- [Technology-specific views](technology-specific-views.md)
  Use SwiftUI views that other Apple frameworks provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appkit-integration)*