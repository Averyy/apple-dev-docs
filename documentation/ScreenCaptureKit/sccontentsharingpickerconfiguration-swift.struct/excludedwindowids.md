# excludedWindowIDs

**Framework**: ScreenCaptureKit  
**Kind**: property

A list of window IDs to exclude from the sharing picker.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var excludedWindowIDs: Array<Int>
```

#### Discussion

> ❗ **Important**:  Using an invalid window ID can cause an error. Use window values returned from Core Graphics methods such as [`CGWindowListCopyWindowInfo(_:_:)`](https://developer.apple.com/documentation/CoreGraphics/CGWindowListCopyWindowInfo(_:_:)) to provide window IDs to exclude from the picker.

 Using an invalid window ID can cause an error. Use window values returned from Core Graphics methods such as [`CGWindowListCopyWindowInfo(_:_:)`](https://developer.apple.com/documentation/CoreGraphics/CGWindowListCopyWindowInfo(_:_:)) to provide window IDs to exclude from the picker.

## See Also

- [var allowedPickerModes: SCContentSharingPickerMode](sccontentsharingpickerconfiguration-swift.struct/allowedpickermodes.md)
  The content-selection modes supported by the picker.
- [var allowsChangingSelectedContent: Bool](sccontentsharingpickerconfiguration-swift.struct/allowschangingselectedcontent.md)
  A Boolean value that indicates if the present stream can change to a different source.
- [var excludedBundleIDs: Array<String>](sccontentsharingpickerconfiguration-swift.struct/excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-swift.struct/excludedwindowids)*