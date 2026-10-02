# SFAuthorizationView

**Framework**: Security Interface  
**Kind**: class

The class responsible for displaying a lock icon that can be used to indicate that a user interface has restricted access.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFAuthorizationView
```

#### Overview

The lock appears locked when the user must be authorized and appears open when the user has been authorized. The closed and open lock icons of the authorization view are shown in the following figure.

![Authorization view lock icon](/images/com.apple.securityinterface/media-1965610.gif)

When you add an authorization view as a custom view to a window or dialog box, you must initialize it before it displays correctly. To initialize the view, use the [`setString(_:)`](sfauthorizationview/setstring(_:).md) method to create a default rights structure (containing a prompt string) or the [`setAuthorizationRights(_:)`](sfauthorizationview/setauthorizationrights(_:).md) method to specify a rights structure. You must also either specify automatic updates ([`setAutoupdate(_:)`](sfauthorizationview/setautoupdate(_:).md) or [`setAutoupdate(_:interval:)`](sfauthorizationview/setautoupdate(_:interval:).md)) or perform a manual update ([`updateStatus(_:)`](sfauthorizationview/updatestatus(_:).md)) to set the lock icon to its initial state.

You can implement delegate methods that are invoked when the authorization view changes state. You can optionally implement the delegate methods to obtain the state of the authorization object when you are using an authorization view.

When the user clicks a locked authorization view icon, the Security Server displays an authentication dialog (to request a user name and password, for example). When the user provides the requested credentials, the lock icon unlocks and the user is considered preauthorized to perform the functions specified by the authorization rights structure. You can call the [`updateStatus(_:)`](sfauthorizationview/updatestatus(_:).md) method to determine whether the user has been preauthorized: this method returns [`true`](https://developer.apple.com/documentation/swift/true) if the view is in the unlocked state, otherwise [`false`](https://developer.apple.com/documentation/swift/false). Before committing changes or performing actions that require authorization, you should check the user’s authorization again, even if they are preauthorized.

The default behavior of this view is to preauthorize rights; if this is not possible it unlocks and waits for authorization to be checked when explicitly required.

## Topics

### Setting up the authorization view
- [func setString(AuthorizationString!)](sfauthorizationview/setstring(_:).md)
  Sets the requested-right string to use with the default authorization rights set.
- [func setAuthorizationRights(UnsafePointer<AuthorizationRights>!)](sfauthorizationview/setauthorizationrights(_:).md)
  Sets the authorization rights for this view.
- [func setAutoupdate(Bool)](sfauthorizationview/setautoupdate(_:).md)
  Sets the authorization view to update itself automatically.
- [func setAutoupdate(Bool, interval: TimeInterval)](sfauthorizationview/setautoupdate(_:interval:).md)
  Sets the authorization view to update itself at a specific interval.
- [func setFlags(AuthorizationFlags)](sfauthorizationview/setflags(_:).md)
  Sets the current authorization flags for the view.
- [func setEnabled(Bool)](sfauthorizationview/setenabled(_:).md)
  Sets the current state of the authorization view.
### Setting and getting the delegate for the view
- [func setDelegate(Any!)](sfauthorizationview/setdelegate(_:).md)
  Sets the delegate for this authorization view.
- [func delegate() -> Any!](sfauthorizationview/delegate.md)
  Returns the delegate for this view.
### Updating the view
- [func updateStatus(Any!) -> Bool](sfauthorizationview/updatestatus(_:).md)
  Manually updates the authorization view.
### Getting information about the authorization view
- [func authorization() -> SFAuthorization!](sfauthorizationview/authorization.md)
  Returns the authorization object associated with this view.
- [func authorizationRights() -> UnsafeMutablePointer<AuthorizationRights>!](sfauthorizationview/authorizationrights.md)
  Returns the authorization rights for this view.
- [func authorizationState() -> SFAuthorizationViewState](sfauthorizationview/authorizationstate.md)
  Returns the current state of the authorization view.
- [func isEnabled() -> Bool](sfauthorizationview/isenabled.md)
  Indicates whether the authorization view is enabled ([`true`](https://developer.apple.com/documentation/swift/true)) or disabled ([`false`](https://developer.apple.com/documentation/swift/false)).
### Setting the authorization state
- [func authorize(Any!) -> Bool](sfauthorizationview/authorize(_:).md)
  Attempts to unlock the lock icon in the view.
- [func deauthorize(Any!) -> Bool](sfauthorizationview/deauthorize(_:).md)
  Sets the authorization state to unauthorized and locks the lock icon in the view.
### Delegate methods
- [func authorizationViewShouldDeauthorize(SFAuthorizationView!) -> Bool](../objectivec/nsobject-swift.class/authorizationviewshoulddeauthorize(_:).md)
  Sent to the delegate when a user clicks the open lock icon.
- [func authorizationViewCreatedAuthorization(SFAuthorizationView!)](../objectivec/nsobject-swift.class/authorizationviewcreatedauthorization(_:).md)
  Sent to the delegate to indicate the authorization object has been created or changed.
- [func authorizationViewDidAuthorize(SFAuthorizationView!)](../objectivec/nsobject-swift.class/authorizationviewdidauthorize(_:).md)
  Sent to the delegate to indicate the user was authorized and the authorization view was changed to unlocked.
- [func authorizationViewDidDeauthorize(SFAuthorizationView!)](../objectivec/nsobject-swift.class/authorizationviewdiddeauthorize(_:).md)
  Sent to the delegate to indicate the user was deauthorized and the authorization view was changed to locked.
- [func authorizationViewDidHide(SFAuthorizationView!)](../objectivec/nsobject-swift.class/authorizationviewdidhide(_:).md)
  Sent to the delegate to indicate that the view’s visibility has changed.
- [func authorizationViewReleasedAuthorization(SFAuthorizationView!)](../objectivec/nsobject-swift.class/authorizationviewreleasedauthorization(_:).md)
  Sent to the delegate to indicate that deauthorization is about to occur.
### Constants
- [struct SFAuthorizationViewState](sfauthorizationviewstate.md)
  Defines the current state of the authorization view.

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationview)*