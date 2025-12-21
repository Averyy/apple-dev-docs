# setShowsHelp(_:)

**Framework**: Security Interface  
**Kind**: method

Displays a Help button in the sheet or panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setShowsHelp(_ showsHelp: Bool)
```

#### Discussion

When a user clicks the help button, the certificate panel first checks the delegate for a [`certificatePanelShowHelp(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/certificatePanelShowHelp(_:)) method. If the delegate does not implement such a method, or the delegate method returns [`false`](https://developer.apple.com/documentation/Swift/false), then the [`NSHelpManager`](https://developer.apple.com/documentation/AppKit/NSHelpManager) method [`openHelpAnchor(_:inBook:)`](https://developer.apple.com/documentation/AppKit/NSHelpManager/openHelpAnchor(_:inBook:)) is called with a `nil` book and the anchor specified by the [`setHelpAnchor(_:)`](sfcertificatepanel/sethelpanchor(_:).md) method. An exception is raised if the delegate returns [`false`](https://developer.apple.com/documentation/Swift/false) and there is no help anchor set.

## Parameters

- `showsHelp`: Set to   to display the help button. The help button is hidden by default.

## See Also

- [@MainActor func openHelpAnchor(_ anchor: NSHelpManager.AnchorName, inBook book: NSHelpManager.BookName?)](../AppKit/NSHelpManager/openHelpAnchor(_:inBook:).md)
  Finds and displays the text at the given anchor location in the given book.
- [func showsHelp() -> Bool](sfcertificatepanel/showshelp.md)
  Indicates whether the help button is currently set to be displayed.
- [func certificatePanelShowHelp(_ sender: SFCertificatePanel!) -> Bool](../ObjectiveC/NSObject-swift.class/certificatePanelShowHelp(_:).md)
  Implements custom help behavior for the modal panel.
- [func setHelpAnchor(String!)](sfcertificatepanel/sethelpanchor(_:).md)
  Sets the help anchor string for the sheet or modal panel.
- [func helpAnchor() -> String!](sfcertificatepanel/helpanchor.md)
  Returns the current help anchor string for the sheet or panel.
- [func showsHelp() -> Bool](sfcertificatepanel/showshelp.md)
  Indicates whether the help button is currently set to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/setshowshelp(_:))*