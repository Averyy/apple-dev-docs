# Profile-Specific Payload Keys

**Framework**: Device Management

Use the appropriate payload for your configuration needs.

#### Overview

In addition to the standard payload keys (described in [`Define a Profile`](configuring-multiple-devices-using-profiles#Define-a-Profile.md)) each payload can contain keys specific to a payload type. These payload specific keys are described in detail, below.

For profiles that use paths, consider them to be case sensitive.

## Topics

### Top Level
- [object TopLevel](toplevel.md)
  The top-level payload properties for all profiles.
- [object CommonPayloadKeys](commonpayloadkeys.md)
  The properties common to all payloads.
### Accounts
- [object Accounts](accounts.md)
  The payload that configures guest accounts.
- [object CalDAV](caldav.md)
  The payload that configures a Calendar account.
- [object CardDAV](carddav.md)
  The payload that configures a Contacts account.
- [object GoogleAccount](googleaccount.md)
  The payload that configures a Google account.
- [object LDAP](ldap.md)
  The payload that configures a Lightweight Directory Access Protocol (LDAP) account.
- [object MobileAccounts](mobileaccounts.md)
  The payload that configures mobile accounts on the device.
- [object SubscribedCalendars](subscribedcalendars.md)
  The payload that configures subscribed calendars.
### AirPlay
- [object AirPlay](airplay.md)
  The payload that configures AirPlay settings.
- [object AirPlaySecurity](airplaysecurity.md)
  The payload that configures Apple TV for a particular style of AirPlay security.
### App Management
- [object AppLock](applock.md)
  The payload that configures a device to run a single app.
- [object AssociatedDomains](associateddomains.md)
  The payload that configures associated domains.
- [object AutonomousSingleAppMode](autonomoussingleappmode.md)
  The payload that configures Autonomous Single App mode.
- [object NSExtensionManagement](nsextensionmanagement.md)
  The payload that configures the extensions that the system allows or disallows to run on the device.
### App Store
- [object AppStore](appstore.md)
  The payload that configures macOS App Store restrictions.
### Apple TV
- [object ConferenceRoomDisplay](conferenceroomdisplay.md)
  The payload that configures Conference Room Display mode for Apple TV.
- [object TVRemote](tvremote.md)
  The payload that configures the Apple TV remote.
### Authentication
- [object DirectoryService](directoryservice.md)
  The payload that configures an Active Directory (AD) domain.
- [object ExtensibleSingleSignOn](extensiblesinglesignon.md)
  The payload that configures an app extension that performs single sign-on (SSO).
- [object ExtensibleSingleSignOnKerberos](extensiblesinglesignonkerberos.md)
  The payload that configures an app extension that performs single sign-on with the Kerberos extension.
- [object Identification](identification.md)
  The payload that configures the names of the account user.
- [object IdentityPreference](identitypreference.md)
  The payload that configures the user’s identity on the device.
- [object SingleSignOn](singlesignon.md)
  The payload that configures single sign-on (SSO).
### Certificates
- [object ACMECertificate](acmecertificate.md)
  The payload that configures Automated Certificate Management Environment (ACME) settings.
- [object ActiveDirectoryCertificate](activedirectorycertificate.md)
  The payload that configures Active Directory Certificate settings.
- [object CertificatePEM](certificatepem.md)
  The payload that configures a PEM-formatted certificate.
- [object CertificatePKCS1](certificatepkcs1.md)
  The payload that configures a PKCS #1-formatted certificate.
- [object CertificatePKCS12](certificatepkcs12.md)
  The payload that configures a PKCS #12-formatted certificate.
- [object CertificateRoot](certificateroot.md)
  The payload that configures a root certificate.
- [object CertificatePreference](certificatepreference.md)
  The payload that configures a certificate preference.
- [object CertificateRevocation](certificaterevocation.md)
  The payload that configures certificate revocation checking.
- [object CertificateTransparency](certificatetransparency.md)
  The payload that configures certificate transparency enforcement.
- [object SCEP](scep.md)
  The payload that configures Simple Certificate Enrollment Protocol (SCEP) settings.
### Ethernet
- [object 8021XGlobalEthernet](8021xglobalethernet.md)
  The payload that configures the default fallback global Ethernet interface.
- [type 8021XFirstActiveEthernet](8021xfirstactiveethernet.md)
  The payload that configures the first wired, active Ethernet interface.
- [type 8021XFirstEthernet](8021xfirstethernet.md)
  The payload that configures the first wired Ethernet interface.
- [type 8021XSecondActiveEthernet](8021xsecondactiveethernet.md)
  The payload that configures the second wired, active Ethernet interface.
- [type 8021XSecondEthernet](8021xsecondethernet.md)
  The payload that configures the second wired Ethernet interface.
- [type 8021XThirdActiveEthernet](8021xthirdactiveethernet.md)
  The payload that configures the third wired, active Ethernet interface.
- [type 8021XThirdEthernet](8021xthirdethernet.md)
  The payload that configures the third wired Ethernet interface.
### Full Disk Encryption
- [object FDEFileVault](fdefilevault.md)
  The payload that configures FileVault.
- [object FDEFileVaultOptions](fdefilevaultoptions.md)
  The payload that configures FileVault options.
- [object FDERecoveryKeyEscrow](fderecoverykeyescrow.md)
  The payload that configures FileVault recovery key escrow.
### Login
- [object LoginItemsManagedItems](loginitemsmanageditems.md)
  The payload that configures a device’s login items.
- [object LoginWindowLoginItems](loginwindowloginitems.md)
  The payload that configures login behavior.
- [object LoginWindow](loginwindow.md)
  The payload that configures Login Window behavior.
- [object LoginWindowScripts](loginwindowscripts.md)
  The payload that configures scripts to run at login and logout.
- [object ServiceManagementManagedLoginItems](servicemanagementmanagedloginitems.md)
  This payload that configures managed login items, which auto-enables and auto-allows matched items.
### Mail
- [object ExchangeActiveSync](exchangeactivesync.md)
  The payload that configures Exchange ActiveSync accounts.
- [object ExchangeWebServices](exchangewebservices.md)
  The payload that configures an Exchange Web Services accounts.
- [object Mail](mail.md)
  The payload that configures a Mail account.
### Managed Devices
- [object EducationConfiguration](educationconfiguration.md)
  The payload that configures the users, groups, and departments within an educational organization.
- [object LightsOutManagementLOM](lightsoutmanagementlom.md)
  The payload that configures lights-out management (LOM) settings.
- [object ManagedPreferences](managedpreferences.md)
  The payload that configures managed preferences.
- [object MDM](mdm.md)
  The payload that configures mobile device management (MDM) settings.
- [object ProfileRemovalPassword](profileremovalpassword.md)
  The payload that configures profile removal.
### Media Management
- [object MediaManagementDiscBurning](mediamanagementdiscburning.md)
  The payload that configures disc-burning settings.
### Networking
- [object Cellular](cellular.md)
  The payload that configures cellular settings.
- [object CellularPrivateNetwork](cellularprivatenetwork.md)
  The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.
- [object ContentCaching](contentcaching.md)
  The payload that configures the Content Caching service.
- [object DNSSettings](dnssettings.md)
  The payload that configures encrypted DNS settings.
- [object Domains](domains.md)
  The payload that configures the domains under an organization’s management.
- [object Firewall](firewall.md)
  The payload that configures the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload that configures network-usage rules.
- [object Relay](relay.md)
  The payload that configures relay settings.
- [object WiFi](wifi.md)
  The payload that configures Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload that configures managed Wi-Fi settings.
### Parental Controls
- [object ParentalControlsApplicationRestrictions](parentalcontrolsapplicationrestrictions.md)
  The payload that configures parental controls for apps.
- [object ParentalControlsContentFilter](parentalcontrolscontentfilter.md)
  The payload that configures the parental control web content filters.
- [object ParentalControlsDictionary](parentalcontrolsdictionary.md)
  The payload that configures parental control dictionary restrictions.
- [object ParentalControlsGameCenter](parentalcontrolsgamecenter.md)
  The payload that configures Game Center parental controls.
- [object ParentalControlsTimeLimits](parentalcontrolstimelimits.md)
  The payload that configures parental control time limits.
### Preferences
- [object GlobalPreferences](globalpreferences.md)
  The payload to configure global preferences.
- [object UserPreferences](userpreferences.md)
  The payload that configures iCloud password preferences.
### Printing
- [object AirPrint](airprint.md)
  The payload that configures AirPrint printer discoverability in the user’s printer list.
- [object Printing](printing.md)
  The payload that configures printers.
### Privacy
- [object PrivacyPreferencesPolicyControl](privacypreferencespolicycontrol.md)
  The payload that configures privacy preferences.
### Proxies
- [object DNSProxy](dnsproxy.md)
  The payload that configures DNS proxies.
- [object GlobalHTTPProxy](globalhttpproxy.md)
  The payload that configures a global HTTP proxy.
- [object NetworkProxyConfiguration](networkproxyconfiguration.md)
  The payload that configures network proxies for a device.
### Restrictions
- [object Restrictions](restrictions.md)
  The payload that configures restrictions on a device.
### Security
- [object Passcode](passcode.md)
  The payload that configures a passcode policy.
- [object SecurityPreferences](securitypreferences.md)
  The payload that configures security preferences.
- [object SmartCard](smartcard.md)
  The payload that configures a smart card.
### System Configuration
- [object Declarations](declarations.md)
  The payload that applies a set of declarations to the device through the Settings app.
- [object EnergySaver](energysaver.md)
  The payload that configures Energy Saver settings.
- [object FileProvider](fileprovider.md)
  The payload that configures file provider settings.
- [object Font](font.md)
  The payload that configures fonts.
- [object LockScreenMessage](lockscreenmessage.md)
  The payload that configures a Lock Screen message.
- [object Screensaver](screensaver.md)
  The payload that configures the screen saver.
- [object SystemExtensions](systemextensions.md)
  The payload that configures system extensions.
- [object SystemLogging](systemlogging.md)
  The payload that configures system logging.
- [object TimeServer](timeserver.md)
  The payload that configures the time server.
### System Policy
- [object SystemPolicyControl](systempolicycontrol.md)
  The payload that configures the system policy for assessments.
- [object SystemPolicyKernelExtensions](systempolicykernelextensions.md)
  The payload that configures the kernel extension policies.
- [object SystemPolicyManaged](systempolicymanaged.md)
  The payload that configures the Finder’s contextual menu to bypass the system policy.
- [object SystemPolicyRule](systempolicyrule.md)
  The payload that configures the system policy.
### System Updates
- [object SoftwareUpdate](softwareupdate.md)
  The payload that configures the software update policy.
- [object SystemMigration](systemmigration.md)
  The payload that configures system migration.
### User Experience
- [object Accessibility](accessibility.md)
  The payload that configures the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload that configures the desktop wallpaper.
- [object Dock](dock.md)
  The payload that configures the Dock.
- [object Finder](finder.md)
  The payload that configures Finder settings.
- [object HomeScreenLayout](homescreenlayout.md)
  The payload that configures the Home Screen layout.
- [object ManagedMenuExtras](managedmenuextras.md)
  The payload that configures menu extras.
- [object Notifications](notifications.md)
  The payload that configures notifications.
- [object ScreensaverUser](screensaveruser.md)
  The payload that configures a user’s screen saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload that configures Setup Assistant settings.
- [object TimeMachine](timemachine.md)
  The payload that configures Time Machine.
### VPN
- [object AppLayerVPN](applayervpn.md)
  The payload that configures a per-app VPN.
- [object AppToAppLayerVPNMapping](apptoapplayervpnmapping.md)
  The payload that configures per-app VPN settings.
- [object VPN](vpn.md)
  The payload that configures a VPN.
### Web
- [object WebClip](webclip.md)
  The profile that configures web clips on the device.
- [object WebContentFilter](webcontentfilter.md)
  The payload that configures web content filters.
### Xsan
- [object Xsan](xsan.md)
  The payload that configures an Xsan client system.
- [object XsanPreferences](xsanpreferences.md)
  The payload that configures the Xsan preferences that define the volumes that automatically mount at startup.
### Deprecated
- [object AIMAccount](aimaccount.md)
  The payload that configures an AIM account on the device.
- [object APN](apn.md)
  The payload that configures access point names.
- [object FDERecoveryKeyRedirection](fderecoverykeyredirection.md)
  The payload that configures FileVault recovery key redirection.
- [object JabberAccount](jabberaccount.md)
  The payload that configures a Jabber account.
- [object MacOSServerAccount](macosserveraccount.md)
  The payload that configures a macOS Server account.
- [object MediaManagementAllowedMedia](mediamanagementallowedmedia.md)
  The payload that configures media management.
- [object ParentalControlsDashboardWidgetRestrictions](parentalcontrolsdashboardwidgetrestrictions.md)
  The payload that configures allowed dashboard widgets.
- [object ParentalControlDictationAndProfanity](parentalcontroldictationandprofanity.md)
  The payload that configures parental control for dictation and profanity.
- [object ShareKit](sharekit.md)
  The payload that configures ShareKit.
- [object SystemPreferences](systempreferences.md)
  The payload that configures the preference panes.

## See Also

- [Configuring Multiple Devices Using Profiles](configuring-multiple-devices-using-profiles.md)
  Create and deploy configuration profiles to users within your organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profile-specific-payload-keys)*