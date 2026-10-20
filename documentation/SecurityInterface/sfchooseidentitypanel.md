# SFChooseIdentityPanel

**Framework**: Security Interface  
**Kind**: class  
**Role**: Class

A panel or sheet containing a list of identities that a user can choose from.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFChooseIdentityPanel
```

```objc
@interface SFChooseIdentityPanel : NSPanel
```

#### Overview

An identity is a digital certificate together with its associated private key. This class also allows the user to display the contents of any certificate in the list.

The following figure shows an example of a choose identity panel.

![Choose identity panel](https://developer.apple.com/tutorials/images/com.apple.securityinterface/media-1965600.jpg)

## Topics

### Returning a Shared Certificate Panel Object
- [class func shared() -> SFChooseIdentityPanel!](./sfchooseidentitypanel/shared%28%29.md)
  Returns a fully initialized, singleton choose identity panel object.
### Providing Help
- [func setHelpAnchor(String!)](./sfchooseidentitypanel/sethelpanchor%28_%29.md)
  Sets the help anchor string for the sheet or modal panel.
- [func setShowsHelp(Bool)](./sfchooseidentitypanel/setshowshelp%28_%29.md)
  Displays a Help button in the sheet or panel.
- [func helpAnchor() -> String!](./sfchooseidentitypanel/helpanchor%28%29.md)
  Returns the current help anchor string for the sheet or panel.
- [func showsHelp() -> Bool](./sfchooseidentitypanel/showshelp%28%29.md)
  Indicates whether the help button is currently set to be displayed.
### Customizing the Appearance of the Sheet or Panel
- [func setAlternateButtonTitle(String!)](./sfchooseidentitypanel/setalternatebuttontitle%28_%29.md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](./sfchooseidentitypanel/setdefaultbuttontitle%28_%29.md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](./sfchooseidentitypanel/setpolicies%28_%29.md)
  Specifies one or more policies that apply to the displayed certificates.
- [func policies() -> [Any]!](./sfchooseidentitypanel/policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
- [func informativeText() -> String!](./sfchooseidentitypanel/informativetext%28%29.md)
  Returns the informative text currently displayed in the panel.
- [func setInformativeText(String!)](./sfchooseidentitypanel/setinformativetext%28_%29.md)
  Sets the optional informative text displayed in the panel.
### Displaying a Sheet or Panel
- [func beginSheet(for: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!, identities: [Any]!, message: String!)](./sfchooseidentitypanel/beginsheet%28for,modaldelegate,didend,contextinfo,identities,message%29.md)
  Displays a list of identities in a modal sheet from which the user can select an identity.
- [func runModal(forIdentities: [Any]!, message: String!) -> Int](./sfchooseidentitypanel/runmodal%28foridentities,message%29.md)
  Displays a list of identities in a modal panel.
### Getting Identity Information from a Sheet or Panel
- [func identity() -> Unmanaged<SecIdentity>!](./sfchooseidentitypanel/identity%28%29.md)
  Returns the identity that the user chose in the panel or sheet.
### Working with Domains
- [func domain() -> String!](./sfchooseidentitypanel/domain%28%29.md)
  Returns the domain that will be associated with the chosen identity.
- [func setDomain(String!)](./sfchooseidentitypanel/setdomain%28_%29.md)
  Sets an optional domain in which the identity is to be used.
### Delegate methods for providing help
- [func chooseIdentityPanelShowHelp(SFChooseIdentityPanel!) -> Bool](../ObjectiveC/nsobject-swift.class/chooseidentitypanelshowhelp%28_%29.md)
  Implements custom help behavior for the modal panel.

## Relationships

### Inherits From
- [NSPanel](../AppKit/nspanel.md)
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
- [class SFCertificateTrustPanel](./sfcertificatetrustpanel.md)
  A panel or sheet that lets the user edit the trust settings in any of the certificates in a certificate chain.
- [class SFCertificateView](./sfcertificateview.md)
  A view that displays the contents of a certificate, with options to display certificate details, display trust settings, and allow users to edit a certificate’s trust settings.
- [class SFChooseIdentityTableCellView](./sfchooseidentitytablecellview.md)
- [class SFKeychainSavePanel](./sfkeychainsavepanel.md)
  A panel or sheet that allows the user to create a keychain.
- [class SFKeychainSettingsPanel](./sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel)*