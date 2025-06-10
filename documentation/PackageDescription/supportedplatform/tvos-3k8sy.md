# tvOS(_:)

**Framework**: PackageDescription  
**Kind**: method

Configures the minimum deployment target version for the tvOS platform using a custom version string.

## Declaration

```swift
static func tvOS(_ versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

The version string must be a series of two or three dot-separated integers,such as `9.0` or `9.0.1`.

> **Note**: First available in PackageDescription 5.0

## Parameters

- `versionString`: The minimum deployment target as a string   representation of two or three dot-separated integers, such as  .

## See Also

- [static func tvOS(SupportedPlatform.TVOSVersion) -> SupportedPlatform](supportedplatform/tvos(_:)-6931l.md)
  Configures the minimum deployment target version for the tvOS platform.
- [static let tvOS: Platform](platform/tvos.md)
  The tvOS platform.
- [SupportedPlatform.TVOSVersion](supportedplatform/tvosversion.md)
  The supported tvOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/tvos(_:)-3k8sy)*