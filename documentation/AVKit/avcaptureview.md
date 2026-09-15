# AVCaptureView

**Framework**: AVKit  
**Kind**: class

A view that displays standard user interface controls for capturing media data.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class AVCaptureView
```

## Topics

### Configuring the Capture Session
- [var session: AVCaptureSession?](avcaptureview/session.md)
  The view’s associated capture session.
- [func setSession(AVCaptureSession?, showVideoPreview: Bool, showAudioPreview: Bool)](avcaptureview/setsession(_:showvideopreview:showaudiopreview:).md)
  Sets the view’s capture session.
### Customizing the View
- [var controlsStyle: AVCaptureViewControlsStyle](avcaptureview/controlsstyle.md)
  The style of the capture controls presented by the view.
- [enum AVCaptureViewControlsStyle](avcaptureviewcontrolsstyle.md)
  Constants that describe the capture view’s supported controls styles.
- [var videoGravity: AVLayerVideoGravity](avcaptureview/videogravity.md)
  A string value that defines how the capture view displays video within its bounds.
### Configuring the Delegate
- [var delegate: (any AVCaptureViewDelegate)?](avcaptureview/delegate.md)
  The capture view’s delegate object.
- [protocol AVCaptureViewDelegate](avcaptureviewdelegate.md)
  The protocol that defines the methods you can implement to respond to capture view events.
### Recording Media
- [var fileOutput: AVCaptureFileOutput?](avcaptureview/fileoutput.md)
  The capture file output used to record media data.

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)

## See Also

- [Implementing Trimming in a macOS Player](implementing-trimming-in-a-macos-player.md)
  Provide a QuickTime media-trimming experience in your macOS app.
- [class AVPlayerView](avplayerview.md)
  A view that displays content from a player and presents a native user interface to control playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview)*