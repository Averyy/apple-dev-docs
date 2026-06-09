# Passcode

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a passcode policy.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- visionOS 2.0+
- watchOS 10.0+

## Declaration

```swift
object Passcode
```

#### Discussion

Specify `com.apple.mobiledevice.passwordpolicy` as the payload type.

The presence of this payload type causes the device to present the user with a passcode entry mechanism. The payload controls the complexity of the passcode.

For user enrollments, the system allows this payload type, but ignores most of the keys. Instead, the presence of the payload forces only these settings:

- `allowSimple`: always set to `false`
- `forcePIN`: always set to `true`
- `minLength`: always set to `6`
- `maxInactivity`: if this key is present its value is ignored, but the `never` option is removed in the Settings UI.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, visionOS, watchOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, visionOS, watchOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | iOS, visionOS |
| Allow multiple payloads | iOS, macOS, visionOS, watchOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>allowSimple</key>
            <true/>
            <key>forcePIN</key>
            <true/>
            <key>maxFailedAttempts</key>
            <integer>5</integer>
            <key>maxGracePeriod</key>
            <integer>1</integer>
            <key>maxInactivity</key>
            <integer>2</integer>
            <key>maxPINAgeInDays</key>
            <real>30</real>
            <key>minLength</key>
            <integer>8</integer>
            <key>pinHistory</key>
            <real>2</real>
            <key>requireAlphanumeric</key>
            <false/>
            <key>PayloadIdentifier</key>
            <string>com.example.mypasscodepayload</string>
            <key>PayloadType</key>
            <string>com.apple.mobiledevice.passwordpolicy</string>
            <key>PayloadUUID</key>
            <string>2a8a75e5-d17d-44d5-b062-3cb92161af9f</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Passcode</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>e044f50d-ff67-4bcd-9f3f-d7b678091061</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object Passcode.CustomRegex](passcode/customregex-data.dictionary.md)
  The regex defining the passcode policy.

## Properties

- `allowSimple` (boolean): If `false`, the system prevents use of a simple passcode. A simple passcode contains repeated characters, or increasing or decreasing characters, such as `123` or `CBA`.
- `changeAtNextAuth` (boolean): If `true`, the system causes a password reset to occur the next time the user tries to authenticate. If this key is set in a device profile, the setting takes effect for all users, and admin authentications may fail until the admin user password is also reset. Available: macOS 10.13+
- `customRegex` (Passcode.CustomRegex): Specifies a regular expression, and its description, used to enforce password compliance. Use the simpler passcode restrictions whenever possible, and rely on regular expression matching only when necessary. Mistakes in regular expressions can lead to frustrating user experiences, such as unsatisfiable passcode policies, or policy descriptions that don’t match the enforced policy. Available: macOS 14+
- `forcePIN` (boolean): If `true`, the system forces the user to enter a PIN.
- `maxFailedAttempts` (integer): The number of failed passcode attempts that the system allows the user before it erases or locks the device. After six failed attempts, the device imposes a time delay before the user can enter a passcode again. The time delay increases with each failed attempt. On macOS, set `minutesUntilFailedLoginReset` to define the time delay. The time delay begins after the sixth attempt, so if `MaximumFailedAttempts` is six or lower, the system has no time delay and triggers the erase or lock as soon as the user exceeds the limit. After the final failed attempt, the system locks a macOS device, or securely erases all data and settings from an iOS, visionOS, or watchOS device.
- `maxGracePeriod` (integer): The maximum grace period, in minutes, to unlock the phone without entering a passcode. The default is `0`, which is no grace period and requires a passcode immediately. On macOS, the system translates this grace period value to screen-saver settings.
- `maxInactivity` (integer): The maximum number of minutes for which the device can be idle without the user unlocking it, before the system locks it. When this limit is reached, the system locks the device and the passcode is required to unlock it. The user can edit this setting, but the value can’t exceed the `maxInactivity` value. On macOS, the system translates this inactivity value to screen-saver settings. The maximum value for macOS is `60`. Setting this key removes the `never` option in the Settings UI on user enrolled devices.
- `maxPINAgeInDays` (integer): The number of days for which the passcode can remain unchanged. After this number of days, the system forces the user to change the passcode before it unlocks the device.
- `minComplexChars` (integer): The minimum number of complex characters that a passcode needs to contain. A *complex* character is a character other than a number or a letter, such as `&`, `%`, `$`, and `#`. The system ignores this property for user enrollments. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | visionOS 2+
- `minLength` (integer): The minimum overall length of the passcode. This value is independent of the value for `minComplexChars`.
- `minutesUntilFailedLoginReset` (integer): The number of minutes before the system resets the login after the maximum number of unsuccessful login attempts is reached. This key requires setting `maxFailedAttempts`. Available: macOS 10.10+
- `pinHistory` (integer): This value defines *N*, where the new passcode must be unique within the last *N* entries in the passcode history.
- `requireAlphanumeric` (boolean): If `true`, the system requires alphabetic characters instead of only numeric characters. Available: iOS 4+ | iPadOS 4+ | macOS 10.7+ | visionOS 2+

## See Also

- [object SecurityPreferences](securitypreferences.md)
  The payload that configures security preferences.
- [object SmartCard](smartcard.md)
  The payload that configures a smart card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/passcode)*