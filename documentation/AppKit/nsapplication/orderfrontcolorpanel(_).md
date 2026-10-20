# orderFrontColorPanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Brings up the color panel, an instance of `NSColorPanel`.

**Availability**:
- macOS

## Declaration

```swift
func orderFrontColorPanel(_ sender: Any?)
```

```objc
- (void) orderFrontColorPanel:(id) sender;
```

#### Discussion

If the `NSColorPanel` object does not exist yet, this method creates one. This method is typically invoked when the user chooses Colors from a menu.

## Parameters

- `sender`: The object that sent the command.

## See Also

### Managing Panels
- [func orderFrontStandardAboutPanel(Any?)](./orderfrontstandardaboutpanel%28_%29.md)
  Displays a standard About window.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](./orderfrontstandardaboutpanel%28options%29.md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](./orderfrontcharacterpalette%28_%29.md)
  Opens the character palette.
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/orderfrontcolorpanel(_:))*