# SFKeychainSavePanel

**Framework**: Security Interface  
**Kind**: class

A panel or sheet that allows the user to create a keychain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class SFKeychainSavePanel
```

#### Overview

The following figure shows an example of a keychain save panel.

![Keychain save panel](https://docs-assets.developer.apple.com/published/b327febdaf39a8f65e881c53bb3df3ae/media-1965598.gif)

## Topics

### Returning a Shared Keychain Save Panel Object
- [class func shared() -> SFKeychainSavePanel!](sfkeychainsavepanel/shared.md)
  Returns a shared keychain save panel object.
### Displaying a Sheet or Panel
- [func setPassword(String!)](sfkeychainsavepanel/setpassword(_:).md)
  Specifies the password for the keychain that will be created.
- [func beginSheet(forDirectory: String!, file: String!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](sfkeychainsavepanel/beginsheet(fordirectory:file:modalfor:modaldelegate:didend:contextinfo:).md)
  Displays a sheet that allows a user to create a new keychain.
- [func runModal(forDirectory: String!, file: String!) -> Int](sfkeychainsavepanel/runmodal(fordirectory:file:).md)
  Displays a panel that allows a user to create a new keychain.
### Returning Information from the Sheet or Panel
- [func error() -> (any Error)!](sfkeychainsavepanel/error.md)
  Returns the last error encountered by the keychain save panel.
- [func keychain() -> Unmanaged<SecKeychain>!](sfkeychainsavepanel/keychain.md)
  Returns the keychain created by the keychain save panel.

## Relationships

### Inherits From
- [NSSavePanel](../AppKit/NSSavePanel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSMenuItemValidation](../AppKit/NSMenuItemValidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class SFAuthorizationPluginView](sfauthorizationpluginview.md)
  Allows authorization plug-in developers to create a custom view their plug-in can display.
- [class SFAuthorizationView](sfauthorizationview.md)
  The class responsible for displaying a lock icon that can be used to indicate that a user interface has restricted access.
- [class SFCertificatePanel](sfcertificatepanel.md)
  A panel or sheet that displays one or more certificates.
- [class SFCertificateTrustPanel](sfcertificatetrustpanel.md)
  A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.
- [class SFCertificateView](sfcertificateview.md)
  A view that displays the contents of a certificate, with options to display certificate details, display trust settings, and allow users to edit a certificate’s trust settings.
- [class SFChooseIdentityPanel](sfchooseidentitypanel.md)
  A panel or sheet containing a list of identities that a user can choose from.
- [class SFChooseIdentityTableCellView](sfchooseidentitytablecellview.md)
- [class SFKeychainSettingsPanel](sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel)*