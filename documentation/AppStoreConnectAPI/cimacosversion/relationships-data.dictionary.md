# CiMacOsVersion.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the macOS Versions resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiMacOsVersion.Relationships
```

## Topics

### Objects
- [object CiMacOsVersion.Relationships.XcodeVersions](./relationships-data.dictionary/xcodeversions-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the macOS Versions and Xcode Versions resources.

## Properties

- `xcodeVersions` (CiMacOsVersion.Relationships.XcodeVersions): The macOS version’s related Xcode version.

## See Also

### Objects
- [object CiMacOsVersion.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a macOS Versions resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cimacosversion/relationships-data.dictionary)*