# SCContentSharingPickerConfiguration

**Framework**: ScreenCaptureKit  
**Kind**: struct

An instance for configuring the system content-sharing picker.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
struct SCContentSharingPickerConfiguration
```

## Topics

### Initializers
- [init()](sccontentsharingpickerconfiguration-swift.struct/init.md)
  Initializes a picker configuration with default values.
### Control streaming selections
- [var allowedPickerModes: SCContentSharingPickerMode](sccontentsharingpickerconfiguration-swift.struct/allowedpickermodes.md)
  The content-selection modes supported by the picker.
- [var allowsChangingSelectedContent: Bool](sccontentsharingpickerconfiguration-swift.struct/allowschangingselectedcontent.md)
  A Boolean value that indicates if the present stream can change to a different source.
- [var excludedBundleIDs: Array<String>](sccontentsharingpickerconfiguration-swift.struct/excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.
- [var excludedWindowIDs: Array<Int>](sccontentsharingpickerconfiguration-swift.struct/excludedwindowids.md)
  A list of window IDs to exclude from the sharing picker.

## See Also

- [class SCContentSharingPicker](sccontentsharingpicker.md)
  An instance of a picker presented by the operating system for managing frame-capture streams.
- [struct SCContentSharingPickerMode](sccontentsharingpickermode.md)
  Available modes for selecting streaming content from a picker presented by the operating system.
- [protocol SCContentSharingPickerObserver](sccontentsharingpickerobserver.md)
  An observer protocol your app implements to receive messages from the operating system’s content picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-swift.struct)*