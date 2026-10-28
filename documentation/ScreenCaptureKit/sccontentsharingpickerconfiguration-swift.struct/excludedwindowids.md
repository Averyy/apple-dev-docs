# excludedWindowIDs

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A list of window IDs to exclude from the sharing picker.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
var excludedWindowIDs: Array<Int>
```

## Discussion

> ❗ **Important**:  Using an invalid window ID can cause an error. Use window values returned from Core Graphics methods such as [`CGWindowListCopyWindowInfo(_:_:)`](../../CoreGraphics/cgwindowlistcopywindowinfo%28_,_%29.md) to provide window IDs to exclude from the picker.

## See Also

### Control streaming selections
- [var allowedPickerModes: SCContentSharingPickerMode](./allowedpickermodes.md)
  The content-selection modes supported by the picker.
- [var allowsChangingSelectedContent: Bool](./allowschangingselectedcontent.md)
  A Boolean value that indicates if the present stream can change to a different source.
- [var excludedBundleIDs: Array<String>](./excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-swift.struct/excludedwindowids)*