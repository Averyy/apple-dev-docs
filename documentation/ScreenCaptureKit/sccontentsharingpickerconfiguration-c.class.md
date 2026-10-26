# SCContentSharingPickerConfiguration

**Framework**: ScreenCaptureKit  
**Kind**: class  
**Role**: Class

An instance for configuring the system content-sharing picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```objc
@interface SCContentSharingPickerConfiguration : NSObject
```

## Topics

### Control streaming selections
- [allowedPickerModes](./sccontentsharingpickerconfiguration-c.class/allowedpickermodes.md)
  The content-selection modes supported by the picker.
- [allowsChangingSelectedContent](./sccontentsharingpickerconfiguration-c.class/allowschangingselectedcontent.md)
  A Boolean value that indicates if the present stream can change to a different source.
- [excludedBundleIDs](./sccontentsharingpickerconfiguration-c.class/excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.
- [excludedWindowIDs](./sccontentsharingpickerconfiguration-c.class/excludedwindowids.md)
  A list of window IDs to exclude from the sharing picker.
### Instance Properties
- [showsCameraControl](./sccontentsharingpickerconfiguration-c.class/showscameracontrol.md)
- [showsMicrophoneControl](./sccontentsharingpickerconfiguration-c.class/showsmicrophonecontrol.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### System content-sharing picker
- [class SCContentSharingPicker](./sccontentsharingpicker.md)
  An instance of a picker presented by the operating system for managing frame-capture streams.
- [struct SCContentSharingPickerMode](./sccontentsharingpickermode.md)
  Available modes for selecting streaming content from a picker presented by the operating system.
- [protocol SCContentSharingPickerObserver](./sccontentsharingpickerobserver.md)
  An observer protocol your app implements to receive messages from the operating system’s content picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-c.class)*