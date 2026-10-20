# runPageLayout(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the receiver’s page layout panel, an instance of `NSPageLayout`.

**Availability**:
- macOS

## Declaration

```swift
func runPageLayout(_ sender: Any?)
```

```objc
- (void) runPageLayout:(id) sender;
```

#### Discussion

If the `NSPageLayout` instance does not exist, this method creates one. This method is typically invoked when the user chooses Page Setup from the app’s File menu.

## Parameters

- `sender`: The object that sent the command.

## See Also

### Managing Panels
- [func orderFrontColorPanel(Any?)](./orderfrontcolorpanel%28_%29.md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](./orderfrontstandardaboutpanel%28_%29.md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](./orderfrontstandardaboutpanel%28options%29.md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](./orderfrontcharacterpalette%28_%29.md)
  Opens the character palette.
- [NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/runpagelayout(_:))*