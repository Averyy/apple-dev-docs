# ManagedAppDistribution

**Framework**: ManagedAppDistribution  
**Kind**: module

Manage the distribution of apps within an organization.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 2.4+

#### Overview

*Managed apps* are featured, downloadable apps that an enterprise, educational, or other institution provides to its employees or students. The Managed App Distribution framework allows developers of device management solutions to vend these managed apps. The framework verifies that someone initiated an app installation, provides status and download progress, and can launch the app once it’s downloaded.

> ❗ **Important**: The [`Managed App Installation UI`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.managed-app-distribution.install-ui) entitlement is required to use this framework.

![An image of an iPhone showing an app with a banner image along the top of the screen. The middle of the screen contains two app banners, one top of the other. Each app banner contains a title, subtitle, and an install button.](/images/com.apple.ManagedAppDistribution/managed-app-distribution@2x.png)

The Managed App Distribution framework works with declarative management to provide a list of managed apps that are assigned to a device. Your app can sort or filter the list of managed apps, and request a view from the Managed App Distribution framework to display. See [`Integrating declarative management`](https://developer.apple.com/documentation/devicemanagement/integrating-declarative-management) for more information.

## Topics

### Essentials
- [Fetching and displaying managed apps](fetching-and-displaying-managed-apps.md)
  Provide a consistent app presentation when displaying managed apps.
- [struct ManagedApp](managedapp.md)
  A representation of a managed app.
- [class ManagedAppLibrary](managedapplibrary.md)
  A representation of a library of managed apps.
### App information
- [struct Platform](platform.md)
  The supported platform for the app.
### View creation
- [struct ManagedAppView](managedappview.md)
  A view that displays a managed app.
- [struct ManagedContentView](managedcontentview.md)
- [struct ManagedContentOfferState](managedcontentofferstate.md)
  The state for a managed content view offer.
- [struct ManagedContentStyle](managedcontentstyle.md)
  A type that applies a custom appearance to the managed content view.
### Errors
- [enum ManagedAppDistributionError](managedappdistributionerror.md)
  Codes that identify errors in Managed App Distribution.
### Classes
- [class ManagedPackageLibrary](managedpackagelibrary.md)
  A representation of a library of managed packages.
### Structures
- [struct ManagedPackage](managedpackage.md)
  A representation of a managed package.
- [struct ManagedPackageView](managedpackageview.md)
  A view that displays information and controls for a managed software package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ManagedAppDistribution)*