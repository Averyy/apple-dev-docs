# PaperMarkupViewController

**Framework**: PaperKit  
**Kind**: class  
**Role**: Class

A view controller for interactively creating and showing markup.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class PaperMarkupViewController
```

## Mentions

- [Integrating PaperKit into your app](./getting-started-with-paperkit.md)

#### Overview

Properties are observable, so to save markup changes to disk, iterate over the changes to `markup`.

```
let markups = Observations.untilFinished { [weak paperViewController] in
    if let markup = paperViewController?.markup {
        return .next(markup)
    }
    return .finish
}
Task { [weak self] in
    for await newMarkup in markups {
        self?.save(model)
    }
}
```

## Topics

### Creating a view controller
- [init(markup: PaperMarkup?, supportedFeatureSet: FeatureSet)](./papermarkupviewcontroller/init%28markup,supportedfeatureset%29.md)
  Creates a new markup view controller with the provided data model.
### Displaying markup
- [var markup: PaperMarkup?](./papermarkupviewcontroller/markup.md)
  The paper data that this view controller displays.
- [var contentView: UIView?](./papermarkupviewcontroller/contentview-4aeda.md)
  The content that markup appears on top of.
- [var contentView: NSView?](./papermarkupviewcontroller/contentview-4hbkf.md)
  The content that markup appears on top of.
- [var supportedFeatureSet: FeatureSet](./papermarkupviewcontroller/supportedfeatureset.md)
  The supported PaperKit features on this canvas.
### Editing markup
- [var isEditable: Bool](./papermarkupviewcontroller/iseditable.md)
  A Boolean value that indicates whether a person can edit the canvas contents.
- [var drawingTool: any PKTool](./papermarkupviewcontroller/drawingtool.md)
  The tool for drawing on the canvas.
- [var isRulerActive: Bool](./papermarkupviewcontroller/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
### Controlling touch input
- [var directTouchMode: PaperMarkupViewController.TouchMode](./papermarkupviewcontroller/directtouchmode.md)
  The interaction mode for direct touches on the canvas.
- [var directTouchAutomaticallyDraws: Bool](./papermarkupviewcontroller/directtouchautomaticallydraws.md)
  A Boolean value that indicates whether direct touches automatically draw based on system state.
- [var indirectPointerTouchMode: PaperMarkupViewController.TouchMode](./papermarkupviewcontroller/indirectpointertouchmode.md)
  The interaction mode for indirect pointer touches on the canvas.
- [PaperMarkupViewController.TouchMode](./papermarkupviewcontroller/touchmode.md)
  The canvas behavior for touches.
### Selecting elements
- [var selection: Set<MarkupOrderedSet.ElementID>](./papermarkupviewcontroller/selection.md)
  The current selected elements on the canvas.
- [var selectedMarkup: PaperMarkup](./papermarkupviewcontroller/selectedmarkup.md)
  The selected contents in the UI.
- [func suggestedFrameForInserting(contentInFrame: CGRect) -> CGRect](./papermarkupviewcontroller/suggestedframeforinserting%28contentinframe%29.md)
  Returns the suggested frame for inserting shapes and other content.
### Managing adornments
- [var adornments: [MarkupAdornment]](./papermarkupviewcontroller/adornments.md)
  An array of visual adornments that appear on the markup canvas.
- [func adornmentFrame(for: UUID) -> CGRect?](./papermarkupviewcontroller/adornmentframe%28for%29.md)
  Returns the current frame of the specified adornment.
### Scrolling and zooming
- [var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration](./papermarkupviewcontroller/scrollconfiguration-swift.property.md)
  The configuration object that provides access to scroll view functionality.
- [PaperMarkupViewController.ScrollConfiguration](./papermarkupviewcontroller/scrollconfiguration-swift.class.md)
  A cross-platform type that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](./papermarkupviewcontroller/contentvisibleframe.md)
  The visible area of content in the scroll view.
- [func setContentVisibleFrame(CGRect, animated: Bool)](./papermarkupviewcontroller/setcontentvisibleframe%28_,animated%29.md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomRange: ClosedRange<CGFloat>](./papermarkupviewcontroller/zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.
### Responding to changes
- [var delegate: (any PaperMarkupViewController.Delegate)?](./papermarkupviewcontroller/delegate-swift.property.md)
  The delegate for responding to a person’s actions.
- [PaperMarkupViewController.Delegate](./papermarkupviewcontroller/delegate-swift.protocol.md)
  The interface for responding to interactions in a markup view controller.
- [var undoManager: UndoManager?](./papermarkupviewcontroller/undomanager.md)
### Managing first responder status
- [var acceptsFirstResponder: Bool](./papermarkupviewcontroller/acceptsfirstresponder.md)
- [var canBecomeFirstResponder: Bool](./papermarkupviewcontroller/canbecomefirstresponder.md)
### Managing view lifecycle
- [func loadView()](./papermarkupviewcontroller/loadview%28%29.md)
- [func viewDidLoad()](./papermarkupviewcontroller/viewdidload%28%29.md)
- [func viewDidAppear()](./papermarkupviewcontroller/viewdidappear%28%29.md)
- [func viewDidLayout()](./papermarkupviewcontroller/viewdidlayout%28%29.md)
### Deprecated
- [var showsVerticalScrollIndicator: Bool](./papermarkupviewcontroller/showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var showsHorizontalScrollIndicator: Bool](./papermarkupviewcontroller/showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [MarkupEditViewController.Delegate](./markupeditviewcontroller/delegate-swift.protocol.md)
- [MarkupToolbarViewController.Delegate](./markuptoolbarviewcontroller/delegate-swift.protocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Observable](../Observation/observable.md)
- [PKToolPickerObserver](../PencilKit/pktoolpickerobserver.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### View controllers
- [class MarkupEditViewController](./markupeditviewcontroller.md)
  A view controller that manages the interface for inserting content into a canvas.
- [class MarkupToolbarViewController](./markuptoolbarviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller)*