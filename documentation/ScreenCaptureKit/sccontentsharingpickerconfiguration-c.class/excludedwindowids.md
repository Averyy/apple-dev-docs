# excludedWindowIDs

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

A list of window IDs to exclude from the sharing picker.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```objc
@property (nonatomic, strong) NSArray<NSNumber *> * excludedWindowIDs;
```

#### Discussion

> ❗ **Important**:  Using an invalid window ID can cause an error. Use [`CGWindowID`](../../CoreGraphics/cgwindowid.md) values provided by methods such as [`CGWindowListCopyWindowInfo(_:_:)`](../../CoreGraphics/cgwindowlistcopywindowinfo%28_,_%29.md) or a stream window’s [`windowID`](../scwindow/windowid.md) property.

## See Also

### Control streaming selections
- [allowedPickerModes](./allowedpickermodes.md)
  The content-selection modes supported by the picker.
- [allowsChangingSelectedContent](./allowschangingselectedcontent.md)
  A Boolean value that indicates if the present stream can change to a different source.
- [excludedBundleIDs](./excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-c.class/excludedwindowids)*