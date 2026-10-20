# Device.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a Devices resource.

**Availability**:
- App Store Connect API 1.1+

## Declaration

```
object Device.Attributes
```

## Mentions

- [App Store Connect API 4.0 release notes](../app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.1 release notes](../app-store-connect-api-4-1-release-notes.md)

## Properties

- `deviceClass` (string): **Allowed Values**: `APPLE_VISION_PRO`, `APPLE_WATCH`, `IPAD`, `IPHONE`, `IPOD`, `APPLE_TV`, `MAC`
- `model` (string)
- `name` (string)
- `platform` (BundleIdPlatform)
- `status` (string): **Allowed Values**: `ENABLED`, `DISABLED`
- `udid` (string)
- `addedDate` (date-time)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/device/attributes-data.dictionary)*