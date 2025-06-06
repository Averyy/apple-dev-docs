# System Extensions

**Framework**: System Extensions  
**Kind**: module

Install and manage user space code that extends the capabilities of macOS.

**Availability**:
- macOS 10.15+

## Mentions

- [Implementing drivers, system extensions, and kexts](implementing-drivers-system-extensions-and-kexts.md)

#### Overview

Extend the capabilities of macOS by installing and managing system extensions—drivers and other low-level code—in user space rather than in the kernel. By running in user space, system extensions can’t compromise the security or stability of macOS. The system grants these extensions a high level of privilege, so they can perform the kinds of tasks previously reserved for kernel extensions (KEXTs).

You use frameworks like [`DriverKit`](https://developer.apple.com/documentation/DriverKit), [`Endpoint Security`](https://developer.apple.com/documentation/EndpointSecurity), and [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) to write your system extension, and you package the extension in your app bundle. At runtime, use the SystemExtensions framework to install or update the extension on the user’s system. Once installed, an extension remains available for all users on the system. Users can disable the extension by deleting the app, which deletes the extension.

##### Configure the System Extension and the Host App

To successfully activate your extension, you must adhere to the following rules:

- The extension must match your bundle identifier, excluding file extension. For example, a DriverKit extension with bundle identifier `com.example.usbdriver` must use the filename `com.example.usbdriver.dext`. Similarly, a NetworkExtension extension with bundle identifier `com.example.networkextension` must use the filename `com.example.networkextension.systemextension`.
- You must use the same Team ID when signing the extension that you use for signing your app, unless the extension has the `com.apple.developer.system-extension.redistributable` entitlement.
- You must either distribute your app and extension through the Mac App Store, or notarize them. See [`Notarizing macOS software before distribution`](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution) to learn more about notarization.

## Topics

### Essentials
- [Implementing drivers, system extensions, and kexts](implementing-drivers-system-extensions-and-kexts.md)
  Create drivers and system extensions to communicate with hardware and provide low-level services, and only use kernel extensions for a few tasks.
- [Debugging and testing system extensions](../DriverKit/debugging-and-testing-system-extensions.md)
  Debug your system extensions by temporarily disabling the security checks that macOS performs during the installation process.
- [System Extension Entitlement](../BundleResources/Entitlements/com.apple.developer.system-extension.install.md)
  A Boolean value that indicates whether your app has permission to activate or deactivate system extensions.
### Usage descriptions
- [let NSSystemExtensionUsageDescriptionKey: String](nssystemextensionusagedescriptionkey.md)
  A message that tells the user why the app is trying to install a system extension bundle.
- [let OSBundleUsageDescriptionKey: String](osbundleusagedescriptionkey.md)
  A message that tells the user why the app is trying to install a driver extension bundle.
### Extension activation and deactivation
- [Installing System Extensions and Drivers](installing-system-extensions-and-drivers.md)
  Activate system extensions and drivers to make them available to the system, and update or deactivate them as needed.
- [class OSSystemExtensionManager](ossystemextensionmanager.md)
  A type that facilitates activation and deactivation of system extensions.
- [class OSSystemExtensionRequest](ossystemextensionrequest.md)
  A request to activate or deactivate a system extension.
- [System Extension Redistributable Entitlement](../BundleResources/Entitlements/com.apple.developer.system-extension.redistributable.md)
  A Boolean value that indicates whether other development teams may distribute a system extension you create.
### Errors
- [struct OSSystemExtensionError](ossystemextensionerror.md)
  An error that describes a failed extension manager request.
- [OSSystemExtensionError.Code](ossystemextensionerror/code.md)
  Error codes for system extensions.
- [let OSSystemExtensionErrorDomain: String](ossystemextensionerrordomain.md)
  The error domain identifying system extension errors.
### Reference
- [SystemExtensions Constants](systemextensions-constants.md)
### Classes
- [class OSSystemExtensionInfo](ossystemextensioninfo.md)
- [class OSSystemExtensionsWorkspace](ossystemextensionsworkspace.md)
### Protocols
- [protocol OSSystemExtensionsWorkspaceObserver](ossystemextensionsworkspaceobserver.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/SystemExtensions)*