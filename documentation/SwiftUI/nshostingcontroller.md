# NSHostingController

**Framework**: SwiftUI  
**Kind**: class

An AppKit view controller that hosts SwiftUI view hierarchy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency class NSHostingController<Content> where Content : View
```

#### Overview

Create an `NSHostingController` object when you want to integrate SwiftUI views into an AppKit view hierarchy. At creation time, specify the SwiftUI view you want to use as the root view for this view controller; you can change that view later using the [`rootView`](nshostingcontroller/rootview.md) property. Use the hosting controller like you would any other view controller, by presenting it or embedding it as a child view controller in your interface.

## Topics

### Creating a hosting controller object
- [init(rootView: Content)](nshostingcontroller/init(rootview:).md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder, rootView: Content)](nshostingcontroller/init(coder:rootview:).md)
  Creates a hosting controller object from an archive and the specified SwiftUI view.
- [init?(coder: NSCoder)](nshostingcontroller/init(coder:).md)
  Creates a hosting controller object from the contents of the specified archive.
### Getting the root view
- [var rootView: Content](nshostingcontroller/rootview.md)
  The root view of the SwiftUI view hierarchy managed by this view controller.
- [var identifier: NSUserInterfaceItemIdentifier?](nshostingcontroller/identifier.md)
### Configuring the controller
- [func sizeThatFits(in: CGSize) -> CGSize](nshostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.
- [var preferredContentSize: NSSize](nshostingcontroller/preferredcontentsize.md)
- [var sizingOptions: NSHostingSizingOptions](nshostingcontroller/sizingoptions.md)
  The options for how the hosting controller’s view creates and updates constraints based on the size of its SwiftUI content.
- [var safeAreaRegions: SafeAreaRegions](nshostingcontroller/safearearegions.md)
  The safe area regions that this view controller adds to its view.
- [var sceneBridgingOptions: NSHostingSceneBridgingOptions](nshostingcontroller/scenebridgingoptions.md)
  The options for which aspects of the window will be managed by this controller’s hosting view.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)

## See Also

- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingcontroller)*