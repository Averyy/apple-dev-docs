# iOS(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Configures the minimum deployment target version for the iOS platform using a custom version string.

## Declaration

```swift
static func iOS(_ versionString: String) -> SupportedPlatform
```

## Return Value

A `SupportedPlatform` instance.

## Discussion

The version string must be a series of two or three dot-separated integers, such as `8.0` or `8.0.1`.

> **Since**: First available in PackageDescription 5.0

## Parameters

- `versionString`: The minimum deployment target as a string representation of two or three dot-separated integers, such as `8.0.1`.

## See Also

### Supporting iOS
- [static func iOS(SupportedPlatform.IOSVersion) -> SupportedPlatform](./ios%28_%29-5pvv5.md)
  Configures the minimum deployment target version for the iOS platform.
- [static let iOS: Platform](../platform/ios.md)
  The iOS platform.
- [SupportedPlatform.IOSVersion](./iosversion.md)
  The supported iOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/ios(_:)-83bbf)*