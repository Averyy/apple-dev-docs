# beginSheet(for:modalDelegate:didEnd:contextInfo:trust:showGroup:)

**Framework**: Security Interface  
**Kind**: method

Displays a certificate chain in a modal sheet.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func beginSheet(for docWindow: NSWindow!, modalDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, showGroup: Bool)
```

#### Discussion

The sheet displays the leaf certificate plus any other certificates in the certificate chain that the Security Server can find.

The delegate method has the following signature:

```objc
-(void)certificateSheetDidEnd:(NSWindow *)sheet
       returnCode:(NSInteger)returnCode
       contextInfo:(void *)contextInfo
```

The parameters for the delegate method are:

The delegate method may dismiss the keychain settings sheet itself; if it does not, the sheet is dismissed on return from the `beginSheetForDirectory:...` method.

## Parameters

- `docWindow`: The parent window to which the sheet is attached.
- `delegate`: The delegate object in which the method specified in the   parameter is implemented.
- `didEndSelector`: A selector for a delegate method called when the sheet has been dismissed. Implementation of this delegate method is optional.
- `contextInfo`: A pointer to data that is passed to the delegate method. You can use this data pointer for any purpose you wish.
- `trust`: A   object for the certificates to be displayed.
- `showGroup`: Specifies whether additional certificates (other than the leaf certificate) are displayed.

## See Also

- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, certificates: [Any]!, showGroup: Bool)](sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:certificates:showgroup:).md)
  Displays one or more certificates in a modal sheet.
- [func certificateView() -> SFCertificateView!](sfcertificatepanel/certificateview.md)
  Returns the certificate view for the modal panel.
- [func runModal(for: SecTrust!, showGroup: Bool) -> Int](sfcertificatepanel/runmodal(for:showgroup:).md)
  Displays a certificate chain in a modal panel.
- [func runModal(forCertificates: [Any]!, showGroup: Bool) -> Int](sfcertificatepanel/runmodal(forcertificates:showgroup:).md)
  Displays one or more specified certificates in a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:showgroup:))*