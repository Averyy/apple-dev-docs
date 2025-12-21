# PaperMarkupViewController

**Framework**: PaperKit  
**Kind**: class

A view controller for interactively creating, and showing markup.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class PaperMarkupViewController
```

#### Overview

Properties are observable, so to save markup changes to disk iterate over the changes to `markup`.

```None
// Listen to changes and save them to disk.
Task { [weak self] in
    for model in await paperViewController.observeValues(for: \.markup) {
        self?.save(model)
    }
}
```

## Topics

### Protocols
- [PaperMarkupViewController.Delegate](papermarkupviewcontroller/delegate-swift.protocol.md)
### Initializers
- [init(markup: PaperMarkup?, supportedFeatureSet: FeatureSet)](papermarkupviewcontroller/init(markup:supportedfeatureset:).md)
  Create a new `PaperMarkupViewController` with the provided data model.
### Instance Properties
- [var acceptsFirstResponder: Bool](papermarkupviewcontroller/acceptsfirstresponder.md)
- [var canBecomeFirstResponder: Bool](papermarkupviewcontroller/canbecomefirstresponder.md)
- [var contentView: UIView?](papermarkupviewcontroller/contentview-4aeda.md)
  The content that markup happens on top of.
- [var contentView: NSView?](papermarkupviewcontroller/contentview-4hbkf.md)
  The content that markup happens on top of.
- [var contentVisibleFrame: CGRect](papermarkupviewcontroller/contentvisibleframe.md)
  The visible area of content in the scroll view.
- [var delegate: (any PaperMarkupViewController.Delegate)?](papermarkupviewcontroller/delegate-swift.property.md)
  The delegate for responding to user actions.
- [var directTouchAutomaticallyDraws: Bool](papermarkupviewcontroller/directtouchautomaticallydraws.md)
  A Boolean value that indicates that direct touches should automatically draw based on system state.
- [var directTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/directtouchmode.md)
  The interaction mode for direct touches on the canvas.
- [var drawingTool: any PKTool](papermarkupviewcontroller/drawingtool.md)
  The tool used to draw on the canvas.
- [var indirectPointerTouchMode: PaperMarkupViewController.TouchMode](papermarkupviewcontroller/indirectpointertouchmode.md)
  The interaction mode for indirect pointer touches on the canvas.
- [var isEditable: Bool](papermarkupviewcontroller/iseditable.md)
  A Boolean value that indicates whether the contents of the canvas is editable.
- [var isRulerActive: Bool](papermarkupviewcontroller/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
- [var markup: PaperMarkup?](papermarkupviewcontroller/markup.md)
  The paper data shown in this view controller.
- [var selectedMarkup: PaperMarkup](papermarkupviewcontroller/selectedmarkup.md)
  The selected contents in the UI.
- [var showsHorizontalScrollIndicator: Bool](papermarkupviewcontroller/showshorizontalscrollindicator.md)
  A Boolean value that controls whether the horizontal scroll indicator is visible.
- [var showsVerticalScrollIndicator: Bool](papermarkupviewcontroller/showsverticalscrollindicator.md)
  A Boolean value that controls whether the vertical scroll indicator is visible.
- [var supportedFeatureSet: FeatureSet](papermarkupviewcontroller/supportedfeatureset.md)
  The supported PaperKIt features on this canvas.
- [var undoManager: UndoManager?](papermarkupviewcontroller/undomanager.md)
- [var zoomRange: ClosedRange<CGFloat>](papermarkupviewcontroller/zoomrange.md)
  A floating-point range that specifies the minimum and maximum scale factor that can apply to the canvas’ content.
### Instance Methods
- [func loadView()](papermarkupviewcontroller/loadview.md)
- [func setContentVisibleFrame(CGRect, animated: Bool)](papermarkupviewcontroller/setcontentvisibleframe(_:animated:).md)
  Zooms to a specific area of the content so that it’s visible in the scroll view.
- [func suggestedFrameForInserting(contentInFrame: CGRect) -> CGRect](papermarkupviewcontroller/suggestedframeforinserting(contentinframe:).md)
  The frame that should be used for inserting shapes and other content.
- [func viewDidAppear()](papermarkupviewcontroller/viewdidappear.md)
- [func viewDidLayout()](papermarkupviewcontroller/viewdidlayout.md)
- [func viewDidLoad()](papermarkupviewcontroller/viewdidload.md)
### Enumerations
- [PaperMarkupViewController.TouchMode](papermarkupviewcontroller/touchmode.md)
  The canvas behavior for touches.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MarkupToolbarViewController.Delegate](markuptoolbarviewcontroller/delegate-swift.protocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Observable](../Observation/Observable.md)
- [PKToolPickerObserver](../PencilKit/PKToolPickerObserver.md)
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

- [class MarkupEditViewController](markupeditviewcontroller.md)
  A view controller that manages the interface for inserting content into a canvas.
- [class MarkupToolbarViewController](markuptoolbarviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller)*