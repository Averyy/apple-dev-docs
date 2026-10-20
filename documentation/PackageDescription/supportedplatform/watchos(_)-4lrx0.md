# watchOS(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Configure the minimum deployment target version for the watchOS platform using a custom version string.

## Declaration

```swift
static func watchOS(_ versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

The version string must be a series of two or three dot-separated integers, such as `2.0` or `2.0.1`.

> **Since**: First available in PackageDescription 5.0

## Parameters

- `versionString`: The minimum deployment target as a string representation of two or three dot-separated integers, such as `2.0.1`.

## See Also

### Supporting watchOS
- [static func watchOS(SupportedPlatform.WatchOSVersion) -> SupportedPlatform](./watchos%28_%29-t998.md)
  Configure the minimum deployment target version for the watchOS platform.
- [static let watchOS: Platform](../platform/watchos.md)
  The watchOS platform.
- [SupportedPlatform.WatchOSVersion](./watchosversion.md)
  The supported watchOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/watchos(_:)-4lrx0)*