# AVCaptureView

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A view that displays standard user interface controls for capturing media data.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class AVCaptureView
```

```objc
@interface AVCaptureView : NSView
```

## Topics

### Configuring the capture session
- [var session: AVCaptureSession?](./avcaptureview/session.md)
  The view’s associated capture session.
- [func setSession(AVCaptureSession?, showVideoPreview: Bool, showAudioPreview: Bool)](./avcaptureview/setsession%28_,showvideopreview,showaudiopreview%29.md)
  Sets the view’s capture session.
### Customizing the view
- [var controlsStyle: AVCaptureViewControlsStyle](./avcaptureview/controlsstyle.md)
  The style of the capture controls presented by the view.
- [enum AVCaptureViewControlsStyle](./avcaptureviewcontrolsstyle.md)
  Constants that describe the capture view’s supported controls styles.
- [var videoGravity: AVLayerVideoGravity](./avcaptureview/videogravity.md)
  A string value that defines how the capture view displays video within its bounds.
### Configuring the delegate
- [var delegate: (any AVCaptureViewDelegate)?](./avcaptureview/delegate.md)
  The capture view’s delegate object.
- [protocol AVCaptureViewDelegate](./avcaptureviewdelegate.md)
  The protocol that defines the methods you can implement to respond to capture view events.
### Recording media
- [var fileOutput: AVCaptureFileOutput?](./avcaptureview/fileoutput.md)
  The capture file output used to record media data.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Capture views
- [protocol AVCaptureViewDelegate](./avcaptureviewdelegate.md)
  The protocol that defines the methods you can implement to respond to capture view events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureview)*