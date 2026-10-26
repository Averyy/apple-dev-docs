# beginSheet(for:modalDelegate:didEnd:contextInfo:trust:message:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays a modal sheet that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func beginSheet(for docWindow: NSWindow!, modalDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, message: String!)
```

```objc
- (void) beginSheetForWindow:(NSWindow *) docWindow modalDelegate:(id) delegate didEndSelector:(SEL) didEndSelector contextInfo:(void *) contextInfo trust:(SecTrustRef) trust message:(NSString *) message;
```

#### Discussion

The delegate method has the following signature:

```objc
- (void)createPanelDidEnd:(NSWindow *)sheet
        returnCode:(int)returnCode
        contextInfo:(void *)contextInfo
```

The parameters for the delegate method are:

- **`sheet`**: The window to which the sheet was attached.
- **`returnCode`**: The result code indicating which button the user clicked: either [`NSFileHandlingPanelOKButton`](../../AppKit/nsfilehandlingpanelokbutton.md) or [`NSFileHandlingPanelCancelButton`](../../AppKit/nsfilehandlingpanelcancelbutton.md).
- **`contextInfo`**: Client-defined contextual data that is passed in the `contextInfo` parameter of the `beginSheetForWindow:...` method.

The delegate method may dismiss the keychain settings sheet itself; if it does not, the sheet is dismissed on return from the `beginSheetForWindow:...` method.

## Parameters

- `docWindow`: The parent window to which the sheet is attached.
- `delegate`: The delegate object in which the method specified in the `didEndSelector` parameter is implemented.
- `didEndSelector`: A method selector for a delegate method called when the sheet has been dismissed. Implementation of this delegate method is optional.
- `contextInfo`: A pointer to data that is passed to the delegate method. You can use this data pointer for any purpose you wish.
- `trust`: A trust management object. Use the [`SecTrustCreateWithCertificates(_:_:_:)`](../../Security/sectrustcreatewithcertificates%28_,_,_%29.md) function (in Security/SecTrust.h) to create the trust management object.
- `message`: A message string to display in the sheet.

## See Also

### Related Documentation
- [func SecTrustCreateWithCertificates(CFTypeRef, CFTypeRef?, UnsafeMutablePointer<SecTrust?>) -> OSStatus](../../Security/sectrustcreatewithcertificates%28_,_,_%29.md)
  Creates a trust management object based on certificates and policies.
- [func runModal(for: SecTrust!, message: String!) -> Int](./runmodal%28for,message%29.md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.
- [SecTrustGetResult](../../Security/sectrustgetresult.md)
  Retrieves details on the outcome of a call to the function `SecTrustEvaluate`.
### Displaying a Sheet or Panel
- [func runModal(for: SecTrust!, message: String!) -> Int](./runmodal%28for,message%29.md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:message:))*