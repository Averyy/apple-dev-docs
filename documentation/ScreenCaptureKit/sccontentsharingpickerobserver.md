# SCContentSharingPickerObserver

**Framework**: ScreenCaptureKit  
**Kind**: protocol  
**Role**: Protocol

An observer protocol your app implements to receive messages from the operating system’s content picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol SCContentSharingPickerObserver : NSObjectProtocol
```

```objc
@protocol SCContentSharingPickerObserver <NSObject>
```

## Topics

### Observing events
- [func contentSharingPicker(SCContentSharingPicker, didCancelFor: SCStream?)](./sccontentsharingpickerobserver/contentsharingpicker%28_,didcancelfor%29.md)
  Tells the observer that a sharing picker canceled selection for a stream.
- [func contentSharingPicker(SCContentSharingPicker, didUpdateWith: SCContentFilter, for: SCStream?)](./sccontentsharingpickerobserver/contentsharingpicker%28_,didupdatewith,for%29.md)
  Tells the observer that a sharing picker updated the content filter for a stream.
### Observing errors
- [func contentSharingPickerStartDidFailWithError(any Error)](./sccontentsharingpickerobserver/contentsharingpickerstartdidfailwitherror%28_%29.md)
  Tells the observer that a sharing picker was unable to start.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### System content-sharing picker
- [class SCContentSharingPicker](./sccontentsharingpicker.md)
  An instance of a picker presented by the operating system for managing frame-capture streams.
- [struct SCContentSharingPickerConfiguration](./sccontentsharingpickerconfiguration-swift.struct.md)
  An instance for configuring the system content-sharing picker.
- [struct SCContentSharingPickerMode](./sccontentsharingpickermode.md)
  Available modes for selecting streaming content from a picker presented by the operating system.
- [SCContentSharingPickerConfiguration](./sccontentsharingpickerconfiguration-c.class.md)
  An instance for configuring the system content-sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerobserver)*