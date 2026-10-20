# RPSystemBroadcastPickerView

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

A view displaying a broadcast button that, when tapped, shows a broadcast picker.

**Availability**:
- iOS 12.0+ - Deprecated in 27.0
- iPadOS 12.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCContentSharingPicker instead

## Declaration

```swift
class RPSystemBroadcastPickerView
```

```objc
@interface RPSystemBroadcastPickerView : UIView
```

#### Overview

Add this view to your view hierarchy to let users broadcast directly from your app. When a user taps the broadcast button, it displays a broadcast picker, allowing the user to select a broadcast provider.

> **Note**:  Clicking the broadcast button has no effect in Mac apps built with Mac Catalyst.

You can limit the picker to a particular broadcast provider by setting [`preferredExtension`](./rpsystembroadcastpickerview/preferredextension.md) to the bundle identifier of a broadcast extension. You can also show or hide the microphone button displayed in the picker by setting the [`showsMicrophoneButton`](./rpsystembroadcastpickerview/showsmicrophonebutton.md) property. Set these properties before presenting [`RPSystemBroadcastPickerView`](./rpsystembroadcastpickerview.md), as shown here:

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
- [var preferredExtension: String?](./rpsystembroadcastpickerview/preferredextension.md)
  A bundle identifier of a broadcast extension.
- [var showsMicrophoneButton: Bool](./rpsystembroadcastpickerview/showsmicrophonebutton.md)
  A Boolean value that indicates whether the microphone button is visible in the broadcast picker.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Live Broadcast Implementation
- [class RPBroadcastActivityViewController](./rpbroadcastactivityviewcontroller.md)
  A view controller that displays a user interface where users choose a broadcast service.
- [class RPBroadcastActivityController](./rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](./rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- [class RPBroadcastConfiguration](./rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpsystembroadcastpickerview)*