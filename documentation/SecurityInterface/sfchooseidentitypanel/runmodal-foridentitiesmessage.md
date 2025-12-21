# runModal(forIdentities:message:)

**Framework**: Security Interface  
**Kind**: method

Displays a list of identities in a modal panel.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func runModal(forIdentities identities: [Any]!, message: String!) -> Int
```

#### Discussion

This method returns [`NSOKButton`](https://developer.apple.com/documentation/AppKit/NSOKButton) if the default button is clicked, or [`NSCancelButton`](https://developer.apple.com/documentation/AppKit/NSCancelButton) if the alternate button is clicked.

Use the [`identity()`](sfchooseidentitypanel/identity().md) method to obtain the identity chosen by the user.

## Parameters

- `identities`: An array of identity objects (objects of type  . Use the   function (in Security/SecIdentitySearch.h) to find identity objects.
- `message`: A message string to display in the panel.

## See Also

- [func identity() -> Unmanaged<SecIdentity>!](sfchooseidentitypanel/identity.md)
  Returns the identity that the user chose in the panel or sheet.
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, identities: [Any]!, message: String!)](sfchooseidentitypanel/beginsheet(for:modaldelegate:didend:contextinfo:identities:message:).md)
  Displays a list of identities in a modal sheet from which the user can select an identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/runmodal(foridentities:message:))*