# iOS(_:)

**Framework**: PackageDescription  
**Kind**: method

Configures the minimum deployment target version for the iOS platform using a custom version string.

## Declaration

```swift
static func iOS(_ versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

The version string must be a series of two or three dot-separated integers, such as `8.0` or `8.0.1`.

> **Note**: First available in PackageDescription 5.0

## Parameters

- `versionString`: The minimum deployment target as a string   representation of two or three dot-separated integers, such as  .

## See Also

- [static func iOS(SupportedPlatform.IOSVersion) -> SupportedPlatform](supportedplatform/ios(_:)-5pvv5.md)
  Configures the minimum deployment target version for the iOS platform.
- [static let iOS: Platform](platform/ios.md)
  The iOS platform.
- [SupportedPlatform.IOSVersion](supportedplatform/iosversion.md)
  The supported iOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/ios(_:)-83bbf)*