# UIPasteControl

**Framework**: UIKit  
**Kind**: class

A button that a person taps to place pasteboard contents in your app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPasteControl
```

#### Overview

You can configure the button to appear as an icon, text, or both. The following button represents the icon and text option:

![A screenshot of a pill-shaped button with an icon of a paper sheet on top of a clipboard, and text that says Paste.](/images/com.apple.uikit/media-4085675@2x.png)

In iOS 16 and later, programmatic pasting raises a user alert that prompts the user for approval before the app gains access to pasteboard contents (`UIPasteboard.general.string`). Use this class to paste without a user prompt.

##### Add a Paste Button to a Text View

The following code displays a paste button and assigns a text view as the recipient of pasteboard contents:

```swift
let textView = UITextView(frame: view.bounds)
view.addSubview(textView)

let configuration = UIPasteControl.Configuration()
configuration.baseBackgroundColor = .red
configuration.baseForegroundColor = .magenta
configuration.cornerStyle = .capsule
configuration.displayMode = .iconAndLabel
                    
let pasteButton = UIPasteControl(configuration: configuration)
pasteButton.frame = CGRect(x: view.bounds.width/2.0, y: view.bounds.height/2.0, width: 150, height: 60)
textView.addSubview(pasteButton)

pasteButton.target = textView
```

## Topics

### Creating a paste button
- [init?(coder: NSCoder)](uipastecontrol/init(coder:).md)
  Creates a paste button by deserializing the specified coder.
- [init(configuration: UIPasteControl.Configuration)](uipastecontrol/init(configuration:).md)
  Creates a paste button that conforms to the specified configuration.
- [init(frame: CGRect)](uipastecontrol/init(frame:).md)
  Creates a paste button with the specified size and position.
### Identifying the content recipient
- [var target: (any UIPasteConfigurationSupporting)?](uipastecontrol/target.md)
  The UI control that receives pasted content.
### Determining the button’s look
- [var configuration: UIPasteControl.Configuration](uipastecontrol/configuration-swift.property.md)
  An object that customizes the look of the paste button.
- [UIPasteControl.Configuration](uipastecontrol/configuration-swift.class.md)
  An object that determines a paste button’s color, corner style, icon, and text.

## Relationships

### Inherits From
- [UIControl](uicontrol.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [UIPasteControl.Configuration](uipastecontrol/configuration-swift.class.md)
  An object that determines a paste button’s color, corner style, icon, and text.
- [UIPasteControl.DisplayMode](uipastecontrol/displaymode.md)
  Options that determine whether a paste button composes an icon, textual label, or both.
- [class UIPasteboard](uipasteboard.md)
  An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [class UIPasteConfiguration](uipasteconfiguration.md)
  The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [protocol UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
  The interface that determines whether a responder object supports paste configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipastecontrol)*