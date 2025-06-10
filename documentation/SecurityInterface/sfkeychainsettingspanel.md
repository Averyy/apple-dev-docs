# SFKeychainSettingsPanel

**Framework**: Security Interface  
**Kind**: class

A panel or sheet that allows users to change their keychain settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class SFKeychainSettingsPanel
```

#### Overview

Keychain settings include:

- Lock after a set period of inactivity
- Lock on sleep
- Synchronize using .Mac

The following figure shows an example of a keychain settings panel.

![Keychain settings panel](https://docs-assets.developer.apple.com/published/807c5e2eae2ca1b565a06adb351a2b21/media-1965595.png)

For more information, see [`Keychain Services Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/keychainServConcepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000897).

## Topics

### Returning a shared keychain save panel object
- [class func shared() -> SFKeychainSettingsPanel!](sfkeychainsettingspanel/shared.md)
  Returns a shared keychain settings panel object.
### Displaying a sheet or panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, settings: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!)](sfkeychainsettingspanel/beginsheet(for:modaldelegate:didend:contextinfo:settings:keychain:).md)
  Displays a sheet that allows users to change keychain settings.
- [func runModal(for: UnsafeMutablePointer<SecKeychainSettings>!, keychain: SecKeychain!) -> Int](sfkeychainsettingspanel/runmodal(for:keychain:).md)
  Displays a panel that allows users to change keychain settings.

## Relationships

### Inherits From
- [NSPanel](../AppKit/NSPanel.md)
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
- [class SFKeychainSavePanel](sfkeychainsavepanel.md)
  A panel or sheet that allows the user to create a keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsettingspanel)*