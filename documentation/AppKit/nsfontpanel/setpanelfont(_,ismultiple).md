# setPanelFont(_:isMultiple:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the selected font in the receiver to the specified font.

**Availability**:
- macOS

## Declaration

```swift
func setPanelFont(_ fontObj: NSFont, isMultiple flag: Bool)
```

```objc
- (void) setPanelFont:(NSFont *) fontObj isMultiple:(BOOL) flag;
```

## Discussion

You normally don’t use this method directly; instead, you send [`setSelectedFont(_:isMultiple:)`](../nsfontmanager/setselectedfont%28_,ismultiple%29.md) to the shared `NSFontManager`, which in turn invokes this method.

## Parameters

- `fontObj`: The font to be selected.
- `flag`: If [`false`](../../Swift/false.md), selects the specified font; otherwise selects no font and displays a message in the preview area indicating that multiple fonts are selected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/setpanelfont(_:ismultiple:))*