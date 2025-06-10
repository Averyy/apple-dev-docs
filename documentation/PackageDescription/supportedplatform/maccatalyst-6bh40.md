# macCatalyst(_:)

**Framework**: PackageDescription  
**Kind**: method

Configures the minimum deployment target version for the Mac Catalyst platform.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func macCatalyst(_ version: SupportedPlatform.MacCatalystVersion) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

> **Note**: First available in PackageDescription 5.5

## Parameters

- `version`: The minimum deployment target that the package supports.

## See Also

- [static func macCatalyst(String) -> SupportedPlatform](supportedplatform/maccatalyst(_:)-9wbz.md)
  Configures the minimum deployment target version for the Mac Catalyst platform using a version string.
- [static let macCatalyst: Platform](platform/maccatalyst.md)
  The Mac Catalyst platform.
- [SupportedPlatform.MacCatalystVersion](supportedplatform/maccatalystversion.md)
  The supported Mac Catalyst version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/maccatalyst(_:)-6bh40)*