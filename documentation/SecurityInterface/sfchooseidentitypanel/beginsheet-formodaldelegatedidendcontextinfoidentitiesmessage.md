# beginSheet(for:modalDelegate:didEnd:contextInfo:identities:message:)

**Framework**: Security Interface  
**Kind**: method

Displays a list of identities in a modal sheet from which the user can select an identity.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func beginSheet(for docWindow: NSWindow!, modalDelegate delegate: Any!, didEnd didEndSelector: Selector!, contextInfo: UnsafeMutableRawPointer!, identities: [Any]!, message: String!)
```

#### Discussion

Use the `identity` method to obtain the identity chosen by the user.

The delegate method has the following signature:

```objc
- (void)createPanelDidEnd:(NSWindow *)sheet
        returnCode:(int)returnCode
        contextInfo:(void *)contextInfo
```

The parameters for the delegate method are:

The sheet is dismissed on return from the `beginSheetForWindow:...` method.

## Parameters

- `docWindow`: The parent window to which the sheet is attached.
- `delegate`: The delegate object in which the method specified in the   parameter is implemented.
- `didEndSelector`: A method selector for a delegate method called when the sheet has been dismissed. Implementation of this delegate method is optional.
- `contextInfo`: A pointer to data that is passed to the delegate method. You can use this data pointer for any purpose you wish.
- `identities`: An array of identity objects (objects of type  ). Use the   function (in Security/SecIdentitySearch.h) to find identity objects.
- `message`: A message string to display in the sheet.

## Topics

### Related Documentation
- [func runModal(forIdentities: [Any]!, message: String!) -> Int](sfchooseidentitypanel/runmodal(foridentities:message:).md)
  Displays a list of identities in a modal panel.
- [func identity() -> Unmanaged<SecIdentity>!](sfchooseidentitypanel/identity.md)
  Returns the identity that the user chose in the panel or sheet.

## See Also

- [func runModal(forIdentities: [Any]!, message: String!) -> Int](sfchooseidentitypanel/runmodal(foridentities:message:).md)
  Displays a list of identities in a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/beginsheet(for:modaldelegate:didend:contextinfo:identities:message:))*