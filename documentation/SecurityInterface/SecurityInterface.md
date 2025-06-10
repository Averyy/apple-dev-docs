# Security Interface

**Framework**: Security Interface  
**Kind**: module

Provide user interface elements for security features such as authorization, access to digital certificates, and access to items in keychains.

**Availability**:
- macOS 10.3+

#### Overview

> **Note**:  This document was previously titled . The documentation for the SFAuthorization class is now in a separate document, [`Security Foundation`](https://developer.apple.com/documentation/SecurityFoundation).

The Security Interface framework is a set of Objective-C classes that provide user interface elements for programs that implement security features such as authorization, access to digital certificates, and access to items in keychains.

## Topics

### Classes
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
- [class SFKeychainSettingsPanel](sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.
### Reference
- [struct SFAuthorizationViewState](sfauthorizationviewstate.md)
  Defines the current state of the authorization view.
- [struct SFButtonType](sfbuttontype.md)
  These constants define the button types used by authorization plug-ins.
- [struct SFViewType](sfviewtype.md)
  These constants define the view type requested by the authorization plug-in.
- [SecurityInterface Constants](securityinterface-constants.md)
  Constants in the SecurityInterface framework.
- [SecurityInterface Data Types](securityinterface-data-types.md)
  Data types found in the Security Interface framework.
- [SecurityInterface Enumerations](securityinterface-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SecurityInterface)*