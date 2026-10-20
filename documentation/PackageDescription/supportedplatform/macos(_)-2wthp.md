# macOS(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Configures the minimum deployment target version for the macOS platform.

## Declaration

```swift
static func macOS(_ version: SupportedPlatform.MacOSVersion) -> SupportedPlatform
```

#### Discussion

> **Since**: First available in PackageDescription 5.0

## Parameters

- `version`: The minimum deployment target that the package supports.

## See Also

### Supporting macOS
- [static func macOS(String) -> SupportedPlatform](./macos%28_%29-9771f.md)
  Configures the minimum deployment target version for the macOS platform using a version string.
- [static let macOS: Platform](../platform/macos.md)
  The macOS platform.
- [SupportedPlatform.MacOSVersion](./macosversion.md)
  The supported macOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/macos(_:)-2wthp)*