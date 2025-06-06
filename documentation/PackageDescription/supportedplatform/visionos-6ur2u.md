# visionOS(_:)

**Framework**: PackageDescription  
**Kind**: method

Configure the minimum deployment target version for the visionOS platform using a custom version string.

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
static func visionOS(_ versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

The version string must be a series of two or three dot-separated integers, such as `1.0` or `1.0.0`.

> **Note**: First available in PackageDescription 5.9

First available in PackageDescription 5.9

## Parameters

- `versionString`: The minimum deployment target as a string   representation of two or three dot-separated integers, such as  .

## See Also

- [static func visionOS(SupportedPlatform.VisionOSVersion) -> SupportedPlatform](supportedplatform/visionos(_:)-3ip0z.md)
  Configure the minimum deployment target version for the visionOS platform.
- [static let visionOS: Platform](platform/visionos.md)
  The visionOS platform.
- [SupportedPlatform.VisionOSVersion](supportedplatform/visionosversion.md)
  The supported visionOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/visionos(_:)-6ur2u)*