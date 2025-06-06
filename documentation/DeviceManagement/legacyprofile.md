# LegacyProfile

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a legacy profile.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object LegacyProfile
```

#### Discussion

Specify `com.apple.configuration.legacy` as the declaration type.

This declaration specifies an MDM 1 profile for the device to download and install.

The declaration may contain any profile that MDM supports. The system doesn’t allow MDM enrollment and Profile Services profiles.

##### Configuration Availability

| Allowed in Device Enrollment | iOS, macOS, tvOS, watchOS |
| --- | --- |
| Allowed in User Enrollment | iOS, macOS |
| Allowed in Local Enrollment | iOS, macOS, tvOS, watchOS |
| Allowed in System Scope | iOS, macOS, Shared iPad, tvOS, watchOS |
| Allowed in User Scope | macOS, Shared iPad |

## See Also

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
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive, legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test the MDM system.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.
- [object PasscodeSettings](passcodesettings.md)
  The declaration to configure passcode policy settings.
- [object SafariExtensionSettings](safariextensionsettings.md)
  The declaration to configure Safari Extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/legacyprofile)*