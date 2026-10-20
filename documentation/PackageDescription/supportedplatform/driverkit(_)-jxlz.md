# driverKit(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Configures the minimum deployment target version for the DriverKit platform.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func driverKit(_ version: SupportedPlatform.DriverKitVersion) -> SupportedPlatform
```

## Parameters

- `version`: The minimum deployment target that the package supports.

## See Also

### Supporting DriverKit
- [static func driverKit(String) -> SupportedPlatform](./driverkit%28_%29-6evdd.md)
  Configures the minimum deployment target version for the DriverKit platform using a custom version string.
- [static let driverKit: Platform](../platform/driverkit.md)
  The DriverKit platform
- [SupportedPlatform.DriverKitVersion](./driverkitversion.md)
  The supported DriverKit version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/driverkit(_:)-jxlz)*