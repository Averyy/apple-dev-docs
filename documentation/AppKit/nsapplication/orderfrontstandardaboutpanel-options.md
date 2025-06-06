# orderFrontStandardAboutPanel(options:)

**Framework**: AppKit  
**Kind**: method

Displays a standard About window with information from a given options dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func orderFrontStandardAboutPanel(options optionsDictionary: [NSApplication.AboutPanelOptionKey : Any] = [:])
```

#### Discussion

In addition to the keys in AboutPanelOptionKey, you may also include the following key in `optionsDictionary`:

- `@``"Copyright"`: An `NSString` object with a line of copyright information. If not specified, this method then looks for the value of `NSHumanReadableCopyright` in the localized version of the app’s `Info.plist` file. If neither is available, this method leaves the space blank.

## Parameters

- `optionsDictionary`: A dictionary whose keys define the contents of the About window. For a list of keys, see  .

## See Also

- [func orderFrontColorPanel(Any?)](nsapplication/orderfrontcolorpanel(_:).md)
  Brings up the color panel, an instance of `NSColorPanel`.
- [func orderFrontStandardAboutPanel(Any?)](nsapplication/orderfrontstandardaboutpanel(_:).md)
  Displays a standard About window.
- [func orderFrontCharacterPalette(Any?)](nsapplication/orderfrontcharacterpalette(_:).md)
  Opens the character palette.
- [func runPageLayout(Any?)](nsapplication/runpagelayout(_:).md)
  Displays the receiver’s page layout panel, an instance of `NSPageLayout`.
- [NSApplication.AboutPanelOptionKey](nsapplication/aboutpaneloptionkey.md)
  Keys to include in the options dictionary when displaying an About panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/orderfrontstandardaboutpanel(options:))*