# PasscodeSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure passcode policy settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- visionOS 2.0+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object PasscodeSettings
```

#### Discussion

Specify `com.apple.configuration.passcode.settings` as the declaration type.

##### Configuration Availability

| Allowed in Device Enrollment | iOS, macOS, watchOS |
| --- | --- |
| Allowed in User Enrollment | iOS |
| Allowed in Local Enrollment | iOS, macOS, watchOS |
| Allowed in System Scope | iOS, macOS, watchOS |
| Allowed in User Scope | macOS |

## Topics

### Supporting Objects
- [object PasscodeSettingsCustomRegexObject](passcodesettingscustomregexobject.md)
  A regular expression and its description to enforce password compliance.
- [object PasscodeSettingsCustomRegex_DescriptionObject](passcodesettingscustomregex_descriptionobject.md)
  A dictionary that contains supported OS language IDs for the keys and values that represent a localized description of the policy that the regular expression enforces.

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
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test the MDM system.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.
- [object SafariExtensionSettings](safariextensionsettings.md)
  The declaration to configure Safari Extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passcodesettings)*