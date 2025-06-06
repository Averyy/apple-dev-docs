# nuget(_:)

**Framework**: PackageDescription  
**Kind**: method

Creates a system package provider with a list of installable packages for users of the NuGet package manager on Linux or Windows.

**Availability**:
- SwiftPM 999.0+

## Declaration

```swift
static func nuget(_ packages: [String]) -> SystemPackageProvider
```

#### Return Value

A package provider.

## Parameters

- `packages`: The list of package names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/systempackageprovider/nuget(_:))*