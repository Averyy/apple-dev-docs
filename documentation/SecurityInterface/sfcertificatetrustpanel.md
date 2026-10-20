# SFCertificateTrustPanel

**Framework**: Security Interface  
**Kind**: class  
**Role**: Class

A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFCertificateTrustPanel
```

```objc
@interface SFCertificateTrustPanel : SFCertificatePanel
```

#### Overview

The following figure shows an example of a certificate trust panel.

![Certificate trust panel](https://developer.apple.com/tutorials/images/com.apple.securityinterface/media-1965607.jpg)

You can use this class to enable a user to make trust decisions when one or more certificates required for an operation are invalid or cannot be verified.

To display a certificate in a panel or sheet without editable trust settings, use the [`SFCertificatePanel`](./sfcertificatepanel.md) class. To display certificates in a custom view, use the [`SFCertificateView`](./sfcertificateview.md) class.

## Topics

### Returning a Shared Certificate Trust Panel Object
- [class func shared() -> SFCertificateTrustPanel!](./sfcertificatetrustpanel/shared%28%29.md)
  Returns a fully initialized, singleton certificate trust panel object.
### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, message: String!)](./sfcertificatetrustpanel/beginsheet%28for,modaldelegate,didend,contextinfo,trust,message%29.md)
  Displays a modal sheet that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.
- [func runModal(for: SecTrust!, message: String!) -> Int](./sfcertificatetrustpanel/runmodal%28for,message%29.md)
  Displays a modal panel that shows the results of a certificate trust evaluation and that allows the user to edit trust settings.
### Controlling the Appearance of a Certificate Trust Panel
- [func informativeText() -> String!](./sfcertificatetrustpanel/informativetext%28%29.md)
  Returns the (optional) informative text currently displayed in the panel.
- [func setInformativeText(String!)](./sfcertificatetrustpanel/setinformativetext%28_%29.md)
  Sets the (optional) informative text displayed in the panel.

## Relationships

### Inherits From
- [SFCertificatePanel](./sfcertificatepanel.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSMenuItemValidation](../AppKit/nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](../AppKit/nsuserinterfacevalidations.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class SFAuthorizationPluginView](./sfauthorizationpluginview.md)
  Allows authorization plug-in developers to create a custom view their plug-in can display.
- [class SFAuthorizationView](./sfauthorizationview.md)
  The class responsible for displaying a lock icon that can be used to indicate that a user interface has restricted access.
- [class SFCertificatePanel](./sfcertificatepanel.md)
  A panel or sheet that displays one or more certificates.
- [class SFCertificateView](./sfcertificateview.md)
  A view that displays the contents of a certificate, with options to display certificate details, display trust settings, and allow users to edit a certificate’s trust settings.
- [class SFChooseIdentityPanel](./sfchooseidentitypanel.md)
  A panel or sheet containing a list of identities that a user can choose from.
- [class SFChooseIdentityTableCellView](./sfchooseidentitytablecellview.md)
- [class SFKeychainSavePanel](./sfkeychainsavepanel.md)
  A panel or sheet that allows the user to create a keychain.
- [class SFKeychainSettingsPanel](./sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel)*