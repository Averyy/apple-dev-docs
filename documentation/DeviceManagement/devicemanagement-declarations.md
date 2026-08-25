# Declarations

**Framework**: Device Management

Configure devices using declarative device management.

## Topics

### Configurations
- [object AccessibilitySettings](accessibilitysettings.md)
  The declaration to configure accessibility settings.
- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.
- [object KeyboardSettings](keyboardsettings.md)
  The declaration to configure keyboard settings.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to configure a declarative device management test.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.
- [object MigrationAssistantSettings](migrationassistantsettings.md)
  The declaration to configure Migration Assistant settings.
- [object NetworkDNSProxy](networkdnsproxy.md)
  The declaration to configure DNS proxy settings.
- [object NetworkDNSSettings](networkdnssettings.md)
  The declaration to configure encrypted DNS settings.
- [object NetworkRelay](networkrelay.md)
  The declaration to configure Network Relay settings.
- [object NetworkVPNAlwaysOn](networkvpnalwayson.md)
  The declaration to configure a VPN using the Always On sub-type.
- [object NetworkVPNIKEV2](networkvpnikev2.md)
  The declaration to configure a VPN using the IKEv2 sub-type.
- [object NetworkVPNIPSec](networkvpnipsec.md)
  The declaration to configure a VPN using the IPSec sub-type.
- [object NetworkVPNVPNPlugin](networkvpnvpnplugin.md)
  The declaration to configure a VPN using the VPN plugin sub-type.
- [object Package](package.md)
  The declaration to configure a package.
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
  The declaration to configure a certificate.
- [object SecurityIdentity](securityidentity.md)
  The declaration to configure an identity.
- [object SecurityPasskeyAttestation](securitypasskeyattestation.md)
  The declaration to configure the device to allow WebAuthn enterprise attestation for certain passkeys.
- [object ServicesBackgroundTasks](servicesbackgroundtasks.md)
  The declaration to configure background tasks.
- [object ServicesConfigurationFiles](servicesconfigurationfiles.md)
  The declaration to configure managed configuration files for services.
- [object SiriSettings](sirisettings.md)
  The declaration to configure Siri settings.
- [object SoftwareUpdateEnforcementSpecific](softwareupdateenforcementspecific.md)
  The declaration to configure a software update enforcement policy for a specific OS release.
- [object SoftwareUpdateSettings](softwareupdatesettings.md)
  The declaration to configure software updates.
- [object WatchEnrollment](watchenrollment.md)
  The declaration to configure an MDMv1 profile for Apple Watch enrollment.
- [object WebContentFilterPlugin](webcontentfilterplugin.md)
  The declaration to configure a WebContent Filter that uses a plugin.
### Activations
- [object ActivationSimple](activationsimple.md)
  The declaration to activate a set of configurations.
### Assets
- [object AssetCredentialACME](assetcredentialacme.md)
  A reference to an ACME identity.
- [object AssetCredentialCertificate](assetcredentialcertificate.md)
  A reference to one PKCS #1 or PEM encoded certificate.
- [object AssetCredentialIdentity](assetcredentialidentity.md)
  A reference to a PKCS #12 password-protected identity.
- [object AssetCredentialSCEP](assetcredentialscep.md)
  A reference to a SCEP identity.
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
  A SCEP identity that the device generates.
- [object UserNameAndPasswordCredential](usernameandpasswordcredential.md)
  Data that describes a credential that represents a user name and password.
### Management
- [object ManagementOrganizationInformation](managementorganizationinformation.md)
  The declaration to configure the managing organization’s contact information.
- [object ManagementProperties](managementproperties.md)
  The declaration to configure the properties on the device.
- [object ManagementServerCapabilities](managementservercapabilities.md)
  The declaration to configure the server’s feature set.
### Base declaration
- [object DeclarationBase](declarationbase.md)
  Keys common to all declarations used with the Remote Management protocol.

## See Also

- [Status items](status-items.md)
  Monitor device state using status reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/devicemanagement-declarations)*