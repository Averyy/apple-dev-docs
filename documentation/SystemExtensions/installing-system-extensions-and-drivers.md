# Installing System Extensions and Drivers

**Framework**: Systemextensions

Activate system extensions and drivers to make them available to the system, and update or deactivate them as needed.

#### Overview

Instead of installing system extensions using an installer, you ship system extensions inside your app’s bundle and install them from your app. Request activation of any system extensions as early as possible in your app’s launch. Doing so helps the system seamlessly update the extension when updating the app. Depending on your app, you may choose to request activation later. For example, you might delay activation until after the user accepts a license agreement or makes an in-app purchase.

System extensions reside inside your app’s `Contents/Library/SystemExtensions` folder. When the user launches your app, use the SystemExtensions framework to activate your driver and make it available for use. During the activation process, the system checks the validity of your driver—for example, by verifying that it has the proper entitlements to run. The specific checks depend on the type of system extension you activate.

##### Activate a New System Extension

To start the activation process for your system extension, create an activation request by calling the [`activationRequest(forExtensionWithIdentifier:queue:)`](ossystemextensionrequest/activationrequest(forextensionwithidentifier:queue:).md) method of [`OSSystemExtensionRequest`](ossystemextensionrequest.md). When you submit that request object to the [`OSSystemExtensionManager`](ossystemextensionmanager.md), the system begins the activation process and reports the results back to the delegate object you specify. The following code shows the activation steps for a DriverKit extension.

```swift
// Create an activation request and assign a delegate to
// receive reports of success or failure.
let request = OSSystemExtensionRequest.activationRequest(forExtensionWithIdentifier: driverID,
                     queue: DispatchQueue.main)
request.delegate = self

// Submit the request to the system.
let extensionManager = OSSystemExtensionManager.shared
extensionManager.submitRequest(request)
```

During the activation process, the system verifies:

- Your extension is installed in the `Contents/Library/SystemExtensions` folder of your app.
- Your app is installed in an appropriate `Applications` directory of the system.
- The code signature of your extension.
- The entitlements in the code signature match the entitlements granted to your development team.
- The identifer in your activation request matches the one in your system extension bundle.
- The identifier isn’t already in use by another system extension.

If the verification process fails, the system reports the error back to your delegate’s [`request(_:didFailWithError:)`](ossystemextensionrequestdelegate/request(_:didfailwitherror:).md) method. Use the error code to identify the reason for the failure so that you can correct it.

> **Note**:  During development, you can disable some verification checks to simplify testing your system extensions. For more information, see Debugging and Testing System Extensions.

##### Update an Existing System Extension

To update a driver, increment the driver’s version and activate it using the same process for new system extensions. When the system detects an existing extension with the same identifier, it passes the version information for both extensions to the [`request(_:actionForReplacingExtension:withExtension:)`](ossystemextensionrequestdelegate/request(_:actionforreplacingextension:withextension:).md) method of your request delegate. Use that information to determine whether you want to install the new extension or keep the old one.

For more information about implementing the delegate methods for your request, see [`OSSystemExtensionRequestDelegate`](ossystemextensionrequestdelegate.md).

##### Uninstall a System Extension

The system automatically uninstalls any system extensions when the user deletes the corresponding app. You can also uninstall a system extension by creating a deactivation request. Call the [`deactivationRequest(forExtensionWithIdentifier:queue:)`](ossystemextensionrequest/deactivationrequest(forextensionwithidentifier:queue:).md) method of [`OSSystemExtensionRequest`](ossystemextensionrequest.md) and submit the resulting object to the [`OSSystemExtensionManager`](ossystemextensionmanager.md).

##### Examine the Installed System Extensions

To see the system extensions installed on your system, run the `systemextensionsctl` command-line tool with the `list` option from Terminal.

`% systemextensionsctl list`

For more information about how to use the `systemextensionsctl` tool, see the man pages.

## See Also

- [class OSSystemExtensionManager](ossystemextensionmanager.md)
  A type that facilitates activation and deactivation of system extensions.
- [class OSSystemExtensionRequest](ossystemextensionrequest.md)
  A request to activate or deactivate a system extension.
- [System Extension Redistributable Entitlement](../BundleResources/Entitlements/com.apple.developer.system-extension.redistributable.md)
  A Boolean value that indicates whether other development teams may distribute a system extension you create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SystemExtensions/installing-system-extensions-and-drivers)*