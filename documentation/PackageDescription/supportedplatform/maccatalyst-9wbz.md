# macCatalyst(_:)

**Framework**: Packagedescription  
**Kind**: method

Configures the minimum deployment target version for the Mac Catalyst platform using a version string.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func macCatalyst(_ versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

The version string must be a series of two or three dot-separated integers, such as `13.0` or `13.0.1`.

> **Note**: First available in PackageDescription 5.5

## Parameters

- `versionString`: The minimum deployment target as a string representation of two or three dot-separated integers, such as  .

## See Also

- [static func macCatalyst(SupportedPlatform.MacCatalystVersion) -> SupportedPlatform](supportedplatform/maccatalyst(_:)-6bh40.md)
  Configures the minimum deployment target version for the Mac Catalyst platform.
- [static let macCatalyst: Platform](platform/maccatalyst.md)
  The Mac Catalyst platform.
- [SupportedPlatform.MacCatalystVersion](supportedplatform/maccatalystversion.md)
  The supported Mac Catalyst version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/maccatalyst(_:)-9wbz)*