# setHelpAnchor(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Sets the help anchor string for the sheet or modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setHelpAnchor(_ anchor: String!)
```

```objc
- (void) setHelpAnchor:(NSString *) anchor;
```

## Discussion

You may call this function to set a help anchor string if you display a help button in the sheet or modal panel and do not implement the delegate method [`certificatePanelShowHelp(_:)`](../../ObjectiveC/nsobject-swift.class/certificatepanelshowhelp%28_%29.md), or if the delegate method returns [`false`](../../Swift/false.md). If you display a help button, do not set a help anchor string, and do not implement a delegate, the certificate panel displays a default help page (“Why isn’t a certificate being accepted?”).

## Parameters

- `anchor`: The new help anchor string.

## See Also

### Related Documentation
- [func helpAnchor() -> String!](./helpanchor%28%29.md)
  Returns the current help anchor string for the sheet or panel.
- [func setShowsHelp(Bool)](./setshowshelp%28_%29.md)
  Displays a Help button in the sheet or panel.
- [func certificatePanelShowHelp(SFCertificatePanel!) -> Bool](../../ObjectiveC/nsobject-swift.class/certificatepanelshowhelp%28_%29.md)
  Implements custom help behavior for the modal panel.
### Providing Help
- [func setShowsHelp(Bool)](./setshowshelp%28_%29.md)
  Displays a Help button in the sheet or panel.
- [func helpAnchor() -> String!](./helpanchor%28%29.md)
  Returns the current help anchor string for the sheet or panel.
- [func showsHelp() -> Bool](./showshelp%28%29.md)
  Indicates whether the help button is currently set to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/sethelpanchor(_:))*