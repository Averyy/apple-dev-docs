# driverKit(_:)

**Framework**: PackageDescription  
**Kind**: method

Configures the minimum deployment target version for the DriverKit platform using a custom version string.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func driverKit(_ versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

## Parameters

- `versionString`: The minimum deployment target as a string representation of two or three dot-separated integers, such as  .

## See Also

- [static func driverKit(SupportedPlatform.DriverKitVersion) -> SupportedPlatform](supportedplatform/driverkit(_:)-jxlz.md)
  Configures the minimum deployment target version for the DriverKit platform.
- [static let driverKit: Platform](platform/driverkit.md)
  The DriverKit platform
- [SupportedPlatform.DriverKitVersion](supportedplatform/driverkitversion.md)
  The supported DriverKit version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/driverkit(_:)-6evdd)*