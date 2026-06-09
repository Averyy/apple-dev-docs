# Device Management

**Framework**: Device Management  
**Kind**: module

Manage your organization’s devices remotely.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.1+
- watchOS 6.0+
- Device Assignment Services 5.0+
- VPP License Management 1.0+

#### Overview

Deploying a device management service allows administrators to securely and remotely configure enrolled devices. Administrators use Apple School Manager or Apple Business Manager to enroll organization-owned devices, and users can enroll their own devices. After enrolling a device, administrators can update software and device settings; monitor compliance with organizational policies; remotely erase or lock devices; and install apps, books, and subscriptions developed in-house or purchased through Apple School Manager or Apple Business Manager.

A device management service uses the Mobile Device Management (MDM) protocol to establish a communication channel with devices and declarative configurations, as well as configuration profiles to deploy settings.

Device management works with Managed App Distribution and Managed App Configuration to provide a seamless app download and launch experience. For more information, see [`ManagedAppDistribution`](https://developer.apple.com/documentation/ManagedAppDistribution) and [`ManagedApp`](https://developer.apple.com/documentation/ManagedApp).

## Topics

### Implementing device management
- [Device management essentials](device-management-essentials.md)
  Set up and maintain connectivity with devices and leverage declarative device management.
- [Device enrollment](device-enrollment.md)
  Implement Automated Device Enrollment and account-driven enrollments.
- [Identity management](identity-management.md)
  Use Platform Single Sign-on and Managed Device Attestation on managed devices.
- [Content management](content-management.md)
  Deploy apps and books to managed devices.
- [Device life cycle](device-life-cycle.md)
  Manage software updates, migrate managed devices, and return them into service.
### MDM protocol
- [Commands and queries](commands-and-queries.md)
  Remotely execute management commands and queries on managed devices.
- [Check-in](check-in.md)
  Authenticate devices and maintain push tokens.
### Declarative management
- [Declarations](devicemanagement-declarations.md)
  Configure devices using declarative device management.
- [Status items](status-items.md)
  Monitor device state using status reports.
### Configuration profiles
- [Profile-specific payload keys](profile-specific-payload-keys.md)
  Apply settings to devices using configuration profiles.
### Miscellaneous data formats
- [object ManifestURL](manifesturl.md)
  The URL to the app manifest.
- [object PasswordHash](passwordhash.md)
  A dictionary that contains the password hash for the account.
### Deployment services
- [Device assignment](device-assignment.md)
  Manage devices for your students and employees.
- [Roster management](roster-management.md)
  Manage classes for your students and teachers.
- [App, Book, and Subscription Management](app-book-and-subscription-management.md)
  Manage apps, books, and subscriptions for your students and employees.
- [Apple School Manager and Apple Business APIs](../apple-school-and-business-manager-api/apple-school-and-business-manager-api.md)
  Automate device management actions and access data about devices that enroll using Automated Device Enrollment with the Apple School Manager and Apple Business APIs.
### Dictionaries
- [object ResponseErrorCode](responseerrorcode.md)
  An error code.
- [object StorefrontsResponse](storefrontsresponse.md)
  The response to a storefront request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement)*