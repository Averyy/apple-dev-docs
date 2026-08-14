# SFCertificateView

**Framework**: Security Interface  
**Kind**: class

A view that displays the contents of a certificate, with options to display certificate details, display trust settings, and allow users to edit a certificate’s trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFCertificateView
```

#### Overview

The following figure shows a certificate view that includes editable trust settings and certificate details.

![Certificate view](/images/com.apple.securityinterface/media-1965608.jpg)

## Topics

### Specifying the Certificate to Display
- [func setCertificate(SecCertificate!)](sfcertificateview/setcertificate(_:).md)
  Specifies the certificate that’s displayed in the view.
### Customizing the Appearance and Behavior of the View
- [func setDetailsDisclosed(Bool)](sfcertificateview/setdetailsdisclosed(_:).md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](sfcertificateview/setdisplaydetails(_:).md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](sfcertificateview/setdisplaytrust(_:).md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](sfcertificateview/seteditabletrust(_:).md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](sfcertificateview/setpolicies(_:).md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](sfcertificateview/setpoliciesdisclosed(_:).md)
  Specifies whether the trust policy settings subview is disclosed.
### Getting Information About the View
- [func certificate() -> Unmanaged<SecCertificate>!](sfcertificateview/certificate.md)
  Returns the certificate currently displayed in the view.
- [func detailsDisplayed() -> Bool](sfcertificateview/detailsdisplayed.md)
  Indicates if the view currently shows the certificate’s details.
- [func detailsDisclosed() -> Bool](sfcertificateview/detailsdisclosed.md)
  Returns whether the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](sfcertificateview/istrustdisplayed.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func isEditable() -> Bool](sfcertificateview/iseditable.md)
  Indicates if the view allows the user to edit the certificate’s trust.
- [func policies() -> [Any]!](sfcertificateview/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
- [func policiesDisclosed() -> Bool](sfcertificateview/policiesdisclosed.md)
  Returns whether the trust policy subview is disclosed.
### Saving User Trust Settings
- [func saveTrustSettings()](sfcertificateview/savetrustsettings.md)
  Saves the user’s current trust settings for the displayed certificate.
### Constants
- [Notifications](notifications.md)
  Notifications sent by this class.

## Relationships

### Inherits From
- [NSVisualEffectView](../appkit/nsvisualeffectview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class SFAuthorizationPluginView](sfauthorizationpluginview.md)
  Allows authorization plug-in developers to create a custom view their plug-in can display.
- [class SFAuthorizationView](sfauthorizationview.md)
  The class responsible for displaying a lock icon that can be used to indicate that a user interface has restricted access.
- [class SFCertificatePanel](sfcertificatepanel.md)
  A panel or sheet that displays one or more certificates.
- [class SFCertificateTrustPanel](sfcertificatetrustpanel.md)
  A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.
- [class SFChooseIdentityPanel](sfchooseidentitypanel.md)
  A panel or sheet containing a list of identities that a user can choose from.
- [class SFChooseIdentityTableCellView](sfchooseidentitytablecellview.md)
- [class SFKeychainSavePanel](sfkeychainsavepanel.md)
  A panel or sheet that allows the user to create a keychain.
- [class SFKeychainSettingsPanel](sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview)*