# tvOS(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Configures the minimum deployment target version for the tvOS platform.

## Declaration

```swift
static func tvOS(_ version: SupportedPlatform.TVOSVersion) -> SupportedPlatform
```

## Return Value

A `SupportedPlatform` instance.

## Discussion

> **Since**: First available in PackageDescription 5.0

## Parameters

- `version`: The minimum deployment target that the package supports.

## See Also

### Supporting tvOS
- [static func tvOS(String) -> SupportedPlatform](./tvos%28_%29-3k8sy.md)
  Configures the minimum deployment target version for the tvOS platform using a custom version string.
- [static let tvOS: Platform](../platform/tvos.md)
  The tvOS platform.
- [SupportedPlatform.TVOSVersion](./tvosversion.md)
  The supported tvOS version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/tvos(_:)-6931l)*