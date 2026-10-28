# runModal(for:showGroup:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays a certificate chain in a modal panel.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func runModal(for trust: SecTrust!, showGroup: Bool) -> Int
```

```objc
- (NSInteger) runModalForTrust:(SecTrustRef) trust showGroup:(BOOL) showGroup;
```

## Return Value

This method returns the integer constant [`NSOKButton`](../../AppKit/nsokbutton.md) when dismissed.

## Parameters

- `trust`: A [`SecTrust`](../../Security/sectrust.md) object associated with the certificate chain to display.
- `showGroup`: Specifies whether additional certificates (other than the leaf certificate) are displayed. To show only a single certificate, specify only one [`SecCertificate`](../../Security/seccertificate.md) in the array and set `showGroup` to [`false`](../../Swift/false.md).

## See Also

### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, certificates: [Any]!, showGroup: Bool)](./beginsheet%28for,modaldelegate,didend,contextinfo,certificates,showgroup%29.md)
  Displays one or more certificates in a modal sheet.
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, showGroup: Bool)](./beginsheet%28for,modaldelegate,didend,contextinfo,trust,showgroup%29.md)
  Displays a certificate chain in a modal sheet.
- [func certificateView() -> SFCertificateView!](./certificateview%28%29.md)
  Returns the certificate view for the modal panel.
- [func runModal(forCertificates: [Any]!, showGroup: Bool) -> Int](./runmodal%28forcertificates,showgroup%29.md)
  Displays one or more specified certificates in a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/runmodal(for:showgroup:))*