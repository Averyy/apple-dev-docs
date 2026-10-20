# SFCertificatePanel

**Framework**: Security Interface  
**Kind**: class  
**Role**: Class

A panel or sheet that displays one or more certificates.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFCertificatePanel
```

```objc
@interface SFCertificatePanel : NSPanel
```

#### Overview

The following figure shows an example of a certificate panel.

![Certificate panel](https://developer.apple.com/tutorials/images/com.apple.securityinterface/media-1965612.jpg)

An [`SFCertificatePanel`](./sfcertificatepanel.md) can optionally display all of the certificates in a certificate chain.

This class displays certificate details, but not trust settings. To display a certificate with editable trust settings in a panel or sheet, use the [`SFCertificateTrustPanel`](./sfcertificatetrustpanel.md) class. To display certificates in a custom view, use the [`SFCertificateView`](./sfcertificateview.md) class.

Note that for macOS 10.4 and later, this class displays the evaluation status for each certificate. You can modify how the certificates are evaluated by calling the [`setPolicies(_:)`](./sfcertificatepanel/setpolicies%28_%29.md) method.

## Topics

### Returning a Shared Certificate Panel Object
- [class func shared() -> SFCertificatePanel!](./sfcertificatepanel/shared%28%29.md)
  Returns a fully initialized, singleton certificate panel object.
### Providing Help
- [func setHelpAnchor(String!)](./sfcertificatepanel/sethelpanchor%28_%29.md)
  Sets the help anchor string for the sheet or modal panel.
- [func setShowsHelp(Bool)](./sfcertificatepanel/setshowshelp%28_%29.md)
  Displays a Help button in the sheet or panel.
- [func helpAnchor() -> String!](./sfcertificatepanel/helpanchor%28%29.md)
  Returns the current help anchor string for the sheet or panel.
- [func showsHelp() -> Bool](./sfcertificatepanel/showshelp%28%29.md)
  Indicates whether the help button is currently set to be displayed.
### Customizing the Appearance of the Sheet or Panel
- [func setAlternateButtonTitle(String!)](./sfcertificatepanel/setalternatebuttontitle%28_%29.md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](./sfcertificatepanel/setdefaultbuttontitle%28_%29.md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](./sfcertificatepanel/setpolicies%28_%29.md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](./sfcertificatepanel/policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, certificates: [Any]!, showGroup: Bool)](./sfcertificatepanel/beginsheet%28for,modaldelegate,didend,contextinfo,certificates,showgroup%29.md)
  Displays one or more certificates in a modal sheet.
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, trust: SecTrust!, showGroup: Bool)](./sfcertificatepanel/beginsheet%28for,modaldelegate,didend,contextinfo,trust,showgroup%29.md)
  Displays a certificate chain in a modal sheet.
- [func certificateView() -> SFCertificateView!](./sfcertificatepanel/certificateview%28%29.md)
  Returns the certificate view for the modal panel.
- [func runModal(for: SecTrust!, showGroup: Bool) -> Int](./sfcertificatepanel/runmodal%28for,showgroup%29.md)
  Displays a certificate chain in a modal panel.
- [func runModal(forCertificates: [Any]!, showGroup: Bool) -> Int](./sfcertificatepanel/runmodal%28forcertificates,showgroup%29.md)
  Displays one or more specified certificates in a modal panel.
### Delegate method for providing help
- [func certificatePanelShowHelp(SFCertificatePanel!) -> Bool](../ObjectiveC/nsobject-swift.class/certificatepanelshowhelp%28_%29.md)
  Implements custom help behavior for the modal panel.

## Relationships

### Inherits From
- [NSPanel](../AppKit/nspanel.md)
### Inherited By
- [SFCertificateTrustPanel](./sfcertificatetrustpanel.md)
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
- [class SFCertificateTrustPanel](./sfcertificatetrustpanel.md)
  A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.
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

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel)*