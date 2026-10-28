# visionOS(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Configure the minimum deployment target version for the visionOS platform.

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
static func visionOS(_ version: SupportedPlatform.VisionOSVersion) -> SupportedPlatform
```

## Return Value

A `SupportedPlatform` instance.

## Discussion

> **Since**: First available in PackageDescription 5.9

## Parameters

- `version`: The minimum deployment target that the package supports.

## See Also

### Supporting visionOS
- [static func visionOS(String) -> SupportedPlatform](./visionos%28_%29-6ur2u.md)
  Configure the minimum deployment target version for the visionOS platform using a custom version string.
- [static let visionOS: Platform](../platform/visionos.md)
  The visionOS platform.
- [SupportedPlatform.VisionOSVersion](./visionosversion.md)
  The supported visionOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/visionos(_:)-3ip0z)*