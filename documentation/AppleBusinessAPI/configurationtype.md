# ConfigurationType

**Framework**: AppleBusinessAPI  
**Kind**: typealias  
**Role**: Type

The type of Configuration profile.

**Availability**:
- Apple Business API 2.6+

## Declaration

```
string ConfigurationType
```

## Possible Values

- `AIR_DROP`
- `AIR_PRINT`
- `APP_ACCESS`
- `APPLE_INTELLIGENCE_SIRI`
- `APPLICATION_LAYER_FIREWALL`
- `AUTHENTICATION_SCREEN_LOCK`
- `CERTIFICATE`
- `CONFERENCE_ROOM_DISPLAY`
- `CONTENT_CACHING`
- `CUSTOM_PROFILE`
- `CUSTOM_SETTING`
- `DATA_MANAGEMENT`
- `ENERGY_SAVER`
- `FILE_VAULT`
- `GATE_KEEPER`
- `ICLOUD`
- `LOGIN_WINDOW`
- `MEDIA_MANAGEMENT`
- `SOFTWARE_UPDATE`
- `VPN`
- `WEB_CLIP`
- `WEB_FILTER`
- `WIFI`

#### Possible Values

- `CUSTOM_SETTING` - A custom Configuration profile (can be created/updated via API)
- `AIR_DROP` - AirDrop settings
- `AIR_PRINT` - AirPrint settings
- `APP_ACCESS` - App access restrictions
- `APPLE_INTELLIGENCE_SIRI` - Apple Intelligence and Siri settings
- `APPLICATION_LAYER_FIREWALL` - Application layer firewall settings
- `AUTHENTICATION_SCREEN_LOCK` - Authentication and screen lock settings
- `CERTIFICATE` - Certificate management
- `CONFERENCE_ROOM_DISPLAY` - Conference room display settings
- `CONTENT_CACHING` - Content caching settings
- `CUSTOM_PROFILE` - Custom profile
- `DATA_MANAGEMENT` - Data management settings
- `ENERGY_SAVER` - Energy saver settings
- `FILE_VAULT` - FileVault encryption settings
- `GATE_KEEPER` - Gatekeeper settings
- `ICLOUD` - iCloud settings
- `LOGIN_WINDOW` - Login window settings
- `MEDIA_MANAGEMENT` - Media management settings
- `SOFTWARE_UPDATE` - Software update settings
- `VPN` - VPN settings
- `WEB_CLIP` - Web clip settings
- `WEB_FILTER` - Web filter settings
- `WIFI` - Wi-Fi configuration

> **Note**: Only `CUSTOM_SETTING` type Configuration can be created or updated via the API. All other types are read-only.

## See Also

### Type Aliases
- [type OrgDeviceActivityType](./orgdeviceactivitytype.md)
  Strings that represent organization device activities.
- [type AppleCareCoveragePaymentType](./applecarecoveragepaymenttype.md)
  Strings that represent AppleCare coverage payment types.
- [type AppleCareCoverageStatus](./applecarecoveragestatus.md)
  Strings that represent AppleCare coverage status.
- [type UserStatus](./userstatus.md)
  Strings that represent user statuses.
- [type UserPhoneNumberType](./userphonenumbertype.md)
  Strings that represent phone number types.
- [type UserGroupStatus](./usergroupstatus.md)
  Strings that represent user group statuses.
- [type UserGroupType](./usergrouptype.md)
  Strings that represent user group types.
- [type SupportedOS](./supportedos.md)
  The supported operating systems for an app.
- [type BlueprintStatus](./blueprintstatus.md)
  The status of a Blueprint.
- [type ConfigurationPlatform](./configurationplatform.md)
  The platform that a Configuration targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/configurationtype)*