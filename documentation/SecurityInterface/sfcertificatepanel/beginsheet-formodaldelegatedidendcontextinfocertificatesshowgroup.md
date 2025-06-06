# beginSheet(for:modalDelegate:didEnd:contextInfo:certificates:showGroup:)

**Framework**: Security Interface  
**Kind**: method

Displays one or more certificates in a modal sheet.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func beginSheet(for docWindow: NSWindow!, modalDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!, certificates: [Any]!, showGroup: Bool)
```

#### Discussion

The behavior of this method is somewhat different in macOS 10.4 and later versus OS X v10.3. In OS X v10.3, the sheet displays whatever certificates you pass in the `certificates` parameter (provided the `showGroup` parameter is set to [`true`](https://developer.apple.com/documentation/swift/true)). Starting with OS X v10.4, the sheet displays the leaf certificate (that is, the first certificate in the array you pass) plus any other certificates in the certificate chain that the Security Server can find. If you include all of the certificates in the chain in the `certificates` parameter, you can ensure that the same certificates are displayed whatever the version of the operating system, and may decrease the time required to find and display the certificates in macOS 10.4 and later.

The delegate method has the following signature:

```objc
- (void)certificateSheetDidEnd:(NSWindow *)sheet
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
- `certificates`: The certificates to display. Pass an   containing one or more objects of type   in this parameter. The first certificate in the array must be the leaf certificate. The other certificates (if any) can be included in any order.
- `showGroup`: Specifies whether additional certificates (other than the leaf certificate) are displayed.

## See Also

- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, showGroup: Bool)](sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:showgroup:).md)
  Displays a certificate chain in a modal sheet.
- [func certificateView() -> SFCertificateView!](sfcertificatepanel/certificateview.md)
  Returns the certificate view for the modal panel.
- [func runModal(for: SecTrust!, showGroup: Bool) -> Int](sfcertificatepanel/runmodal(for:showgroup:).md)
  Displays a certificate chain in a modal panel.
- [func runModal(forCertificates: [Any]!, showGroup: Bool) -> Int](sfcertificatepanel/runmodal(forcertificates:showgroup:).md)
  Displays one or more specified certificates in a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:certificates:showgroup:))*