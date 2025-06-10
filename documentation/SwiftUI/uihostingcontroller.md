# UIHostingController

**Framework**: SwiftUI  
**Kind**: class

A UIKit view controller that manages a SwiftUI view hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency class UIHostingController<Content> where Content : View
```

#### Overview

Create a `UIHostingController` object when you want to integrate SwiftUI views into a UIKit view hierarchy. At creation time, specify the SwiftUI view you want to use as the root view for this view controller; you can change that view later using the [`rootView`](uihostingcontroller/rootview.md) property. Use the hosting controller like you would any other view controller, by presenting it or embedding it as a child view controller in your interface.

## Topics

### Creating a hosting controller object
- [init(rootView: Content)](uihostingcontroller/init(rootview:).md)
  Creates a hosting controller object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder, rootView: Content)](uihostingcontroller/init(coder:rootview:).md)
  Creates a hosting controller object from an archive and the specified SwiftUI view.
- [init?(coder: NSCoder)](uihostingcontroller/init(coder:).md)
  Creates a hosting controller object from the contents of the specified archive.
### Responding to view-related events
- [func loadView()](uihostingcontroller/loadview.md)
- [func viewWillAppear(Bool)](uihostingcontroller/viewwillappear(_:).md)
  Notifies the view controller that its view is about to be added to a view hierarchy.
- [func viewDidAppear(Bool)](uihostingcontroller/viewdidappear(_:).md)
  Notifies the view controller that its view has been added to a view hierarchy.
- [func viewWillDisappear(Bool)](uihostingcontroller/viewwilldisappear(_:).md)
  Notifies the view controller that its view will be removed from a view hierarchy.
- [func viewDidDisappear(Bool)](uihostingcontroller/viewdiddisappear(_:).md)
- [func willMove(toParent: UIViewController?)](uihostingcontroller/willmove(toparent:).md)
- [func didMove(toParent: UIViewController?)](uihostingcontroller/didmove(toparent:).md)
- [func viewWillTransition(to: CGSize, with: any UIViewControllerTransitionCoordinator)](uihostingcontroller/viewwilltransition(to:with:).md)
- [func viewWillLayoutSubviews()](uihostingcontroller/viewwilllayoutsubviews.md)
- [func target(forAction: Selector, withSender: Any?) -> Any?](uihostingcontroller/target(foraction:withsender:).md)
- [var rootView: Content](uihostingcontroller/rootview.md)
  The root view of the SwiftUI view hierarchy managed by this view controller.
### Checking for modality
- [var isModalInPresentation: Bool](uihostingcontroller/ismodalinpresentation.md)
### Managing the size
- [var sizingOptions: UIHostingControllerSizingOptions](uihostingcontroller/sizingoptions.md)
  The options for how the hosting controller tracks changes to the size of its SwiftUI content.
- [func preferredContentSizeDidChange(forChildContentContainer: any UIContentContainer)](uihostingcontroller/preferredcontentsizedidchange(forchildcontentcontainer:).md)
- [func sizeThatFits(in: CGSize) -> CGSize](uihostingcontroller/sizethatfits(in:).md)
  Calculates and returns the most appropriate size for the current view.
- [var safeAreaRegions: SafeAreaRegions](uihostingcontroller/safearearegions.md)
  The safe area regions that this view controller adds to its view.
### Configuring the status bar
- [var preferredStatusBarStyle: UIStatusBarStyle](uihostingcontroller/preferredstatusbarstyle.md)
  The preferred status bar style for the view controller.
- [var preferredStatusBarUpdateAnimation: UIStatusBarAnimation](uihostingcontroller/preferredstatusbarupdateanimation.md)
  The animation style to use when hiding or showing the status bar for this view controller.
- [var prefersStatusBarHidden: Bool](uihostingcontroller/prefersstatusbarhidden.md)
  A Boolean value that indicates whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarStyle: UIViewController?](uihostingcontroller/childforstatusbarstyle.md)
- [var childForStatusBarHidden: UIViewController?](uihostingcontroller/childforstatusbarhidden.md)
### Configuring the home indicator
- [var prefersHomeIndicatorAutoHidden: Bool](uihostingcontroller/prefershomeindicatorautohidden.md)
  A Boolean value that indicates whether the view controller prefers the home indicator to be hidden or shown.
- [var childForHomeIndicatorAutoHidden: UIViewController?](uihostingcontroller/childforhomeindicatorautohidden.md)
### Configuring the interface appearance
- [var preferredUserInterfaceStyle: UIUserInterfaceStyle](uihostingcontroller/preferreduserinterfacestyle.md)
  The preferred interface style for this view controller.
- [var preferredScreenEdgesDeferringSystemGestures: UIRectEdge](uihostingcontroller/preferredscreenedgesdeferringsystemgestures.md)
  Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [var childForScreenEdgesDeferringSystemGestures: UIViewController?](uihostingcontroller/childforscreenedgesdeferringsystemgestures.md)
### Accessing the available key commands
- [var keyCommands: [UIKeyCommand]?](uihostingcontroller/keycommands.md)
### Managing undo
- [var undoManager: UndoManager?](uihostingcontroller/undomanager.md)
### Instance Properties
- [var childViewControllerForPreferredContainerBackgroundStyle: UIViewController?](uihostingcontroller/childviewcontrollerforpreferredcontainerbackgroundstyle.md)
- [var preferredContainerBackgroundStyle: UIContainerBackgroundStyle](uihostingcontroller/preferredcontainerbackgroundstyle.md)
### Instance Methods
- [func addChild(UIViewController)](uihostingcontroller/addchild(_:).md)

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Using SwiftUI with UIKit](../UIKit/using-swiftui-with-uikit.md)
  Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [struct UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md)
  Options for how a hosting controller tracks its content’s size.
- [struct UIHostingConfiguration](uihostingconfiguration.md)
  A content configuration suitable for hosting a hierarchy of SwiftUI views.
- [protocol UIHostingSceneDelegate](uihostingscenedelegate.md)
  Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller)*