# orderFrontStandardAboutPanel(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays a standard About window.

**Availability**:
- macOS

## Declaration

```swift
func orderFrontStandardAboutPanel(_ sender: Any?)
```

```objc
- (void) orderFrontStandardAboutPanel:(id) sender;
```

#### Discussion

This method calls [`orderFrontStandardAboutPanel(options:)`](./orderfrontstandardaboutpanel%28options%29.md) with a `nil` argument. See [`orderFrontStandardAboutPanel(options:)`](./orderfrontstandardaboutpanel%28options%29.md) for a description of what’s displayed.

## Parameters

- `sender`: The object that sent the command.

## See Also

### Managing Panels
- [func orderFrontColorPanel(Any?)](./orderfrontcolorpanel%28_%29.md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(options: [NSApplication.AboutPanelOptionKey : Any])](./orderfrontstandardaboutpanel%28options%29.md)
  Displays a standard About window with information from a given options dictionary.
- [func orderFrontCharacterPalette(Any?)](./orderfrontcharacterpalette%28_%29.md)
  Opens the character palette.
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/orderfrontstandardaboutpanel(_:))*