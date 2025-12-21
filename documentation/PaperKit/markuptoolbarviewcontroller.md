# MarkupToolbarViewController

**Framework**: PaperKit  
**Kind**: class

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class MarkupToolbarViewController
```

## Topics

### Protocols
- [MarkupToolbarViewController.Delegate](markuptoolbarviewcontroller/delegate-swift.protocol.md)
### Initializers
- [init?(coder: NSCoder)](markuptoolbarviewcontroller/init(coder:).md)
- [init(supportedFeatureSet: FeatureSet)](markuptoolbarviewcontroller/init(supportedfeatureset:).md)
  Creates a markup toolbar view controller.
### Instance Properties
- [var delegate: (any MarkupToolbarViewController.Delegate)?](markuptoolbarviewcontroller/delegate-swift.property.md)
  The delegate for responding to user actions.
- [var indirectPointerTouchModes: [PaperMarkupViewController.TouchMode]](markuptoolbarviewcontroller/indirectpointertouchmodes.md)
  The modes available for a user to select.
- [var selectedDrawingTool: any PKTool](markuptoolbarviewcontroller/selecteddrawingtool.md)
  The currently selected drawing tool.
- [var selectedDrawingToolItem: PKToolPickerItem](markuptoolbarviewcontroller/selecteddrawingtoolitem.md)
  The currently selected drawing tool.
- [var selectedIndirectPointerTouchMode: PaperMarkupViewController.TouchMode](markuptoolbarviewcontroller/selectedindirectpointertouchmode.md)
  The currently selected pointer mode.
- [let supportedFeatureSet: FeatureSet](markuptoolbarviewcontroller/supportedfeatureset.md)
  The supported features of this toolbar.
### Instance Methods
- [func viewDidLoad()](markuptoolbarviewcontroller/viewdidload.md)

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

- [class PaperMarkupViewController](papermarkupviewcontroller.md)
  A view controller for interactively creating, and showing markup.
- [class MarkupEditViewController](markupeditviewcontroller.md)
  A view controller that manages the interface for inserting content into a canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller)*