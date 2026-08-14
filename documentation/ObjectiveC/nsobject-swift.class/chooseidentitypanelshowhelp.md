# chooseIdentityPanelShowHelp(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Implements custom help behavior for the modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func chooseIdentityPanelShowHelp(_ sender: SFChooseIdentityPanel!) -> Bool
```

#### Discussion

You can use this delegate method to implement custom help if you call the [`setShowsHelp(_:)`](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setshowshelp(_:)) method to display a help button in the sheet or panel. If you are not implementing custom help, do not implement this method.

## Parameters

- `sender`: The choose identity panel for which to implement custom help.

## See Also

- [func setShowsHelp(Bool)](../securityinterface/sfchooseidentitypanel/setshowshelp(_:).md)
  Displays a Help button in the sheet or panel.
- [var delegate: (any NSWindowDelegate)?](../appkit/nswindow/delegate.md)
  The window’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/chooseidentitypanelshowhelp(_:))*