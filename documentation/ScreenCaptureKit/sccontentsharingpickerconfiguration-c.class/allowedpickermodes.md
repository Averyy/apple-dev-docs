# allowedPickerModes

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The content-selection modes supported by the picker.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```objc
@property (nonatomic, assign) SCContentSharingPickerMode allowedPickerModes;
```

#### Discussion

The default value doesn’t exclude selecting any content for streaming. There isn’t an equivalent [`SCContentSharingPickerMode`](../sccontentsharingpickermode.md) available to reset this property once changed.

## See Also

### Control streaming selections
- [allowsChangingSelectedContent](./allowschangingselectedcontent.md)
  A Boolean value that indicates if the present stream can change to a different source.
- [excludedBundleIDs](./excludedbundleids.md)
  A list of bundle IDs to exclude from the sharing picker.
- [excludedWindowIDs](./excludedwindowids.md)
  A list of window IDs to exclude from the sharing picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerconfiguration-c.class/allowedpickermodes)*