# SFKeychainSavePanel

**Framework**: Security Interface  
**Kind**: class  
**Role**: Class

A panel or sheet that allows the user to create a keychain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFKeychainSavePanel
```

```objc
@interface SFKeychainSavePanel : NSSavePanel
```

## Overview

The following figure shows an example of a keychain save panel.

![Keychain save panel](https://developer.apple.com/tutorials/images/com.apple.securityinterface/media-1965598.gif)

## Topics

### Returning a Shared Keychain Save Panel Object
- [class func shared() -> SFKeychainSavePanel!](./sfkeychainsavepanel/shared%28%29.md)
  Returns a shared keychain save panel object.
### Displaying a Sheet or Panel
- [func setPassword(String!)](./sfkeychainsavepanel/setpassword%28_%29.md)
  Specifies the password for the keychain that will be created.
- [func beginSheet(forDirectory: String!, file: String!, modalFor: NSWindow!, modalDelegate: Any!, didEnd: Selector!, contextInfo: UnsafeMutableRawPointer!)](./sfkeychainsavepanel/beginsheet%28fordirectory,file,modalfor,modaldelegate,didend,contextinfo%29.md)
  Displays a sheet that allows a user to create a new keychain.
- [func runModal(forDirectory: String!, file: String!) -> Int](./sfkeychainsavepanel/runmodal%28fordirectory,file%29.md)
  Displays a panel that allows a user to create a new keychain.
### Returning Information from the Sheet or Panel
- [func error() -> (any Error)!](./sfkeychainsavepanel/error%28%29.md)
  Returns the last error encountered by the keychain save panel.
- [func keychain() -> Unmanaged<SecKeychain>!](./sfkeychainsavepanel/keychain%28%29.md)
  Returns the keychain created by the keychain save panel.

## Relationships

### Inherits From
- [NSSavePanel](../AppKit/nssavepanel.md)
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
- [class SFChooseIdentityPanel](./sfchooseidentitypanel.md)
  A panel or sheet containing a list of identities that a user can choose from.
- [class SFChooseIdentityTableCellView](./sfchooseidentitytablecellview.md)
- [class SFKeychainSettingsPanel](./sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel)*