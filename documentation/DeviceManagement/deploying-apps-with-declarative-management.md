# Deploying apps with declarative management

**Framework**: Device Management

Use declarative app configurations to deploy managed apps to devices.

#### Overview

Device management services can install, manage, update, configure, and remove apps using the [`AppManaged`](appmanaged.md) configuration. Devices can report managed app status using the [`StatusAppManagedList`](statusappmanagedlist.md) status item.

If a device management service already manages an app using the [`Install Application`](install-application-command.md) or [`Install Enterprise Application`](install-enterprise-application-command.md) commands, it can convert the app to declarative app management.

In macOS, device management services can install, update, and remove packages using the [`Package`](package.md) configuration. They can then manage apps that a package installs using an [`AppManaged`](appmanaged.md) configuration targeting the app. Devices can report package status using the [`StatusPackageList`](statuspackagelist.md) status item.

## Topics

### Supporting managed apps
- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)
  Use declarative management to handle all aspects of managing apps on devices.
- [Displaying managed apps and packages](displaying-managed-apps-and-packages.md)
  Use a management app to display managed apps and packages to the user.
- [Configuring managed apps and extensions](configuring-managed-apps-and-extensions.md)
  Provide managed apps and extensions with app configuration and secrets.
- [Transferring management of apps to declarative management](transferring-management-of-apps-to-declarative-management.md)
  Seamlessly transition apps to declarative management without needing to reinstall.
- [Processing status for managed apps](processing-status-for-managed-apps.md)
  Process the status that declarative management reports for managed apps.
- [Installing packages](installing-packages.md)
  Use declarative package management to install and remove packages in macOS.

## See Also

- [Leveraging the declarative management data model to scale devices](leveraging-the-declarative-management-data-model-to-scale-devices.md)
  Use declarative management to make devices more autonomous and proactive.
- [Integrating Declarative Management](integrating-declarative-management.md)
  Use the declarative management protocol to manage MDM features such as device enrollment and un-enrollment and device and user authentication.
- [Declarations](devicemanagement-declarations.md)
  The available declarations for device management.
- [Status Reports](status-reports.md)
  Reports from the device about its current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deploying-apps-with-declarative-management)*