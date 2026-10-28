# iOS(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Configures the minimum deployment target version for the iOS platform.

## Declaration

```swift
static func iOS(_ version: SupportedPlatform.IOSVersion) -> SupportedPlatform
```

## Return Value

A `SupportedPlatform` instance.

## Discussion

> **Since**: First available in PackageDescription 5.0.

## Parameters

- `version`: The minimum deployment target that the package supports.

## See Also

### Supporting iOS
- [static func iOS(String) -> SupportedPlatform](./ios%28_%29-83bbf.md)
  Configures the minimum deployment target version for the iOS platform using a custom version string.
- [static let iOS: Platform](../platform/ios.md)
  The iOS platform.
- [SupportedPlatform.IOSVersion](./iosversion.md)
  The supported iOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/ios(_:)-5pvv5)*