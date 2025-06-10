# Declarations

**Framework**: Device Management

The available declarations for device management.

## Topics

### Configurations
- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure an address book account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a Calendar subscription.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive, legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test the MDM system.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.
- [object Package](package.md)
  The declaration to install a package.
- [object PasscodeSettings](passcodesettings.md)
  The declaration to configure passcode policy settings.
- [object SafariBookmarks](safaribookmarks.md)
  The declaration to configure managed bookmarks in Safari.
- [object SafariExtensionSettings](safariextensionsettings.md)
  The declaration to configure Safari Extensions.
- [object SafariSettings](safarisettings.md)
  The declaration to configure Safari settings.
- [object ScreenSharingConnection](screensharingconnection.md)
  The declaration to configure a connection to a screen-sharing host.
- [object ScreenSharingConnectionGroup](screensharingconnectiongroup.md)
  The declaration to configure a group of screen-sharing connections.
- [object ScreenSharingHostSettings](screensharinghostsettings.md)
  The declaration to configure screen-sharing host settings and restrictions.
- [object SecurityCertificate](securitycertificate.md)
  The declaration to add a certificate to the device.
- [object SecurityIdentity](securityidentity.md)
  The declaration to install an identity on the device.
- [object SecurityPasskeyAttestation](securitypasskeyattestation.md)
  The declaration to configure the device to allow WebAuthn enterprise attestation for certain passkeys.
- [object ServicesBackgroundTasks](servicesbackgroundtasks.md)
  The declaration to configure background tasks.
- [object ServicesConfigurationFiles](servicesconfigurationfiles.md)
  The managed configuration files for services.
- [object SoftwareUpdateEnforcementSpecific](softwareupdateenforcementspecific.md)
  A software update enforcement policy for a specific OS release.
- [object SoftwareUpdateSettings](softwareupdatesettings.md)
  The declaration to configure software updates.
- [object WatchEnrollment](watchenrollment.md)
  The declaration to configure a Mobile Device Management v1 profile for Apple Watch enrollment.
### Activations
- [object ActivationSimple](activationsimple.md)
  The declaration to activate a set of configurations.
### Assets
- [object AssetCredentialACME](assetcredentialacme.md)
  A reference to an ACME identity.
- [object AssetCredentialCertificate](assetcredentialcertificate.md)
  A reference to a PKCS #1 or PEM encoded certificate.
- [object AssetCredentialIdentity](assetcredentialidentity.md)
  A reference to a PKCS #12 password-protected identity.
- [object AssetCredentialSCEP](assetcredentialscep.md)
  A reference to an SCEP identity.
- [object AssetCredentialUserNameAndPassword](assetcredentialusernameandpassword.md)
  A reference to data that describes a credential that represents a user name and password.
- [object AssetData](assetdata.md)
  A reference to arbitrary data with a specific media type.
- [object AssetUserIdentity](assetuseridentity.md)
  The user-identity data.
### Credentials
- [object ACMECredential](acmecredential.md)
  An ACME identity that the device generates.
- [object IdentityCredential](identitycredential.md)
  The data for a PKCS #12 password-protected identity.
- [object SCEPCredential](scepcredential.md)
  An SCEP identity that the device generates.
- [object UserNameAndPasswordCredential](usernameandpasswordcredential.md)
  Data that describes a credential that represents a user name and password.
### Management
- [object ManagementOrganizationInformation](managementorganizationinformation.md)
  The declaration to configure the managing organization’s contact information.
- [object ManagementProperties](managementproperties.md)
  The declaration to configure the properties on the device.
- [object ManagementServerCapabilities](managementservercapabilities.md)
  The declaration to configure the server’s feature set.
### Base Declaration
- [object DeclarationBase](declarationbase.md)
  Keys common to all declarations used with the Remote Management protocol.

## See Also

- [Leveraging the declarative management data model to scale devices](leveraging-the-declarative-management-data-model-to-scale-devices.md)
  Use declarative management to make devices more autonomous and proactive.
- [Integrating Declarative Management](integrating-declarative-management.md)
  Use the declarative management protocol to manage MDM features such as device enrollment and un-enrollment and device and user authentication.
- [Status Reports](status-reports.md)
  Reports from the device about its current state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/devicemanagement-declarations)*