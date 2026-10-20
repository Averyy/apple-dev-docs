# RPPreviewViewController

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

An object that displays a user interface where users preview and edit a screen recording that you create with ReplayKit.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use SCRecordingEditor instead

## Declaration

```swift
class RPPreviewViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface RPPreviewViewController : UIViewController
```

*macOS*

```objc
@interface RPPreviewViewController : NSViewController
```

#### Overview

Upon completion of a successful recording, the preview view controller is passed into the completion handler for [`stopRecording(handler:)`](./rpscreenrecorder/stoprecording%28handler%29.md).

## Topics

### Displaying the Preview UI
- [var mode: RPPreviewViewControllerMode](./rppreviewviewcontroller/mode.md)
  The type of screen that appears when the view is presented.
- [enum RPPreviewViewControllerMode](./rppreviewviewcontrollermode.md)
  The modes used to determine whether the preview view controller or the share screen appears when editing a replay.
- [var previewControllerDelegate: (any RPPreviewViewControllerDelegate)?](./rppreviewviewcontroller/previewcontrollerdelegate.md)
  The preview view controller’s delegate.
- [protocol RPPreviewViewControllerDelegate](./rppreviewviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a screen-recording user interface.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
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

### Replay Sharing
- [Recording and Streaming Your macOS App](./recording-and-streaming-your-macos-app.md)
  Share screen recordings, or broadcast live audio and video of your app, by adding ReplayKit to your macOS apps and games.
- [class RPScreenRecorder](./rpscreenrecorder.md)
  The shared recorder object that provides the ability to record audio and video of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller)*