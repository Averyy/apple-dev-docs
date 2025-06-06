# custom(_:versionString:)

**Framework**: PackageDescription  
**Kind**: method

Configures the minimum deployment target version for custom platforms.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
static func custom(_ platformName: String, versionString: String) -> SupportedPlatform
```

#### Return Value

A `SupportedPlatform` instance.

#### Discussion

> **Note**: First available in PackageDescription 5.6

First available in PackageDescription 5.6

## Parameters

- `platformName`: The name of the platform.
- `versionString`: The minimum deployment target as a string representation of two or three dot-separated integers, such as  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/supportedplatform/custom(_:versionstring:))*