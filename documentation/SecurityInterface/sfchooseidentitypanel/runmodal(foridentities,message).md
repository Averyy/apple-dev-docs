# runModal(forIdentities:message:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Displays a list of identities in a modal panel.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func runModal(forIdentities identities: [Any]!, message: String!) -> Int
```

```objc
- (NSInteger) runModalForIdentities:(NSArray *) identities message:(NSString *) message;
```

#### Discussion

This method returns [`NSOKButton`](../../AppKit/nsokbutton.md) if the default button is clicked, or [`NSCancelButton`](../../AppKit/nscancelbutton.md) if the alternate button is clicked.

Use the [`identity()`](./identity%28%29.md) method to obtain the identity chosen by the user.

## Parameters

- `identities`: An array of identity objects (objects of type [`SecIdentity`](../../Security/secidentity.md). Use the [`SecIdentitySearchCopyNext`](../../Security/secidentitysearchcopynext.md) function (in Security/SecIdentitySearch.h) to find identity objects.
- `message`: A message string to display in the panel.

## See Also

### Related Documentation
- [func identity() -> Unmanaged<SecIdentity>!](./identity%28%29.md)
  Returns the identity that the user chose in the panel or sheet.
- [SecIdentitySearchCopyNext](../../Security/secidentitysearchcopynext.md)
  Finds the next identity matching specified search criteria
### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, identities: [Any]!, message: String!)](./beginsheet%28for,modaldelegate,didend,contextinfo,identities,message%29.md)
  Displays a list of identities in a modal sheet from which the user can select an identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/runmodal(foridentities:message:))*