# ExtensibleSingleSignOnKerberos.ExtensionData

**Framework**: Device Management  
**Kind**: dictionary

The additional data to pass to the app extension.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.1+

## Declaration

```swift
object ExtensibleSingleSignOnKerberos.ExtensionData
```

## Topics

### Objects
- [object ExtensibleSingleSignOnKerberos.ExtensionData.DomainRealmMapping](extensiblesinglesignonkerberos/extensiondata-data.dictionary/domainrealmmapping-data.dictionary.md)
  The mapping of realms to their DNS suffixes.

## Properties

- `allowAutomaticLogin` (boolean): If `false`, the system doesn’t allow saving passwords in the keychain.
- `allowPassword` (boolean): If `true`, allow the user to switch the user interface to Password mode. Available: macOS 15+
- `allowPasswordChange` (boolean): If `false`, the system disables password changes. Available: macOS 10.15+
- `allowPlatformSSOAuthFallback` (boolean): If `true` and `usePlatformSSOTGT` is `true`, the system allows the user to manually sign in. Available: macOS 13+
- `allowSmartCard` (boolean): If `true`, allow the user to switch the user interface to SmartCard mode. Available: macOS 15+
- `cacheName` (string): The GSS name of the Kerberos cache to use. Rarely set by an administrator. Deprecated: iOS 15+ | iPadOS 15+ | macOS 12+
- `certificateUUID` (string): The PayloadUUID of a PKINIT certificate.
- `credentialBundleIdACL` ([string]): A list of bundle IDs allowed to access the ticket-granting ticket (TGT).
- `credentialUseMode` (string): This setting affects how other processes use the Kerberos Extension credential. Allowed values: - `always`: The system always uses the credential if the SPN matches the Kerberos Extension `Hosts` array and the caller hasn’t specified another credential. However, the system won’t use the credential if the calling app isn’t in the `credentialBundleIDACL`.
- `whenNotSpecified`: The system only uses the extension credential if the SPN matches the Kerberos Extension `Hosts` array. However, the system won’t use the credential if the calling app isn’t in the `credentialBundleIDACL`.
- `kerberosDefault`: The system uses the default Kerberos processes to select credentials, and normally uses the default Kerberos credential. This is the same as turning off this capability. Available: iOS 14+ | iPadOS 14+ | macOS 11+ | visionOS 1.1+
- `customUsernameLabel` (string): The custom user name label used in the Kerberos extension instead of “Username,” such as “Company ID”. Available: iOS 14+ | iPadOS 14+ | macOS 11+ | visionOS 1.1+
- `delayUserSetup` (boolean): If `true`, the system doesn’t prompt the user to setup the Kerberos extension until either the administrator enables it with the `app-sso` tool or the system receives a Kerberos challenge. Available: macOS 11+
- `domainRealmMapping` (ExtensibleSingleSignOnKerberos.ExtensionData.DomainRealmMapping): A custom domain-realm mapping for Kerberos. The system uses this when the DNS name of hosts doesn’t match the realm name. Most administrators don’t need to customize this.
- `helpText` (string): The text to display to the user at the bottom of the Kerberos Login Window. You can also use this to display help information or disclaimer text. Available: iOS 14+ | iPadOS 14+ | macOS 11+ | visionOS 1.1+
- `identityIssuerAutoSelectFilter` (string): A string with wildcards that can use used to filter the list of available SmartCards by issuer. e.g “*My CA2*”. If there is one remaining, it will be auto-selected. If there more than one remaining, then the list is shorter. Available: macOS 15+
- `includeKerberosAppsInBundleIdACL` (boolean): If `true`, the Kerberos extension allows the standard Kerberos utilities including `TicketViewer` and `klist` to access and use the credential. This is in addition to `includeManagedAppsInBundleIdACL` or the `credentialBundleIdACL`, if you specify those values. Available: macOS 12+
- `includeManagedAppsInBundleIdACL` (boolean): If `true`, the Kerberos extension allows only managed apps to access and use the credential. This is in addition to the `credentialBundleIDACL`, if you specify that value. Available: iOS 14+ | iPadOS 14+ | macOS 12+ | visionOS 1.1+
- `isDefaultRealm` (boolean): Specifies whether this is the default realm if there’s more than one Kerberos extension configuration.
- `monitorCredentialsCache` (boolean): If `false`, the system requests the credential on the next matching Kerberos challenge or network state change. If the credential is expired or missing, the system creates a new one. Available: macOS 11+
- `performKerberosOnly` (boolean): If `true`, the Kerberos Extension handles Kerberos requests only. It doesn’t check for password expiration, show the password expiration in the menu, check for external password changes, perform password sync, or retrieve the home directory. Available: iOS 16+ | iPadOS 16+ | macOS 13+ | visionOS 1.1+
- `preferredKDCs` ([string]): The ordered list of preferred Key Distribution Centers (KDCs) to use for Kerberos traffic. Use this if the servers aren’t discoverable through DNS. If you specify the servers, the system uses them for both connectivity checks and attempts to use them first for Kerberos traffic. If the servers don’t respond, the device falls back to DNS discovery. Format each entry the same as it would be in a `krb5.conf` file, for example: - `adserver1.example.com`
- `tcp/adserver1.example.com:88`
- `kkdcp://kerberosproxy.example.com:443/kkdcp` Available: iOS 15+ | iPadOS 15+ | macOS 12+ | visionOS 1.1+
- `principalName` (string): The principal (username) to use. You don’t need to include the realm.
- `pwChangeURL` (string): This URL will launch in the user’s default web browser when they initiate a password change. Available: macOS 10.15+
- `pwExpireOverride` (integer): The number of days that the system allows using passwords on this domain. For most domains, this calculation is automatic. Available: macOS 10.15+
Deprecated: macOS 12+
- `pwNotificationDays` (integer): The number of days prior to password expiration when the system sends a notification of password expiration to the user. Available: macOS 10.15+
- `pwReqComplexity` (boolean): If `true`, the system requires passwords to meet Active Directory’s definition of “complex”. Available: macOS 10.15+
- `pwReqHistory` (integer): The number of prior passwords that the system disallows reuse on this domain. Available: macOS 10.15+
- `pwReqLength` (integer): The minimum length of passwords on the domain. Available: macOS 10.15+
- `pwReqMinAge` (integer): The minimum age of passwords before the system allows changing them on this domain. Available: macOS 10.15+
- `pwReqRTFData` (data): The RTF file formatted version of the domain’s password requirements. Only for use if `pwReqComplexity` or `pwReqLength` aren’t specified. Available: macOS 15+
- `pwReqText` (string): The text version of the domain’s password requirements. Only for use if `pwReqComplexity` or `pwReqLength` aren’t specified. Available: macOS 10.15+
- `replicationTime` (integer): The time, in seconds, required to replicate changes in the Active Directory domain. The Kerberos extension uses this when checking password age after a change. Available: macOS 11+
Deprecated: macOS 12+
- `requireTLSForLDAP` (boolean): Require that LDAP connections use TLS. Available: iOS 14+ | iPadOS 14+ | macOS 11+ | visionOS 1.1+
- `requireUserPresence` (boolean): If `true`, the system requires the user to provide Touch ID, Face ID or their passcode to access the keychain entry.
- `siteCode` (string): The name of the Active Directory site the Kerberos extension should use. Most administrators don’t need to modify this value, as the Kerberos extension can normally find the site automatically.
- `startInSmartCardMode` (boolean): If `true`, the user interface will start in SmartCard mode. Available: macOS 15+
- `syncLocalPassword` (boolean): If `false`, the system disables password sync. Note that this will not work if the user is logged in with a mobile account. Available: macOS 10.15+
- `usePlatformSSOTGT` (boolean): If `true`, the system requires this configuration uses a TGT from Platform SSO instead of requesting a new one. Available: macOS 13+
- `useSiteAutoDiscovery` (boolean): If `false`, the Kerberos extension doesn’t automatically use LDAP and DNS to determine its AD site name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblesinglesignonkerberos/extensiondata-data.dictionary)*