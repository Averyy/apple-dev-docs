# Profile

**Framework**: Device Management  
**Kind**: dictionary

A profile’s properties and their values.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object Profile
```

## Mentions

- [Migrating managed devices](migrating-managed-devices.md)
- [Returning a managed device to service](returning-a-managed-device-to-service.md)
- [Authenticating Through Web Views](authenticating-through-web-views.md)
- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)
- [Implementing Platform SSO during device enrollment](implementing-platform-sso-during-device-enrollment.md)

## Topics

### Skip Keys
- [object SkipKeys](skipkeys.md)
  The list of skip keys for setup panes.

## Properties

- `allow_pairing` (boolean): Default is `true`. In iOS 13, this property was deprecated.
- `anchor_certs` ([string]): An array of strings, where each string is a DER-encoded (Distinguished Encoding Rules) certificate converted to Base64 encoding. If provided, the device uses these certificates as trusted anchor certificates when evaluating the trust of the connection to the MDM server URL. Otherwise, the device uses the built-in root certificates.
- `auto_advance_setup` (boolean): If set to `true`, the device will tell Setup Assistant to automatically advance though its screens. Default is `false`. This key is valid in X-Server-Protocol-Version 2 and later. Available on tvOS and macOS 11 and later.
- `await_device_configured` (boolean): If `true`, the device will not continue in Setup Assistant until the MDM server sends a command that states the device is configured (see [`Device Configured`](device-configured-command.md)). Default is `false`. Ignored on iOS devices if `is_supervised` is `false`. This key is valid in X-Server-Protocol-Version 2 and later.
- `configuration_web_url` (string): The URL that the clients load into a web view during setup. This site provides the appropriate UI to authenticate the user, and when satisfied, initiates the download of the MDM enrollment profile. To provide the MDM enrollment profile, the web view looks for a page with MIME type `application/x-apple-aspen-config`. While the user is allowed to navigate to any site or host during authentication, the MDM enrollment profile must originate from the same host as specified in this field.
- `department` (string): The user-defined department or location name.
- `devices` ([string]): Array of strings that contains device serial numbers (may be empty).
- `do_not_use_profile_from_backup` (boolean): If `true`, the device does not use the profile when it restores a backup. Default is `false`. Available in iOS 26 and later, and visionOS 26 and later; otherwise ignored by devices.
- `is_return_to_service` (boolean): If `true`, the device is configured for Rapid Return to Service. Default is `false`. Available in iOS 26 and later, and visionOS 26 and later; otherwise ignored by devices.
- `is_mandatory` (boolean): If `true`, the user may not skip applying the profile returned by the MDM server. Default is `false`. In iOS 13 and later, all DEP enrollments are mandatory.
- `is_mdm_removable` (boolean): If `false`, the MDM payload delivered by the configuration URL cannot be removed by the user via the user interface on the device; that is, the MDM payload is locked onto the device. This key can be set to `false` only if `is_supervised` is set to `true`. Defaults to `true`.
- `is_multi_user` (boolean): If `true`, tells the device to configure for Shared iPad. Default is false. This key is valid only for Apple School Manager or Apple Business organizations using X-Server-Protocol-Version 2 and later. Devices that do not meet the Shared iPad minimum requirements do not honor this command. With iOS devices, `com.apple.mdm.per-user-connections` must be added to the MDM enrollment profile’s Server Capabilities.
- `is_supervised` (boolean): If `true`, the device must be supervised. Defaults to `false`. In iOS 11, DEP devices that are not supervised have been deprecated. In iOS 13, all DEP devices will be supervised and the OS will ignore the `is_supervised` flag completely.
- `language` (string): A language designator is a code that represents a language. Use the two-letter ISO 639-1 standard (preferred) or the three-letter ISO 639-2 standard. If an ISO 639-1 code is not available for a particular language, use the ISO 639-2 code instead. See [`Language and Locale IDs`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) for more information. Example two-letter: `en`, `fr`, `ja` Example three-letter: `eng`, `fre`, `jpn`, `haw` Available on tvOS and macOS 11 and later.``
- `org_magic` (string): A string that uniquely identifies various services that are managed by a single organization.
- `profile_name` (string): A human-readable name for the profile.
- `region` (string): A region designator is a code that represents a country. Available on tvOS and macOS 11 and later. Use the ISO 3166-1 standard, a two-letter, capitalized code. Examples: US, GB, AU
- `skip_setup_items` ([string]): A list of setup panes to skip. The list of valid strings is defined in [`SkipKeys`](skipkeys.md).
- `supervising_host_certs` ([string]): Each string contains a DER-encoded certificate converted to Base64 encoding. If provided, the device will continue to pair with a host that possesses one of these certificates even when `allow_pairing` is set to `false`. If `is_supervised` is `false`, this list is unused.
- `support_email_address` (string): A support email address for the organization. This key is valid in X-Server-Protocol-Version 2 and later.
- `support_phone_number` (string): A support phone number for the organization.
- `url` (string): String. The URL of the MDM server.

## See Also

- [object Device](device.md)
  A device’s properties and their values.
- [object MachineInfo](machineinfo.md)
  A device’s information in response to a MDM enrollment profile request.
- [object Limit](limit.md)
  A ranged limit.
- [object Url](url.md)
  A URL object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profile)*