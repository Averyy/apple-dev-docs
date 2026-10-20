# MarkupToolbarViewController

**Framework**: PaperKit  
**Kind**: class  
**Role**: Class

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class MarkupToolbarViewController
```

## Mentions

- [Integrating PaperKit into your app](./getting-started-with-paperkit.md)

## Topics

### Creating a toolbar
- [init(supportedFeatureSet: FeatureSet)](./markuptoolbarviewcontroller/init%28supportedfeatureset%29.md)
  Creates a markup toolbar view controller.
- [init?(coder: NSCoder)](./markuptoolbarviewcontroller/init%28coder%29.md)
### Configuring the toolbar
- [let supportedFeatureSet: FeatureSet](./markuptoolbarviewcontroller/supportedfeatureset.md)
  The supported features of this toolbar.
- [var delegate: (any MarkupToolbarViewController.Delegate)?](./markuptoolbarviewcontroller/delegate-swift.property.md)
  The delegate for responding to user actions.
### Managing touch modes
- [var indirectPointerTouchModes: [PaperMarkupViewController.TouchMode]](./markuptoolbarviewcontroller/indirectpointertouchmodes.md)
  The modes available for a user to select.
- [var selectedIndirectPointerTouchMode: PaperMarkupViewController.TouchMode](./markuptoolbarviewcontroller/selectedindirectpointertouchmode.md)
  The currently selected pointer mode.
### Managing drawing tools
- [var selectedDrawingTool: any PKTool](./markuptoolbarviewcontroller/selecteddrawingtool.md)
  The currently selected drawing tool.
- [var selectedDrawingToolItem: PKToolPickerItem](./markuptoolbarviewcontroller/selecteddrawingtoolitem.md)
  The currently selected drawing tool.
### Responding to changes
- [MarkupToolbarViewController.Delegate](./markuptoolbarviewcontroller/delegate-swift.protocol.md)
  The delegate for a PaperKit toolbar.
### Managing view lifecycle
- [func viewDidLoad()](./markuptoolbarviewcontroller/viewdidload%28%29.md)

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
- [class PaperMarkupViewController](./papermarkupviewcontroller.md)
  A view controller for interactively creating and showing markup.
- [class MarkupEditViewController](./markupeditviewcontroller.md)
  A view controller that manages the interface for inserting content into a canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller)*