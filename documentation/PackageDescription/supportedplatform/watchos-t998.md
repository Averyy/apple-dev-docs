# watchOS(_:)

**Framework**: PackageDescription  
**Kind**: method

Configure the minimum deployment target version for the watchOS platform.

## Declaration

```swift
static func watchOS(_ version: SupportedPlatform.WatchOSVersion) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

> **Note**: First available in PackageDescription 5.0

## Parameters

- `version`: The minimum deployment target that the package supports.

## See Also

- [static func watchOS(String) -> SupportedPlatform](supportedplatform/watchos(_:)-4lrx0.md)
  Configure the minimum deployment target version for the watchOS platform using a custom version string.
- [static let watchOS: Platform](platform/watchos.md)
  The watchOS platform.
- [SupportedPlatform.WatchOSVersion](supportedplatform/watchosversion.md)
  The supported watchOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/watchos(_:)-t998)*