# RPSystemBroadcastPickerView

**Framework**: ReplayKit  
**Kind**: class

A view displaying a broadcast button that, when tapped, shows a broadcast picker.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class RPSystemBroadcastPickerView
```

#### Overview

Add this view to your view hierarchy to let users broadcast directly from your app. When a user taps the broadcast button, it displays a broadcast picker, allowing the user to select a broadcast provider.

> **Note**:  Clicking the broadcast button has no effect in Mac apps built with Mac Catalyst.

You can limit the picker to a particular broadcast provider by setting [`preferredExtension`](rpsystembroadcastpickerview/preferredextension.md) to the bundle identifier of a broadcast extension. You can also show or hide the microphone button displayed in the picker by setting the [`showsMicrophoneButton`](rpsystembroadcastpickerview/showsmicrophonebutton.md) property. Set these properties before presenting [`RPSystemBroadcastPickerView`](rpsystembroadcastpickerview.md), as shown here:

```swift
class ViewController: UIViewController {

    @IBOutlet var containerView: UIView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
     
        let broadcastPicker = RPSystemBroadcastPickerView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
        broadcastPicker.preferredExtension = "com.your-app.broadcast.extension"

        containerView.addSubview(broadcastPicker)
    }
    
}

```

## Topics

### Configuring the Broadcast Picker
- [var preferredExtension: String?](rpsystembroadcastpickerview/preferredextension.md)
  A bundle identifier of a broadcast extension.
- [var showsMicrophoneButton: Bool](rpsystembroadcastpickerview/showsmicrophonebutton.md)
  A Boolean value that indicates whether the microphone button is visible in the broadcast picker.

## Relationships

### Inherits From
- [UIView](../uikit/uiview.md)
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
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class RPBroadcastActivityViewController](rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPBroadcastActivityController](rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- [class RPBroadcastConfiguration](rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpsystembroadcastpickerview)*