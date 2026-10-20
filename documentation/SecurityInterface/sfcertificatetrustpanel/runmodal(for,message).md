# runModal(for:message:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func runModal(for trust: SecTrust!, message: String!) -> Int
```

```objc
- (NSInteger) runModalForTrust:(SecTrustRef) trust message:(NSString *) message;
```

#### Discussion

This method returns [`NSOKButton`](../../AppKit/nsokbutton.md) if the default button is clicked, or [`NSCancelButton`](../../AppKit/nscancelbutton.md) if the alternate button is clicked.

The user can use this panel to edit trust decisions for the specified certificate or for any of the certificates in the certificate chain. The trust settings are saved when the user clicks the default button. Call `SecTrustGetUserTrust` to obtain the user’s trust settings.

Note that changing the user trust settings does not affect the results of a trust evaluation. Therefore, the trust evaluation shown in the panel (such as “This certificate is not yet valid”) does not change, nor does the result of a call to [`SecTrustGetResult`](../../Security/sectrustgetresult.md). It is up to your application to determine how to handle the user’s trust decision.

## Parameters

- `trust`: A trust management object. Use the [`SecTrustCreateWithCertificates(_:_:_:)`](../../Security/sectrustcreatewithcertificates%28_,_,_%29.md) function (in Security/SecTrust.h) to create the trust management object.
- `message`: A message string to display in the panel.

## See Also

### Related Documentation
- [func SecTrustCreateWithCertificates(CFTypeRef, CFTypeRef?, UnsafeMutablePointer<SecTrust?>) -> OSStatus](../../Security/sectrustcreatewithcertificates%28_,_,_%29.md)
  Creates a trust management object based on certificates and policies.
### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, message: String!)](./beginsheet%28for,modaldelegate,didend,contextinfo,trust,message%29.md)
  Displays a modal sheet that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/runmodal(for:message:))*