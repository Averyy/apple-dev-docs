# PasscodeSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure passcode policy settings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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
| Allowed in supervised enrollment | iOS, macOS, visionOS, watchOS |
| Allowed in device enrollment | iOS, visionOS |
| Allowed in user enrollment | iOS, visionOS |
| Allowed in local enrollment | iOS, macOS, visionOS, watchOS |
| Allowed in system scope | iOS, macOS, visionOS, watchOS |
| Allowed in user scope | macOS |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Examples

**Complex**:

This configuration applies a complex passcode policy.

```json
{
    "Type": "com.apple.configuration.passcode.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "RequirePasscode": true,
        "RequireComplexPasscode": true,
        "MinimumLength": 10,
        "MaximumInactivityInMinutes": 1
    }
}
```

**Regular expression**:

This configuration applies a passcode policy using a regular expression.

```json
{
    "Type": "com.apple.configuration.passcode.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "CustomRegex": {
            "Regex": "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$",
            "Description": {
                "default": "Default: Minimum 8 characters, 1 number, 1 uppercase, 1 lowercase.",
                "en-US": "Minimum 8 characters, 1 number, 1 uppercase, 1 lowercase.",
                "fr": "Minimum 8 caractères, 1 chiffre, 1 majuscule, 1 minuscule."
            }
        }
    }
}
```

## Topics

### Objects
- [object PasscodeSettingsCustomRegexObject](passcodesettingscustomregexobject.md)
  Specifies a regular expression, and its description, to enforce password compliance. Use the simpler passcode settings whenever possible, and rely on regular expression matching only when necessary. Mistakes in regular expressions can lead to frustrating user experiences, such as unsatisfiable passcode policies, or policy descriptions that don’t match the enforced policy.

## Properties

- `ChangeAtNextAuth` (boolean): If `true`, the system forces a password reset the next time the user tries to authenticate. If you set this key in a configuration in the system scope (device channel), the setting takes effect for all users, and admin authentication may fail until the admin user password is also reset. Available: macOS 13.1+
- `CustomRegex` (PasscodeSettingsCustomRegexObject): Specifies a regular expression, and its description, to enforce password compliance. Use the simpler passcode settings whenever possible, and rely on regular expression matching only when necessary. Mistakes in regular expressions can lead to frustrating user experiences, such as unsatisfiable passcode policies, or policy descriptions that don’t match the enforced policy. Available: macOS 14+
- `FailedAttemptsResetInMinutes` (integer): The number of minutes before the login is reset after the maximum number of failed attempts. Also set the `MaximumFailedAttempts` key for this to take effect. Available: macOS 13.1+
- `MaximumFailedAttempts` (integer): The number of failed passcode attempts that the system allows the user before it erases or locks the device. After six failed attempts, the device imposes a time delay before the user can enter a passcode again. The time delay increases with each failed attempt. On macOS, set `FailedAttemptsResetInMinutes` to define the time delay. The time delay begins after the sixth attempt, so if `MaximumFailedAttempts` is six or lower, the system has no time delay and triggers the erase or lock as soon as the user exceeds the limit. After the final failed attempt, the system locks a macOS device, or securely erases all data and settings from an iOS, visionOS, or watchOS device.
- `MaximumGracePeriodInMinutes` (integer): The maximum period that a user can select, during which the user can unlock the device without a passcode. A value of `0` means no grace period, and the device requires a passcode immediately. In the absence of this key, the user can select any period. In macOS, the system translates this to screensaver settings.
- `MaximumInactivityInMinutes` (integer): The maximum period that a user can select, during which the device can be idle before the system automatically locks it. When the device reaches this limit, the device locks and the user must enter the passcode to unlock it. In the absence of this key, the user can select any period. In macOS, the system translates this to screensaver settings.
- `MaximumPasscodeAgeInDays` (integer): Specifies the maximum number of days that the passcode can remain unchanged. After this number of days, the system forces the user to change the passcode before it unlocks the device. Available: iOS 16.2+ | iPadOS 16.2+ | macOS 13.1+ | visionOS 2+ | watchOS 10+
- `MinimumComplexCharacters` (integer): Specifies the minimum number of complex characters in the password. A complex character is a character other than a number or a letter, such as `&`, `%`, `$`, and `#`. Available: iOS 16.2+ | iPadOS 16.2+ | macOS 13.1+ | visionOS 2+
- `MinimumLength` (integer): The minimum number of characters a passcode can contain.
- `PasscodeReuseLimit` (integer): The number of historical passcode entries the system checks when validating a new passcode. The device refuses a new passcode if it matches a previously used passcode within the specified passcode history range. In the absence of this key, the system performs no historical check.
- `RequireAlphanumericPasscode` (boolean): If `true`, the passcode needs to consist of at least one alphabetic character and at least one number. Available: iOS 16.2+ | iPadOS 16.2+ | macOS 13.1+ | visionOS 2+
- `RequireComplexPasscode` (boolean): If `true`, the system requires a complex passcode. A complex passcode is one that doesn’t contain repeated characters or increasing or decreasing characters (such as 123 or CBA).
- `RequirePasscode` (boolean): If `true`, the system requires the user to set a passcode without any requirements about the length or quality of the passcode. The presence of any other keys implicitly requires a passcode, and overrides this key’s value.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passcodesettings)*