# allowsChangingSelectedContent

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the present stream can change to a different source.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var allowsChangingSelectedContent: Bool
```

#### Discussion

The default value is `true`.

## See Also

### Control streaming selections
- [var allowedPickerModes: SCContentSharingPickerMode](./allowedpickermodes.md)
  The content-selection modes supported by the picker.
- [var excludedBundleIDs: Array<String>](./excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.
- [var excludedWindowIDs: Array<Int>](./excludedwindowids.md)
  A list of window IDs to exclude from the sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-swift.struct/allowschangingselectedcontent)*