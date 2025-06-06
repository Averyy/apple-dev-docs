# orderFrontColorPanel(_:)

**Framework**: AppKit  
**Kind**: method

Brings up the color panel, an instance of `NSColorPanel`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func orderFrontColorPanel(_ sender: Any?)
```

#### Discussion

If the `NSColorPanel` object does not exist yet, this method creates one. This method is typically invoked when the user chooses Colors from a menu.

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func orderFrontStandardAboutPanel(Any?)](nsapplication/orderfrontstandardaboutpanel(_:).md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](nsapplication/orderfrontstandardaboutpanel(options:).md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](nsapplication/orderfrontcharacterpalette(_:).md)
  Opens the character palette.
- [func runPageLayout(Any?)](nsapplication/runpagelayout(_:).md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/orderfrontcolorpanel(_:))*