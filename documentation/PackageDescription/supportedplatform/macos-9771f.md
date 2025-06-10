# macOS(_:)

**Framework**: PackageDescription  
**Kind**: method

Configures the minimum deployment target version for the macOS platform using a version string.

## Declaration

```swift
static func macOS(_ versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

The version string must be a series of two or three dot-separated integers, such as `10.10` or `10.10.1`.

> **Note**: First available in PackageDescription 5.0.

## Parameters

- `versionString`: The minimum deployment target as a string   representation of two or three dot-separated integers, such as   .

## See Also

- [static func macOS(SupportedPlatform.MacOSVersion) -> SupportedPlatform](supportedplatform/macos(_:)-2wthp.md)
  Configures the minimum deployment target version for the macOS platform.
- [static let macOS: Platform](platform/macos.md)
  The macOS platform.
- [SupportedPlatform.MacOSVersion](supportedplatform/macosversion.md)
  The supported macOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/macos(_:)-9771f)*