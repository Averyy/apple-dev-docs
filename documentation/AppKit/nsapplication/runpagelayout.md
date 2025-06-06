# runPageLayout(_:)

**Framework**: AppKit  
**Kind**: method

Displays the receiver’s page layout panel, an instance of `NSPageLayout`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runPageLayout(_ sender: Any?)
```

#### Discussion

If the `NSPageLayout` instance does not exist, this method creates one. This method is typically invoked when the user chooses Page Setup from the app’s File menu.

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func orderFrontColorPanel(Any?)](nsapplication/orderfrontcolorpanel(_:).md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](nsapplication/orderfrontstandardaboutpanel(_:).md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](nsapplication/orderfrontstandardaboutpanel(options:).md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](nsapplication/orderfrontcharacterpalette(_:).md)
  Opens the character palette.
- [NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/runpagelayout(_:))*