# AppSettingsPrivacy_PermissionDefaultsObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary of app privacy permission defaults. Each key in the dictionary is an app identifier. The dictionary values represent the permission defaults that the device applies for each matching app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
object AppSettingsPrivacy_PermissionDefaultsObject
```

#### Discussion

In iOS, the app identifier is a bundle ID, for example, “com.example.app”.

In macOS, the app identifier is a composed identifier. The format of the composed identifier is either “Bundle-ID”, “Bundle-ID (Team-ID)”, or “Bundle-ID {Designated-Requirement}”. “Bundle-ID” is the bundle identifier string of the app. “Team-ID” is the team identifier from the app’s code signature. “Designated-Requirement” is the designated requirement string from the code signature of the app. For example, “com.example.app” for the bundle ID format, “com.example.app (ABCD1234)” for the team ID format, or “com.example.app {anchor apple generic}” for the designated requirement format. The device only applies defaults for an app if its code signature matches the composed identifier.

## Topics

### Objects
- [object AppSettingsAppDictionaryObject](appsettingsappdictionaryobject.md)
  The dictionary that defines the app privacy permission defaults. Each key is an app identifier.

## Properties

- `ANY` (AppSettingsAppDictionaryObject): The dictionary that defines the app privacy permission defaults. Each key is an app identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appsettingsprivacy_permissiondefaultsobject)*