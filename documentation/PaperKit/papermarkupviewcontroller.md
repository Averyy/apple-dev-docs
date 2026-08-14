# PaperMarkupViewController

**Framework**: PaperKit  
**Kind**: class

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

- [Integrating PaperKit into your app](getting-started-with-paperkit.md)

#### Overview

Properties are observable, so to save markup changes to disk, iterate over the changes to `markup`.

```None
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
- [init(markup: PaperMarkup?, supportedFeatureSet: FeatureSet)](papermarkupviewcontroller/init(markup:supportedfeatureset:).md)
  Creates a new markup view controller with the provided data model.
### Displaying markup
- [var markup: PaperMarkup?](papermarkupviewcontroller/markup.md)
  The paper data that this view controller displays.
- [var contentView: UIView?](papermarkupviewcontroller/contentview-4aeda.md)
  The content that markup appears on top of.
- [var contentView: NSView?](papermarkupviewcontroller/contentview-4hbkf.md)
  The content that markup appears on top of.
- [var supportedFeatureSet: FeatureSet](papermarkupviewcontroller/supportedfeatureset.md)
  The supported PaperKit features on this canvas.
### Editing markup
- [var isEditable: Bool](papermarkupviewcontroller/iseditable.md)
  A Boolean value that indicates whether a person can edit the canvas contents.
- [var drawingTool: any PKTool](papermarkupviewcontroller/drawingtool.md)
  The tool for drawing on the canvas.
- [var isRulerActive: Bool](papermarkupviewcontroller/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
### Controlling touch input
- [var directTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/directtouchmode.md)
  The interaction mode for direct touches on the canvas.
- [var directTouchAutomaticallyDraws: Bool](papermarkupviewcontroller/directtouchautomaticallydraws.md)
  A Boolean value that indicates whether direct touches automatically draw based on system state.
- [var indirectPointerTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/indirectpointertouchmode.md)
  The interaction mode for indirect pointer touches on the canvas.
- [PaperMarkupViewController.TouchMode](papermarkupviewcontroller/touchmode.md)
  The canvas behavior for touches.
### Selecting elements
- [var selection: Set<MarkupOrderedSet.ElementID>](papermarkupviewcontroller/selection.md)
  The current selected elements on the canvas.
- [var selectedMarkup: PaperMarkup](papermarkupviewcontroller/selectedmarkup.md)
  The selected contents in the UI.
- [func suggestedFrameForInserting(contentInFrame: CGRect) -> CGRect](papermarkupviewcontroller/suggestedframeforinserting(contentinframe:).md)
  Returns the suggested frame for inserting shapes and other content.
### Managing adornments
- [var adornments: [MarkupAdornment]](papermarkupviewcontroller/adornments.md)
  An array of visual adornments that appear on the markup canvas.
- [func adornmentFrame(for: UUID) -> CGRect?](papermarkupviewcontroller/adornmentframe(for:).md)
  Returns the current frame of the specified adornment.
### Scrolling and zooming
- [var scrollConfiguration: PaperMarkupViewController.ScrollConfiguration](papermarkupviewcontroller/scrollconfiguration-swift.property.md)
  The configuration object that provides access to scroll view functionality.
- [PaperMarkupViewController.ScrollConfiguration](papermarkupviewcontroller/scrollconfiguration-swift.class.md)
  A cross-platform type that provides access to scroll view functionality.
- [var contentVisibleFrame: CGRect](papermarkupviewcontroller/contentvisibleframe.md)
  The visible area of content in the scroll view.
- [func setContentVisibleFrame(CGRect, animated: Bool)](papermarkupviewcontroller/setcontentvisibleframe(_:animated:).md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [var zoomRange: ClosedRange<CGFloat>](papermarkupviewcontroller/zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.
### Responding to changes
- [var delegate: (any PaperMarkupViewController.Delegate)?](papermarkupviewcontroller/delegate-swift.property.md)
  The delegate for responding to a person’s actions.
- [PaperMarkupViewController.Delegate](papermarkupviewcontroller/delegate-swift.protocol.md)
  The interface for responding to interactions in a markup view controller.
- [var undoManager: UndoManager?](papermarkupviewcontroller/undomanager.md)
### Managing first responder status
- [var acceptsFirstResponder: Bool](papermarkupviewcontroller/acceptsfirstresponder.md)
- [var canBecomeFirstResponder: Bool](papermarkupviewcontroller/canbecomefirstresponder.md)
### Managing view lifecycle
- [func loadView()](papermarkupviewcontroller/loadview.md)
- [func viewDidLoad()](papermarkupviewcontroller/viewdidload.md)
- [func viewDidAppear()](papermarkupviewcontroller/viewdidappear.md)
- [func viewDidLayout()](papermarkupviewcontroller/viewdidlayout.md)
### Deprecated
- [var showsVerticalScrollIndicator: Bool](papermarkupviewcontroller/showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var showsHorizontalScrollIndicator: Bool](papermarkupviewcontroller/showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [MarkupEditViewController.Delegate](markupeditviewcontroller/delegate-swift.protocol.md)
- [MarkupToolbarViewController.Delegate](markuptoolbarviewcontroller/delegate-swift.protocol.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Observable](../observation/observable.md)
- [PKToolPickerObserver](../pencilkit/pktoolpickerobserver.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class MarkupEditViewController](markupeditviewcontroller.md)
  A view controller that manages the interface for inserting content into a canvas.
- [class MarkupToolbarViewController](markuptoolbarviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller)*