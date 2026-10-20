# SFCertificateView

**Framework**: Security Interface  
**Kind**: class  
**Role**: Class

A view that displays the contents of a certificate, with options to display certificate details, display trust settings, and allow users to edit a certificate’s trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFCertificateView
```

```objc
@interface SFCertificateView : NSVisualEffectView
```

#### Overview

The following figure shows a certificate view that includes editable trust settings and certificate details.

![Certificate view](https://developer.apple.com/tutorials/images/com.apple.securityinterface/media-1965608.jpg)

## Topics

### Specifying the Certificate to Display
- [func setCertificate(SecCertificate!)](./sfcertificateview/setcertificate%28_%29.md)
  Specifies the certificate that’s displayed in the view.
### Customizing the Appearance and Behavior of the View
- [func setDetailsDisclosed(Bool)](./sfcertificateview/setdetailsdisclosed%28_%29.md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](./sfcertificateview/setdisplaydetails%28_%29.md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](./sfcertificateview/setdisplaytrust%28_%29.md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](./sfcertificateview/seteditabletrust%28_%29.md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](./sfcertificateview/setpolicies%28_%29.md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](./sfcertificateview/setpoliciesdisclosed%28_%29.md)
  Specifies whether the trust policy settings subview is disclosed.
### Getting Information About the View
- [func certificate() -> Unmanaged<SecCertificate>!](./sfcertificateview/certificate%28%29.md)
  Returns the certificate currently displayed in the view.
- [func detailsDisplayed() -> Bool](./sfcertificateview/detailsdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s details.
- [func detailsDisclosed() -> Bool](./sfcertificateview/detailsdisclosed%28%29.md)
  Returns whether the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](./sfcertificateview/istrustdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func isEditable() -> Bool](./sfcertificateview/iseditable%28%29.md)
  Indicates if the view allows the user to edit the certificate’s trust.
- [func policies() -> [Any]!](./sfcertificateview/policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
- [func policiesDisclosed() -> Bool](./sfcertificateview/policiesdisclosed%28%29.md)
  Returns whether the trust policy subview is disclosed.
### Saving User Trust Settings
- [func saveTrustSettings()](./sfcertificateview/savetrustsettings%28%29.md)
  Saves the user’s current trust settings for the displayed certificate.
### Constants
- [Notifications](./notifications.md)
  Notifications sent by this class.

## Relationships

### Inherits From
- [NSVisualEffectView](../AppKit/nsvisualeffectview.md)
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
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
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
- [class SFCertificateTrustPanel](./sfcertificatetrustpanel.md)
  A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.
- [class SFChooseIdentityPanel](./sfchooseidentitypanel.md)
  A panel or sheet containing a list of identities that a user can choose from.
- [class SFChooseIdentityTableCellView](./sfchooseidentitytablecellview.md)
- [class SFKeychainSavePanel](./sfkeychainsavepanel.md)
  A panel or sheet that allows the user to create a keychain.
- [class SFKeychainSettingsPanel](./sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview)*