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

## Mentions

- [Integrating PaperKit into your app](getting-started-with-paperkit.md)

## Topics

### Creating a toolbar
- [init(supportedFeatureSet: FeatureSet)](markuptoolbarviewcontroller/init(supportedfeatureset:).md)
  Creates a markup toolbar view controller.
- [init?(coder: NSCoder)](markuptoolbarviewcontroller/init(coder:).md)
### Configuring the toolbar
- [let supportedFeatureSet: FeatureSet](markuptoolbarviewcontroller/supportedfeatureset.md)
  The supported features of this toolbar.
- [var delegate: (any MarkupToolbarViewController.Delegate)?](markuptoolbarviewcontroller/delegate-swift.property.md)
  The delegate for responding to user actions.
### Managing touch modes
- [var indirectPointerTouchModes: [PaperMarkupViewController.TouchMode]](markuptoolbarviewcontroller/indirectpointertouchmodes.md)
  The modes available for a user to select.
- [var selectedIndirectPointerTouchMode: PaperMarkupViewController.TouchMode](markuptoolbarviewcontroller/selectedindirectpointertouchmode.md)
  The currently selected pointer mode.
### Managing drawing tools
- [var selectedDrawingTool: any PKTool](markuptoolbarviewcontroller/selecteddrawingtool.md)
  The currently selected drawing tool.
- [var selectedDrawingToolItem: PKToolPickerItem](markuptoolbarviewcontroller/selecteddrawingtoolitem.md)
  The currently selected drawing tool.
### Responding to changes
- [MarkupToolbarViewController.Delegate](markuptoolbarviewcontroller/delegate-swift.protocol.md)
  The delegate for a PaperKit toolbar.
### Managing view lifecycle
- [func viewDidLoad()](markuptoolbarviewcontroller/viewdidload.md)

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

- [class PaperMarkupViewController](papermarkupviewcontroller.md)
  A view controller for interactively creating and showing markup.
- [class MarkupEditViewController](markupeditviewcontroller.md)
  A view controller that manages the interface for inserting content into a canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller)*