# setHelpAnchor(_:)

**Framework**: Security Interface  
**Kind**: method

Sets the help anchor string for the sheet or modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setHelpAnchor(_ anchor: String!)
```

#### Discussion

You may call this function to set a help anchor string if you display a help button in the sheet or modal panel and do not implement the delegate method [`certificatePanelShowHelp(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/certificatePanelShowHelp(_:)), or if the delegate method returns [`false`](https://developer.apple.com/documentation/Swift/false). If you display a help button, do not set a help anchor string, and do not implement a delegate, the certificate panel displays a default help page (“Why isn’t a certificate being accepted?”).

## Parameters

- `anchor`: The new help anchor string.

## See Also

- [func helpAnchor() -> String!](sfcertificatepanel/helpanchor.md)
  Returns the current help anchor string for the sheet or panel.
- [func setShowsHelp(Bool)](sfcertificatepanel/setshowshelp(_:).md)
  Displays a Help button in the sheet or panel.
- [func certificatePanelShowHelp(_ sender: SFCertificatePanel!) -> Bool](../ObjectiveC/NSObject-swift.class/certificatePanelShowHelp(_:).md)
  Implements custom help behavior for the modal panel.
- [func setShowsHelp(Bool)](sfcertificatepanel/setshowshelp(_:).md)
  Displays a Help button in the sheet or panel.
- [func helpAnchor() -> String!](sfcertificatepanel/helpanchor.md)
  Returns the current help anchor string for the sheet or panel.
- [func showsHelp() -> Bool](sfcertificatepanel/showshelp.md)
  Indicates whether the help button is currently set to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/sethelpanchor(_:))*