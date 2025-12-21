# Displaying managed apps and packages

**Framework**: Device Management

Use a management app to display managed apps and packages to the user.

#### Overview

Device management services can use declarative management to install and manage apps on iOS, iPadOS, macOS, and visionOS devices (see [`Installing, managing, updating, and removing apps`](installing-managing-updating-and-removing-apps.md)), and install packages in macOS (see [`Installing packages`](installing-packages.md)). Both support an `Optional` install behavior that allows users to trigger installation when desired. So devices need to show managed apps and packages to users, and allow them to trigger installation.

#### Install a Management App

A  is an app that provides users with control over some aspects of the management state of a device. Device management services typically install a management app when enrolling a device, ensuring immediate user access to the app. Services set the `RequiredAppIDForMDM` key in the [`MDM`](mdm.md) profile payload to the App Store ID of the management app to ensure installation without user prompts, regardless of the device’s enrollment mode. Services can then install the management app as a `Required` app without additional user prompts.

The [`ManagedAppDistribution`](https://developer.apple.com/documentation/ManagedAppDistribution) framework provides management apps with system process UI views that display available managed apps and packages. Each managed app or package has its own view that a management app can display to allow users to see details of the app or package, trigger installation or updates, and monitor the install or update progress. Because a system extension hosts the views, the device doesn’t need to prompt for additional approval when users trigger an install. The management app can customize the layout, grouping, and sorting of the views.

If a device management service provides optional apps or packages, it needs to provide a management app that uses the [`ManagedAppDistribution`](https://developer.apple.com/documentation/ManagedAppDistribution) framework so that users can install the apps or packages.

## See Also

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)
  Use declarative management to handle all aspects of managing apps on devices.
- [Configuring managed apps and extensions](configuring-managed-apps-and-extensions.md)
  Provide managed apps and extensions with app configuration and secrets.
- [Transferring management of apps to declarative management](transferring-management-of-apps-to-declarative-management.md)
  Seamlessly transition apps to declarative management without needing to reinstall.
- [Processing status for managed apps](processing-status-for-managed-apps.md)
  Process the status that declarative management reports for managed apps.
- [Installing packages](installing-packages.md)
  Use declarative package management to install and remove packages in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/displaying-managed-apps-and-packages)*