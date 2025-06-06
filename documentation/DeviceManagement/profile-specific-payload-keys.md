# Profile-Specific Payload Keys

**Framework**: Device Management

Use the appropriate payload for your configuration needs.

#### Overview

In addition to the standard payload keys (described in [`Define a Profile`](configuring-multiple-devices-using-profiles#Define-a-Profile.md)) each payload can contain keys specific to a payload type. These payload specific keys are described in detail, below.

For profiles that use paths, consider them to be case sensitive.

## Topics

### Top Level
- [object TopLevel](toplevel.md)
  The top-level payload properties you use to configure all profiles.
- [object CommonPayloadKeys](commonpayloadkeys.md)
  The payload properties that are common across all profiles.
### Accounts
- [object Accounts](accounts.md)
  The payload you use to configure guest accounts.
- [object CalDAV](caldav.md)
  The payload you use to configure a Calendar account.
- [object CardDAV](carddav.md)
  The payload you use to configure a Contacts account.
- [object GoogleAccount](googleaccount.md)
  The payload you use to configure a Google account.
- [object LDAP](ldap.md)
  The payload you use to configure an LDAP account.
- [object MobileAccounts](mobileaccounts.md)
  The payload you use to configure mobile accounts on the device.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload you use to configure subscribed calendars.
### AirPlay
- [object AirPlay](airplay.md)
  The payload you use to configure AirPlay settings.
- [object AirPlaySecurity](airplaysecurity.md)
  The payload you use to configure Apple TV for a particular style of AirPlay security.
### App Management
- [object AppLock](applock.md)
  The payload you use to configure a device to run a single app.
- [object AssociatedDomains](associateddomains.md)
  The payload you use to configure associated domains.
- [object AutonomousSingleAppMode](autonomoussingleappmode.md)
  The payload you use to configure Autonomous Single App mode.
- [object NSExtensionManagement](nsextensionmanagement.md)
  The payload you use to configure the extensions that the system allows or disallows to run on the device.
### App Store
- [object AppStore](appstore.md)
  The payload you use to configure macOS App Store restrictions.
### Apple TV
- [object ConferenceRoomDisplay](conferenceroomdisplay.md)
  The payload you use to configure Conference Room Display mode for Apple TV.
- [object TVRemote](tvremote.md)
  The payload you use to configure the Apple TV remote.
### Authentication
- [object DirectoryService](directoryservice.md)
  The payload you use to configure an Active Directory (AD) domain.
- [object ExtensibleSingleSignOn](extensiblesinglesignon.md)
  The payload you use to configure an app extension that performs single sign-on (SSO).
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload you use to configure an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload you use to configure the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload you use to configure the user’s identity on the device.
- [object SingleSignOn](singlesignon.md)
  The payload you use to configure single sign-on (SSO).
### Certificates
- [object ACMECertificate](acmecertificate.md)
  The payload you use to configure Automated Certificate Management Environment (ACME) Certificate settings.
- [object ActiveDirectoryCertificate](activedirectorycertificate.md)
  The payload you use to configure Active Directory Certificate settings.
- [object CertificatePEM](certificatepem.md)
  The payload you use to configure a PEM-formatted certificate.
- [object CertificatePKCS1](certificatepkcs1.md)
  The payload you use to configure a PKCS #1-formatted certificate.
- [object CertificatePKCS12](certificatepkcs12.md)
  The payload you use to configure a PKCS #12-formatted certificate.
- [object CertificateRoot](certificateroot.md)
  The payload you use to configure a root certificate.
- [object CertificatePreference](certificatepreference.md)
  The payload you use to configure a certificate preference.
- [object CertificateRevocation](certificaterevocation.md)
  The payload you use to configure certificate revocation checking.
- [object CertificateTransparency](certificatetransparency.md)
  The payload you use to configure certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload you use to configure Simple Certificate Enrollment Protocol (SCEP).
### Ethernet
- [object 8021XGlobalEthernet](8021xglobalethernet.md)
  The payload you use to configure the default fallback global Ethernet interface.
- [type 8021XFirstActiveEthernet](8021xfirstactiveethernet.md)
  The payload you use to configure the first wired, active Ethernet interface.
- [type 8021XFirstEthernet](8021xfirstethernet.md)
  The payload you use to configure the first wired Ethernet interface.
- [type 8021XSecondActiveEthernet](8021xsecondactiveethernet.md)
  The payload you use to configure the second wired, active Ethernet interface.
- [type 8021XSecondEthernet](8021xsecondethernet.md)
  The payload you use to configure the second wired Ethernet interface.
- [type 8021XThirdActiveEthernet](8021xthirdactiveethernet.md)
  The payload you use to configure the third wired, active Ethernet interface.
- [type 8021XThirdEthernet](8021xthirdethernet.md)
  The payload you use to configure the third wired Ethernet interface.
### Full Disk Encryption
- [object FDEFileVault](fdefilevault.md)
  The payload you use to configure FileVault.
- [object FDEFileVaultOptions](fdefilevaultoptions.md)
  The payload you use to configure FileVault options.
- [object FDERecoveryKeyEscrow](fderecoverykeyescrow.md)
  The payload you use to configure FileVault recovery key escrow.
### Login
- [object LoginItemsManagedItems](loginitemsmanageditems.md)
  The payload you use to configure a device’s login items.
- [object LoginWindowLoginItems](loginwindowloginitems.md)
  The payload you use to configure login behavior.
- [object LoginWindow](loginwindow.md)
  The payload you use to configure login window behavior.
- [object LoginWindowScripts](loginwindowscripts.md)
  The payload you use to configure scripts to run at login and logout.
- [object ServiceManagementManagedLoginItems](servicemanagementmanagedloginitems.md)
  This payload you use to configure managed login items, which auto-enables and auto-allows matched items.
### Mail
- [object ExchangeActiveSync](exchangeactivesync.md)
  The payload you use to configure Exchange ActiveSync accounts.
- [object ExchangeWebServices](exchangewebservices.md)
  The payload you use to configure an Exchange Web Services account for Contacts, Mail, Notes, Reminders, and Calendar.
- [object Mail](mail.md)
  The payload you use to configure a mail account on the device.
### Managed Devices
- [object EducationConfiguration](educationconfiguration.md)
  The payload you use to configure the users, groups, and departments within an educational organization.
- [object LightsOutManagementLOM](lightsoutmanagementlom.md)
  The payload you use to configure lights-out management (LOM) settings.
- [object ManagedPreferences](managedpreferences.md)
  The payload you use to configure managed preferences.
- [object MDM](mdm.md)
  The payload you use to configure mobile device management (MDM) settings.
- [object ProfileRemovalPassword](profileremovalpassword.md)
  The payload you use to configure profile removal.
### Media Management
- [object MediaManagementDiscBurning](mediamanagementdiscburning.md)
  The payload you use to configure disc-burning settings.
### Networking
- [object Cellular](cellular.md)
  The payload you use to configure cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload to provide device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object ContentCaching](contentcaching.md)
  The payload you use to configure the content-caching service.
- [object DNSSettings](dnssettings.md)
  The payload you use to configure encrypted DNS settings.
- [object Domains](domains.md)
  The payload you use to configure the domains under an organization’s management.
- [object Firewall](firewall.md)
  The payload you use to configure the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload you use to configure network-usage rules.
- [object Relay](relay.md)
  The payload you use to configure relay settings.
- [object WiFi](wifi.md)
  The payload you use to configure Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload you use to configure managed Wi-Fi settings.
### Parental Controls
- [object ParentalControlsApplicationRestrictions](parentalcontrolsapplicationrestrictions.md)
  The payload you use to configure parental controls for apps.
- [object ParentalControlsContentFilter](parentalcontrolscontentfilter.md)
  The payload you use to configure the parental control web content filters.
- [object ParentalControlsDictionary](parentalcontrolsdictionary.md)
  The payload you use to configure parental control dictionary restrictions.
- [object ParentalControlsGameCenter](parentalcontrolsgamecenter.md)
  The payload you use to configure Game Center parental controls.
- [object ParentalControlsTimeLimits](parentalcontrolstimelimits.md)
  The payload you use to configure parental control time limits.
### Preferences
- [object GlobalPreferences](globalpreferences.md)
  The payload you use to configure global preferences.
- [object UserPreferences](userpreferences.md)
  The payload you use to configure iCloud password preferences.
### Printing
- [object AirPrint](airprint.md)
  The payload you use to configure AirPrint printers in the user’s printer list.
- [object Printing](printing.md)
  The payload you use to configure printers.
### Privacy
- [object PrivacyPreferencesPolicyControl](privacypreferencespolicycontrol.md)
  The payload you use to configure privacy preferences.
### Proxies
- [object DNSProxy](dnsproxy.md)
  The payload you use to configure DNS proxies.
- [object GlobalHTTPProxy](globalhttpproxy.md)
  The payload you use to configure a global HTTP proxy.
- [object NetworkProxyConfiguration](networkproxyconfiguration.md)
  The payload you use to configure network proxies for a device.
### Restrictions
- [object Restrictions](restrictions.md)
  The payload you use to configure restrictions on a device.
### Security
- [object Passcode](passcode.md)
  The payload you use to configure a passcode policy.
- [object SecurityPreferences](securitypreferences.md)
  The payload you use to configure security preferences.
- [object SmartCard](smartcard.md)
  The payload you use to configure a smart card.
### System Configuration
- [object Declarations](declarations.md)
  The payload to apply a set of declaration to the device through the Settings app.
- [object EnergySaver](energysaver.md)
  The payload you use to configure energy-saver settings.
- [object FileProvider](fileprovider.md)
  The payload you use to configure file provider settings.
- [object Font](font.md)
  The payload you use to configure fonts.
- [object LockScreenMessage](lockscreenmessage.md)
  The payload you use to configure a Lock screen message.
- [object Screensaver](screensaver.md)
  The payload you use to configure the screen saver.
- [object SystemExtensions](systemextensions.md)
  The payload you use to configure system extensions.
- [object SystemLogging](systemlogging.md)
  The payload you use to configure system logging.
- [object TimeServer](timeserver.md)
  The payload you use to configure the time server.
### System Policy
- [object SystemPolicyControl](systempolicycontrol.md)
  The payload you use to configure the system policy for assessments.
- [object SystemPolicyKernelExtensions](systempolicykernelextensions.md)
  The payload you use to configure the kernel extension policies.
- [object SystemPolicyManaged](systempolicymanaged.md)
  The payload you use to configure the Finder’s contextual menu to bypass the system policy.
- [object SystemPolicyRule](systempolicyrule.md)
  The payload you use to configure the system policy.
### System Updates
- [object SoftwareUpdate](softwareupdate.md)
  The payload you use to configure the software update policy.
- [object SystemMigration](systemmigration.md)
  The payload you use to configure system migration.
### User Experience
- [object Accessibility](accessibility.md)
  The payload you use to configure the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload you use to configure the desktop.
- [object Dock](dock.md)
  The payload you use to configure the dock.
- [object Finder](finder.md)
  The payload you use to configure Finder settings.
- [object HomeScreenLayout](homescreenlayout.md)
  The payload you use to configure the Home screen layout.
- [object ManagedMenuExtras](managedmenuextras.md)
  The payload you use to configure menu extras.
- [object Notifications](notifications.md)
  The payload you use to configure notifications.
- [object ScreensaverUser](screensaveruser.md)
  The payload you use to configure a user’s screen-saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload you use to configure setup-assistant settings.
- [object TimeMachine](timemachine.md)
  The payload you use to configure Time Machine.
### VPN
- [object AppLayerVPN](applayervpn.md)
  The payload you use to configure add-on VPN software.
- [object AppToAppLayerVPNMapping](apptoapplayervpnmapping.md)
  The payload you use to configure per-app VPN settings.
- [object VPN](vpn.md)
  The payload you use to configure a VPN.
### Web
- [object WebClip](webclip.md)
  The profile you use to configure web clips on the device.
- [object WebContentFilter](webcontentfilter.md)
  The payload you use to configure web content filters.
### Xsan
- [object Xsan](xsan.md)
  The payload you use to configure an Xsan client system.
- [object XsanPreferences](xsanpreferences.md)
  The payload you use to configure the Xsan preferences that define the volumes that automatically mount at startup.
### Deprecated
- [object AIMAccount](aimaccount.md)
  The payload you use to configure an AIM account on the device.
- [object APN](apn.md)
  The payload you use to configure access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload you use to configure FileVault recovery key redirection.
- [object JabberAccount](jabberaccount.md)
  The payload you use to configure a Jabber account.
- [object MacOSServerAccount](macosserveraccount.md)
  The payload you use to configure a macOS server account.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload you use to configure media management.
- [object ParentalControlsDashboardWidgetRestrictions](parentalcontrolsdashboardwidgetrestrictions.md)
  The payload you use to configure the parental control dashboard allow list.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload you use to configure parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload you use to configure ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload you use to configure the preference panes.

## See Also

- [Configuring Multiple Devices Using Profiles](configuring-multiple-devices-using-profiles.md)
  Create and deploy configuration profiles to users within your organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profile-specific-payload-keys)*