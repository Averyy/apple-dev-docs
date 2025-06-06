# allowedPickerModes

**Framework**: ScreenCaptureKit  
**Kind**: property

The content-selection modes supported by the picker.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var allowedPickerModes: SCContentSharingPickerMode
```

#### Discussion

The default value doesn’t exclude selecting any content for streaming. There isn’t an equivalent [`SCContentSharingPickerMode`](sccontentsharingpickermode.md) available to reset this property once changed.

## See Also

- [var allowsChangingSelectedContent: Bool](sccontentsharingpickerconfiguration-swift.struct/allowschangingselectedcontent.md)
  A Boolean value that indicates if the present stream can change to a different source.
- [var excludedBundleIDs: Array<String>](sccontentsharingpickerconfiguration-swift.struct/excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.
- [var excludedWindowIDs: Array<Int>](sccontentsharingpickerconfiguration-swift.struct/excludedwindowids.md)
  A list of window IDs to exclude from the sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-swift.struct/allowedpickermodes)*