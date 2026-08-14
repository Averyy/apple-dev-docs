# runModal(for:showGroup:)

**Framework**: Security Interface  
**Kind**: method

Displays a certificate chain in a modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func runModal(for trust: SecTrust!, showGroup: Bool) -> Int
```

#### Return Value

This method returns the integer constant [`NSOKButton`](https://developer.apple.com/documentation/appkit/nsokbutton) when dismissed.

## Parameters

- `trust`: A [`SecTrust`](https://developer.apple.com/documentation/security/sectrust) object associated with the certificate chain to display.
- `showGroup`: Specifies whether additional certificates (other than the leaf certificate) are displayed. To show only a single certificate, specify only one [`SecCertificate`](https://developer.apple.com/documentation/security/seccertificate) in the array and set `showGroup` to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, certificates: [Any]!, showGroup: Bool)](sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:certificates:showgroup:).md)
  Displays one or more certificates in a modal sheet.
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, showGroup: Bool)](sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:showgroup:).md)
  Displays a certificate chain in a modal sheet.
- [func certificateView() -> SFCertificateView!](sfcertificatepanel/certificateview.md)
  Returns the certificate view for the modal panel.
- [func runModal(forCertificates: [Any]!, showGroup: Bool) -> Int](sfcertificatepanel/runmodal(forcertificates:showgroup:).md)
  Displays one or more specified certificates in a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/runmodal(for:showgroup:))*