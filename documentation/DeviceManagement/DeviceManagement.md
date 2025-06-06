# Device Management

**Framework**: Device Management  
**Kind**: module

Manage your organization’s devices remotely.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.1+
- watchOS 6.0+
- Device Assignment Services 5.0+
- VPP License Management 1.0+

#### Overview

Deploying a mobile device management (MDM) solution allows administrators to securely and remotely configure enrolled devices. Administrators use Apple School Manager or Apple Business Manager to enroll organization-owned devices, and users can enroll their own devices. Once a device is enrolled, administrators can update software and device settings, monitor compliance with organizational policies, remotely erase or lock devices, and install apps and books developed in-house or purchased through Apple School Manager or Apple Business Manager.

MDM works with Managed App Distribution to provide a great download and launch experience. For more information, see Managed App Distribution.

## Topics

### Configuration Profiles
- [Configuring Multiple Devices Using Profiles](configuring-multiple-devices-using-profiles.md)
  Create and deploy configuration profiles to users within your organization.
- [Profile-Specific Payload Keys](profile-specific-payload-keys.md)
  Use the appropriate payload for your configuration needs.
### MDM Protocol
- [Implementing Device Management](implementing-device-management.md)
  Set up an MDM server and send commands to managed devices.
- [Commands and Queries](commands-and-queries.md)
  Manage the configuration and behavior of your devices.
- [Check-in](check-in.md)
  Authenticate devices and maintain push tokens with these commands.
- [User Enrollment](user-enrollment.md)
  Authenticate devices using an user identity focused workflow.
### Declarative Management
- [Leveraging the declarative management data model to scale devices](leveraging-the-declarative-management-data-model-to-scale-devices.md)
  Use declarative management to make devices more autonomous and proactive.
- [Integrating Declarative Management](integrating-declarative-management.md)
  Use the declarative management protocol to manage MDM features such as device enrollment and un-enrollment and device and user authentication.
- [Declarations](devicemanagement-declarations.md)
  The available declarations for device management.
- [Status Reports](status-reports.md)
  Reports from the device about its current state.
### Deployment Services
- [Device Assignment](device-assignment.md)
  Manage devices for your students and employees.
- [Roster Management](roster-management.md)
  Manage classes for your students and teachers.
- [App and Book Management](app-and-book-management.md)
  Manage apps and books for your students and employees.
### Endpoints
- [Fetch a apps resource's relationship](fetch-a-apps-resource's-relationship.md)
- [Fetch a books resource's relationship](fetch-a-books-resource's-relationship.md)
- [Get Multiple Genres](get-multiple-genres.md)
  Fetch metadata for genres from the catalog by using their identifiers.
- [Get a Genre](get-a-genre.md)
  Fetch metadata for a genre from the catalog by using its identifier.
### Objects
- [object ErrorUnrecognizedDevice](errorunrecognizeddevice.md)
- [object ErrorWellKnownFailed](errorwellknownfailed.md)
### Dictionaries
- [object ManifestURL](manifesturl.md)
  The URL to the app manifest.
- [object PasswordHash](passwordhash.md)
  A dictionary that contains the password hash for the account.
- [object RelationshipResponse](relationshipresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/DeviceManagement)*