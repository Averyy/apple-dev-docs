# SCContentSharingPickerObserver

**Framework**: ScreenCaptureKit  
**Kind**: protocol

An observer protocol your app implements to receive messages from the operating system’s content picker.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
protocol SCContentSharingPickerObserver : NSObjectProtocol
```

## Topics

### Observing events
- [func contentSharingPicker(SCContentSharingPicker, didCancelFor: SCStream?)](sccontentsharingpickerobserver/contentsharingpicker(_:didcancelfor:).md)
  Tells the observer that a sharing picker canceled selection for a stream.
- [func contentSharingPicker(SCContentSharingPicker, didUpdateWith: SCContentFilter, for: SCStream?)](sccontentsharingpickerobserver/contentsharingpicker(_:didupdatewith:for:).md)
  Tells the observer that a sharing picker updated the content filter for a stream.
### Observing errors
- [func contentSharingPickerStartDidFailWithError(any Error)](sccontentsharingpickerobserver/contentsharingpickerstartdidfailwitherror(_:).md)
  Tells the observer that a sharing picker was unable to start.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SCContentSharingPicker](sccontentsharingpicker.md)
  An instance of a picker presented by the operating system for managing frame-capture streams.
- [struct SCContentSharingPickerConfiguration](sccontentsharingpickerconfiguration-swift.struct.md)
  An instance for configuring the system content-sharing picker.
- [struct SCContentSharingPickerMode](sccontentsharingpickermode.md)
  Available modes for selecting streaming content from a picker presented by the operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerobserver)*