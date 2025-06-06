# orderFrontStandardAboutPanel(_:)

**Framework**: AppKit  
**Kind**: method

Displays a standard About window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func orderFrontStandardAboutPanel(_ sender: Any?)
```

#### Discussion

This method calls [`orderFrontStandardAboutPanel(options:)`](nsapplication/orderfrontstandardaboutpanel(options:).md) with a `nil` argument. See [`orderFrontStandardAboutPanel(options:)`](nsapplication/orderfrontstandardaboutpanel(options:).md) for a description of what’s displayed.

## Parameters

- `sender`: The object that sent the command.

## See Also

- [func orderFrontColorPanel(Any?)](nsapplication/orderfrontcolorpanel(_:).md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](nsapplication/orderfrontstandardaboutpanel(options:).md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](nsapplication/orderfrontcharacterpalette(_:).md)
  Opens the character palette.
- [func runPageLayout(Any?)](nsapplication/runpagelayout(_:).md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/orderfrontstandardaboutpanel(_:))*