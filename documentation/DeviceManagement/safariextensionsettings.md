# SafariExtensionSettings

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure Safari Extensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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
| Allowed in device enrollment | N/A |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | N/A |
| Allowed in system scope | iOS, visionOS |
| Allowed in user scope | macOS, Shared iPad |
| Apply | Multiple configurations are combined and applied as a single effective configuration |

##### Configuration Examples

**Disallow all**:

This configuration disables all Safari extensions.

```json
{
    "Type": "com.apple.configuration.safari.extensions.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManagedExtensions": {
            "*": {
                "State": "AlwaysOff"
            }
        }
    }
}
```

**Allow one**:

This configuration disables all Safari extensions, except for one that it requires.

```json
{
    "Type": "com.apple.configuration.safari.extensions.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManagedExtensions": {
            "*": {
                "State": "AlwaysOff"
            },
            "com.example.WebExtension (ABCDE12345)": {
                "State": "AlwaysOn"
            }
        }
    }
}
```

**Disallow private browsing**:

This configuration allows all Safari extensions, but one isn’t allowed in private browsing.

```json
{
    "Type": "com.apple.configuration.safari.extensions.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManagedExtensions": {
            "com.example.WebExtension (ABCDE12345)": {
                "State": "AlwaysOn",
                "PrivateBrowsing": "AlwaysOff"
            }
        }
    }
}
```

**Disallow domain**:

This configuration allows all Safari extensions, but one isn’t allowed for use with a domain and its sub-domains.

```json
{
    "Type": "com.apple.configuration.safari.extensions.settings",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "ManagedExtensions": {
            "com.example.WebExtension (ABCDE12345)": {
                "DeniedDomains": [
                    "*example.org"
                ]
            }
        }
    }
}
```

## Topics

### Objects
- [object SafariExtensionSettingsManagedExtensionsObject](safariextensionsettingsmanagedextensionsobject.md)
  The dictionary of managed extensions settings. Each key in the dictionary represents a composed identifier for a specific managed extension, or you can specify a single “*” character to match any extension. The dictionary values represent the settings that Safari applies to each extension that matches the key. In order for the extension to be managed, its host app needs to be present on the device.

## Properties

- `ManagedExtensions` (SafariExtensionSettingsManagedExtensionsObject): The dictionary of managed extensions settings. Each key in the dictionary represents a composed identifier for a specific managed extension, or you can specify a single “*” character to match any extension. The dictionary values represent the settings that Safari applies to each extension that matches the key. In order for the extension to be managed, its host app needs to be present on the device. The composed identifier of a managed extension uses the format “Identifier (TeamIdentifier)”, for example “com.example.app (ABCD1234)”. Use `codesign -dv <path_to_appex>` to show the information you need to generate this string on macOS, using the path to the extension bundle located in the “PlugIns” folder inside the app bundle. For other platforms, request this information from the app developer.

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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safariextensionsettings)*