# runModal(for:message:)

**Framework**: Security Interface  
**Kind**: method

Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func runModal(for trust: SecTrust!, message: String!) -> Int
```

#### Discussion

This method returns [`NSOKButton`](https://developer.apple.com/documentation/AppKit/NSOKButton) if the default button is clicked, or [`NSCancelButton`](https://developer.apple.com/documentation/AppKit/NSCancelButton) if the alternate button is clicked.

The user can use this panel to edit trust decisions for the specified certificate or for any of the certificates in the certificate chain. The trust settings are saved when the user clicks the default button. Call doc://com.apple.documentation/documentation/security/certificate_key_and_trust_services/trust/1805379-sectrustgetusertrust to obtain the user’s trust settings.

Note that changing the user trust settings does not affect the results of a trust evaluation. Therefore, the trust evaluation shown in the panel (such as “This certificate is not yet valid”) does not change, nor does the result of a call to [`SecTrustGetResult`](https://developer.apple.com/documentation/security/1524331-sectrustgetresult). It is up to your application to determine how to handle the user’s trust decision.

## Parameters

- `trust`: A trust management object. Use the   function (in Security/SecTrust.h) to create the trust management object.
- `message`: A message string to display in the panel.

## Topics

### Related Documentation
- [func SecTrustCreateWithCertificates(_ certificates: CFTypeRef, _ policies: CFTypeRef?, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus](../Security/SecTrustCreateWithCertificates(_:_:_:).md)
  Creates a trust management object based on certificates and policies.

## See Also

- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, message: String!)](sfcertificatetrustpanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:message:).md)
  Displays a modal sheet that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/runmodal(for:message:))*