# SFCertificateTrustPanel

**Framework**: Security Interface  
**Kind**: class

A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
class SFCertificateTrustPanel
```

#### Overview

The following figure shows an example of a certificate trust panel.

![Certificate trust panel](https://docs-assets.developer.apple.com/published/0f9063c88a6bdf97bfa3276c530ac319/media-1965607.jpg)

You can use this class to enable a user to make trust decisions when one or more certificates required for an operation are invalid or cannot be verified.

To display a certificate in a panel or sheet without editable trust settings, use the [`SFCertificatePanel`](sfcertificatepanel.md) class. To display certificates in a custom view, use the [`SFCertificateView`](sfcertificateview.md) class.

## Topics

### Returning a Shared Certificate Trust Panel Object
- [class func shared() -> SFCertificateTrustPanel!](sfcertificatetrustpanel/shared.md)
  Returns a fully initialized, singleton certificate trust panel object.
### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, message: String!)](sfcertificatetrustpanel/beginsheet(for:modaldelegate:didend:contextinfo:trust:message:).md)
  Displays a modal sheet that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.
- [func runModal(for: SecTrust!, message: String!) -> Int](sfcertificatetrustpanel/runmodal(for:message:).md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.
### Controlling the Appearance of a Certificate Trust Panel
- [func informativeText() -> String!](sfcertificatetrustpanel/informativetext.md)
  Returns the (optional) informative text currently displayed in the panel.
- [func setInformativeText(String!)](sfcertificatetrustpanel/setinformativetext(_:).md)
  Sets the (optional) informative text displayed in the panel.

## Relationships

### Inherits From
- [SFCertificatePanel](sfcertificatepanel.md)
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
- [class SFCertificateView](sfcertificateview.md)
  A view that displays the contents of a certificate, with options to display certificate details, display trust settings, and allow users to edit a certificate’s trust settings.
- [class SFChooseIdentityPanel](sfchooseidentitypanel.md)
  A panel or sheet containing a list of identities that a user can choose from.
- [class SFChooseIdentityTableCellView](sfchooseidentitytablecellview.md)
- [class SFKeychainSavePanel](sfkeychainsavepanel.md)
  A panel or sheet that allows the user to create a keychain.
- [class SFKeychainSettingsPanel](sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel)*