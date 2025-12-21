# SafariExtensionSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Safari Extensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 26.0+

## Declaration

```swift
object SafariExtensionSettings
```

#### Discussion

Specify `com.apple.configuration.safari.extensions.settings` as the declaration type.

Safari supports the following values for `AllowedDomains` and `DeniedDomains`:

- A specific domain such as “example.com” or “www.example.com”.
- A wildcard domain that uses a single “*” character as a prefix for the domain, such as “*example.com”. This matches both the exact domain “example.com”, and any sub-domains such as “www.example.com”. It won’t match other domains with a similar string suffix such as “myexample.com”.
- A global wildcard specified as a single “*” character that matches any domain.

Safari determines whether a domain is allowed or denied using the following precedence rules:

1. A specific domain takes precedence over the global wildcard or a wildcard domain.
2. A wildcard domain takes precedence over the global wildcard.

If the same value appears in both `AllowedDomains` and `DeniedDomains`, Safari denies use of a matching domain.

The user can configure any domains not matched by the values in `AllowedDomains` or `DeniedDomains`.

##### Examples

Give an extension access to only “example.com” and its sub-domains, and deny access to everywhere else.

```json
"AllowedDomains": ["*example.com"],
"DeniedDomains": ["*"]
```

Give an extension access to “example.com” and its sub-domains, without deny anywhere else. The user can make their own choice for other domains.

```json
"AllowedDomains": ["*example.com"]
```

Give an extension access to “example.com” and its sub-domains, but deny access to “private.example.com” or anywhere else.

```json
"AllowedDomains": ["*example.com"],
"DeniedDomains": ["private.example.com", "*"]
```

Give an extension access to “public.example.com”, but deny access to “example.com” or any other of its sub-domains. The user can make their own choice for other domains.

```json
"AllowedDomains": ["public.example.com"],
"DeniedDomains": ["*example.com"]
```

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | NA |
| Allowed in user enrollment | NA |
| Allowed in local enrollment | NA |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |

##### Configuration Examples

## Topics

### Objects
- [object SafariExtensionSettingsManagedExtensionsObject](safariextensionsettingsmanagedextensionsobject.md)
  The dictionary that defines the managed extension.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safariextensionsettings)*