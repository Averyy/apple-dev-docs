# ManagedApp

**Framework**: ManagedApp  
**Kind**: module

Customize your app for managed deployments by providing configurable features that rely on secure access to secrets and data that an administrator provisions.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Mentions

- [Specifying and decoding a configuration](specifying-and-decoding-a-configuration.md)
- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)

#### Overview

This framework defines API to configure managed deployments of your app for installation on multiple devices, using mobile device management (MDM). An administrator determines the configuration of, or , your app for a specific company, school, or government by creating unique configurations for people within an organization.

The framework works in conjunction with [`Device Management`](https://developer.apple.com/documentation/DeviceManagement) to provide streamlined and secure access to  and . Secrets include passwords, certificates, and identities. Configuration includes general information, for example a server URL and its timeout in seconds.

Enabling managed secrets and configuration lets an MDM admin customize the behavior of your app. For example, an MDM admin could configure an app to skip first-time setup and launch ready to use, with a person already logged in, and their app preferences or job-specific information present.

![Two iPhone renderings side by side. A device on the left features the label Unmanaged App, and a device on the right features the label Managed app. A header for the unmanaged app reads Company Name. A login prompt resides in the center of the unmanaged app’s screen with two empty text fields that read username and password respectively. A callout extends from the empty fields that reads Login required. The managed app features a header that reads Company Name and a tabbed layout. The first tab reads Dashboard and is the selected tab. The second tab reads Sales. A callout extends from the Sales tab that reads Access-control roles automatically setup. A profile area resides in the tabbed pane that features an avatar next to the name Juan Chavez. A callout extends from the profile area that reads Automatically logged in. The tabbed pane also contains a settings area and features several sliders. Some of the sliders are switched on and some are off. A callout extends from the settings pane that reads Preconfigured. A final additional area within the tabbed pane has a title that reads To Do, which contains gray rectangles representing text. A callout extends from the rectangles that reads Info loaded immediately.](https://docs-assets.developer.apple.com/published/f221c6511b51a6dc8994bce4bb214264/managedapp-1%402x.png)

#### Use Secrets to Implement Managed Features

The server-provisioned secrets and configuration available in ManagedApp enable you to add the following kinds of common Device Management features to your app:

- Enforcing the role of a person
- Receiving identities provisioned by an administrator for authentication and signing
- Receiving API access tokens
- Acquiring certificates for custom trust, for example, pinning certificates
- Using hardware-bound keys and Managed Device Attestation for strong device authentication

#### Provision Your App or App Extension

ManagedApp works with apps and app extensions. Any framework use that the documentation describes in an app also applies in app extensions.

An MDM admin can provision your app and each of its app extensions differently depending on their intended functions. For example, an MDM admin can provision your app’s [`Packet tunnel provider`](https://developer.apple.com/documentation/NetworkExtension/packet-tunnel-provider) extension using a VPN authentication identity that your app can’t access, which enhances security.

You architect the unique provisioning requirements of your app and its app extensions and communicate the requirements to MDM admins, so they can prepare accordingly.

## Topics

### Configuration
- [Specifying and decoding a configuration](specifying-and-decoding-a-configuration.md)
  Publish a configuration specification and implement a decoder that parses and validates configuration provided by an MDM admin.
- [class ManagedAppConfigurationProvider](managedappconfigurationprovider.md)
  A class that provides configurations that an MDM admin provisions for a managed app or extension.
### Secrets and identifiers
- [Accessing provisioned secrets with identifiers](accessing-provisioned-secrets-with-identifiers.md)
  Specify the secrets your app requires for device management features, receive secrets from MDM servers and use secrets in your app.
- [class ManagedAppCertificatesProvider](managedappcertificatesprovider.md)
  A class that provides certificates that an MDM admin provisions for a managed app or extension.
- [class ManagedAppIdentitiesProvider](managedappidentitiesprovider.md)
  A class that provides identities that an MDM admin provisions for a managed app or extension.
- [class ManagedAppPasswordsProvider](managedapppasswordsprovider.md)
  A class that provides passwords that an MDM admin provisions for a managed app or extension.
### Errors
- [enum ManagedAppError](managedapperror.md)
  Errors that functions in the ManagedApp framework can throw.
- [protocol ManagedAppConfigurationDecodingError](managedappconfigurationdecodingerror.md)
  A protocol for an error that describes an issue with decoding the configuration.
- [struct ManagedAppConfigurationDecodingErrorCode](managedappconfigurationdecodingerrorcode.md)
  A code for an error that occurs during configuration decoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ManagedApp)*