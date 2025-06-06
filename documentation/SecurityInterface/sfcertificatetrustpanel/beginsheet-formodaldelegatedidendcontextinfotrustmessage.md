# beginSheet(for:modalDelegate:didEnd:contextInfo:trust:message:)

**Framework**: Security Interface  
**Kind**: method

Displays a modal sheet that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func beginSheet(for docWindow: NSWindow!, modalDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, message: String!)
```

#### Discussion

The delegate method has the following signature:

```objc
- (void)createPanelDidEnd:(NSWindow *)sheet
        returnCode:(int)returnCode
        contextInfo:(void *)contextInfo
```

The parameters for the delegate method are:

The delegate method may dismiss the keychain settings sheet itself; if it does not, the sheet is dismissed on return from the `beginSheetForWindow:...` method.

## Parameters

- `docWindow`: The parent window to which the sheet is attached.
- `delegate`: The delegate object in which the method specified in the   parameter is implemented.
- `didEndSelector`: A method selector for a delegate method called when the sheet has been dismissed. Implementation of this delegate method is optional.
- `contextInfo`: A pointer to data that is passed to the delegate method. You can use this data pointer for any purpose you wish.
- `trust`: A trust management object. Use the   function (in Security/SecTrust.h) to create the trust management object.
- `message`: A message string to display in the sheet.

## Topics

### Related Documentation
- [func SecTrustCreateWithCertificates(_ certificates: CFTypeRef, _ policies: CFTypeRef?, _ trust: UnsafeMutablePointer<SecTrust?>) -> OSStatus](../Security/SecTrustCreateWithCertificates(_:_:_:).md)
  Creates a trust management object based on certificates and policies.
- [func runModal(for: SecTrust!, message: String!) -> Int](sfcertificatetrustpanel/runmodal(for:message:).md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.

## See Also

- [func runModal(for: SecTrust!, message: String!) -> Int](sfcertificatetrustpanel/runmodal(for:message:).md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:message:))*