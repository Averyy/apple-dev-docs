# RPPreviewViewController

**Framework**: ReplayKit  
**Kind**: class

An object that displays a user interface where users preview and edit a screen recording that you create with ReplayKit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class RPPreviewViewController
```

#### Overview

Upon completion of a successful recording, the preview view controller is passed into the completion handler for [`stopRecording(handler:)`](rpscreenrecorder/stoprecording(handler:).md).

## Topics

### Displaying the Preview UI
- [var mode: RPPreviewViewControllerMode](rppreviewviewcontroller/mode.md)
  The type of screen that appears when the view is presented.
- [enum RPPreviewViewControllerMode](rppreviewviewcontrollermode.md)
  The modes used to determine whether the preview view controller or the share screen appears when editing a replay.
- [var previewControllerDelegate: (any RPPreviewViewControllerDelegate)?](rppreviewviewcontroller/previewcontrollerdelegate.md)
  The preview view controller’s delegate.
- [protocol RPPreviewViewControllerDelegate](rppreviewviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a screen-recording user interface.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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

- [Recording and Streaming Your macOS App](recording-and-streaming-your-macos-app.md)
  Share screen recordings, or broadcast live audio and video of your app, by adding ReplayKit to your macOS apps and games.
- [class RPScreenRecorder](rpscreenrecorder.md)
  The shared recorder object that provides the ability to record audio and video of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rppreviewviewcontroller)*