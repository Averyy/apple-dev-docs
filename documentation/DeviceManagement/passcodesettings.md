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

## Declaration

```swift
object PasscodeSettings
```

#### Discussion

Specify `com.apple.configuration.passcode.settings` as the declaration type.

The presence of this configuration type causes the device to present the user with a passcode entry mechanism. The configuration controls the complexity of the passcode.

For user enrollments, the system allows this configuration type, but ignores most of the keys. Instead, the presence of the configuration forces only these settings:

- `RequirePasscode`: always set to `true`
- `RequireComplexPasscode`: always set to `true`
- `MinimumLength`: always set to `6`
- `MaximumInactivityInMinutes`: if this key is present its value is ignored, but the `never` option is removed in the Settings UI.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS, watchOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | iOS, Shared iPad, visionOS |
| Allowed in local enrollment | iOS, macOS, Shared iPad, visionOS, watchOS |
| Allowed in system scope | iOS, macOS, visionOS, watchOS |
| Allowed in user scope | macOS |

##### Configuration Examples

## Topics

### Objects
- [object PasscodeSettingsCustomRegexObject](passcodesettingscustomregexobject.md)
  A regular expression and its description to enforce password compliance.

## See Also

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
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object LegacyInteractiveProfile](legacyinteractiveprofile.md)
  The declaration to configure an interactive legacy profile.
- [object LegacyProfile](legacyprofile.md)
  The declaration to configure a legacy profile.
- [object ManagementStatusSubscriptions](managementstatussubscriptions.md)
  The declaration to configure status subscriptions.
- [object ManagementTest](managementtest.md)
  The declaration to test declarative device management.
- [object MathSettings](mathsettings.md)
  The declaration to configure the math and calculator apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passcodesettings)*