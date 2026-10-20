# certificateView()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the certificate view for the modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func certificateView() -> SFCertificateView!
```

```objc
- (SFCertificateView *) certificateView;
```

## See Also

### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, certificates: [Any]!, showGroup: Bool)](./beginsheet%28for,modaldelegate,didend,contextinfo,certificates,showgroup%29.md)
  Displays one or more certificates in a modal sheet.
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, showGroup: Bool)](./beginsheet%28for,modaldelegate,didend,contextinfo,trust,showgroup%29.md)
  Displays a certificate chain in a modal sheet.
- [func runModal(for: SecTrust!, showGroup: Bool) -> Int](./runmodal%28for,showgroup%29.md)
  Displays a certificate chain in a modal panel.
- [func runModal(forCertificates: [Any]!, showGroup: Bool) -> Int](./runmodal%28forcertificates,showgroup%29.md)
  Displays one or more specified certificates in a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/certificateview())*