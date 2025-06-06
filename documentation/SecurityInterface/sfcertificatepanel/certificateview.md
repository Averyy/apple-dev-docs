# certificateView()

**Framework**: Security Interface  
**Kind**: method

Returns the certificate view for the modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func certificateView() -> SFCertificateView!
```

## See Also

- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, certificates: [Any]!, showGroup: Bool)](sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:certificates:showgroup:).md)
  Displays one or more certificates in a modal sheet.
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, showGroup: Bool)](sfcertificatepanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:showgroup:).md)
  Displays a certificate chain in a modal sheet.
- [func runModal(for: SecTrust!, showGroup: Bool) -> Int](sfcertificatepanel/runmodal(for:showgroup:).md)
  Displays a certificate chain in a modal panel.
- [func runModal(forCertificates: [Any]!, showGroup: Bool) -> Int](sfcertificatepanel/runmodal(forcertificates:showgroup:).md)
  Displays one or more specified certificates in a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/certificateview())*