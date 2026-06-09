# SafariSettingsPrivacy_PermissionDefaultsObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary of website permission defaults. Each key in the dictionary represents a single website, or a website and its sub-domains. The dictionary values represent the permission defaults that Safari applies for each website that matches the key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
object SafariSettingsPrivacy_PermissionDefaultsObject
```

#### Discussion

Safari supports the following patterns for the website key:

- A specific domain such as “example.com” or “www.example.com”. The permission defaults apply to that website only.
- A wildcard domain that uses a single “*” character as a prefix for the domain, such as “*example.com”. The permission defaults apply to both the exact domain “example.com”, and any sub-domains such as “www.example.com”. It won’t match other domains with a similar string suffix such as “myexample.com”.

When multiple patterns match a website, Safari uses the most precise pattern. For example, for the website “www.example.com”, if rules “www.example.com” and “*example.com” match, Safari uses the former.

## Topics

### Objects
- [object SafariSettingsWebsiteDictionaryObject](safarisettingswebsitedictionaryobject.md)
  The dictionary that defines the website privacy permission defaults. Each key represents a website.

## Properties

- `ANY` (SafariSettingsWebsiteDictionaryObject): The dictionary that defines the website privacy permission defaults. Each key represents a website.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safarisettingsprivacy_permissiondefaultsobject)*