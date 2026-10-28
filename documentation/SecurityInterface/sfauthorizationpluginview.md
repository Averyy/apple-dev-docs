# SFAuthorizationPluginView

**Framework**: Security Interface  
**Kind**: class  
**Role**: Class

Allows authorization plug-in developers to create a custom view their plug-in can display.

**Availability**:
- macOS 10.3+

## Declaration

```swift
class SFAuthorizationPluginView
```

```objc
@interface SFAuthorizationPluginView : NSObject
```

## Overview

If you’re developing an authorization plug-in, you can subclass the [`SFAuthorizationPluginView`](./sfauthorizationpluginview.md) class to create views that provide a custom user interface for your plug-in. By subclassing the [`SFAuthorizationPluginView`](./sfauthorizationpluginview.md) class, you avoid changing or duplicating the Apple-provided authentication or login window dialogs to display your custom view.

To instantiate your [`SFAuthorizationPluginView`](./sfauthorizationpluginview.md) subclass, you need the callbacks structure containing entry points to the Security Server that you receive in your plug-in’s [`AuthorizationPluginCreate`](../Security/authorizationplugincreate.md) function and the authorization engine handle you receive in your plug-in’s [`MechanismCreate`](../Security/authorizationplugininterface/mechanismcreate.md) function.

Your custom subclass of [`SFAuthorizationPluginView`](./sfauthorizationpluginview.md) must override the following methods:

- [`buttonPressed(_:)`](./sfauthorizationpluginview/buttonpressed%28_%29.md)
- [`view(for:)`](./sfauthorizationpluginview/view%28for%29.md)

## Topics

### Initializing an SFAuthorizationPluginView Object
- [init!(callbacks: UnsafePointer<AuthorizationCallbacks>!, andEngineRef: AuthorizationEngineRef!)](./sfauthorizationpluginview/init%28callbacks,andengineref%29.md)
  Initializes a new authorization plug-in view with the specified callbacks and authorization engine handle.
### Getting Instance Information
- [func callbacks() -> UnsafePointer<AuthorizationCallbacks>!](./sfauthorizationpluginview/callbacks%28%29.md)
  Returns the authorization callbacks structure with which this instance was initialized.
- [func engineRef() -> AuthorizationEngineRef!](./sfauthorizationpluginview/engineref%28%29.md)
  Returns the authorization engine handle with which this instance was initialized.
- [func lastError() -> (any Error)!](./sfauthorizationpluginview/lasterror%28%29.md)
  Returns the last error that occurred during evaluation.
### Responding to User Actions
- [func buttonPressed(SFButtonType)](./sfauthorizationpluginview/buttonpressed%28_%29.md)
  Tells the authorization plug-in that the user pressed a button in the custom view.
- [func view(for: SFViewType) -> NSView!](./sfauthorizationpluginview/view%28for%29.md)
  Returns the appropriate view object for the specified view type.
### Configuring the User Interface
- [func didActivate()](./sfauthorizationpluginview/didactivate%28%29.md)
  Tells the authorization plug-in when its user interface has become active.
- [func didDeactivate()](./sfauthorizationpluginview/diddeactivate%28%29.md)
  Tells the authorization plug-in that its user interface has been deactivated.
- [func willActivate(withUser: [AnyHashable : Any]!)](./sfauthorizationpluginview/willactivate%28withuser%29.md)
  Tells the authorization plug-in that its user interface is about to be made active by the Apple-provided Security Agent.
### Setting Up the Keyboard Loop
- [func firstKeyView() -> NSView!](./sfauthorizationpluginview/firstkeyview%28%29.md)
  Returns the first view in the keyboard loop of the view.
- [func firstResponder() -> NSResponder!](./sfauthorizationpluginview/firstresponder%28%29.md)
  Returns the view that should get focus for keyboard events.
- [func lastKeyView() -> NSView!](./sfauthorizationpluginview/lastkeyview%28%29.md)
  Returns the last view in the keyboard loop of the view.
### Enabling and Disabling Controls
- [func setEnabled(Bool)](./sfauthorizationpluginview/setenabled%28_%29.md)
  Enables or disables the controls in the authorization plug-in’s view.
### Communicating with the Authorization Plug-in
- [func display()](./sfauthorizationpluginview/display%28%29.md)
  Displays the user interface provided by the authorization plug-in view subclass.
- [func setButton(SFButtonType, enabled: Bool)](./sfauthorizationpluginview/setbutton%28_,enabled%29.md)
  Enables or disables a button in the authorization plug-in’s user interface.
- [func update()](./sfauthorizationpluginview/update%28%29.md)
  Tells the authorization plug-in to get and display the appropriate view in the authorization plug-in’s user interface.
### Constants
- [struct SFButtonType](./sfbuttontype.md)
  These constants define the button types used by authorization plug-ins.
- [struct SFViewType](./sfviewtype.md)
  These constants define the view type requested by the authorization plug-in.
- [Exceptions](./exceptions.md)
  Exceptions thrown by the `SFAuthorizationPluginView` class

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
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
- [class SFKeychainSavePanel](./sfkeychainsavepanel.md)
  A panel or sheet that allows the user to create a keychain.
- [class SFKeychainSettingsPanel](./sfkeychainsettingspanel.md)
  A panel or sheet that allows users to change their keychain settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview)*