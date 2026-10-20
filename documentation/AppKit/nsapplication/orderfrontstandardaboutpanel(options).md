# orderFrontStandardAboutPanel(options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays a standard About window with information from a given options dictionary.

**Availability**:
- macOS

## Declaration

```swift
func orderFrontStandardAboutPanel(options optionsDictionary: [NSApplication.AboutPanelOptionKey : Any] = [:])
```

```objc
- (void) orderFrontStandardAboutPanelWithOptions:(NSDictionary<NSString *,id> *) optionsDictionary;
```

#### Discussion

In addition to the keys in AboutPanelOptionKey, you may also include the following key in `optionsDictionary`:

- `@``"Copyright"`: An `NSString` object with a line of copyright information. If not specified, this method then looks for the value of `NSHumanReadableCopyright` in the localized version of the app’s `Info.plist` file. If neither is available, this method leaves the space blank.

## Parameters

- `optionsDictionary`: A dictionary whose keys define the contents of the About window. For a list of keys, see [`NSApplication.AboutPanelOptionKey`](./aboutpaneloptionkey.md).

## See Also

### Managing Panels
- [func orderFrontColorPanel(Any?)](./orderfrontcolorpanel%28_%29.md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](./orderfrontstandardaboutpanel%28_%29.md)
  Displays a standard About window.
- [func orderFrontCharacterPalette(Any?)](./orderfrontcharacterpalette%28_%29.md)
  Opens the character palette.
- [func runPageLayout(Any?)](./runpagelayout%28_%29.md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](./aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/orderfrontstandardaboutpanel(options:))*