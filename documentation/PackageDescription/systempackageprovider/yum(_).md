# yum(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Creates a system package provider with a list of installable packages for users of the yum package manager on Red Hat Enterprise Linux or CentOS.

**Availability**:
- SwiftPM 5.3+

## Declaration

```swift
static func yum(_ packages: [String]) -> SystemPackageProvider
```

## Return Value

A package provider.

## Parameters

- `packages`: The list of package names.

## See Also

### Providing Hints to Users of System Packages
- [static func apt([String]) -> SystemPackageProvider](./apt%28_%29.md)
  Creates a system package provider with a list of installable packages for users of the apt-get package manager on Ubuntu Linux.
- [static func brew([String]) -> SystemPackageProvider](./brew%28_%29.md)
  Creates a system package provider with a list of installable packages for people who use the HomeBrew package manager on macOS.
- [static func nuget([String]) -> SystemPackageProvider](./nuget%28_%29.md)
  Creates a system package provider with a list of installable packages for users of the NuGet package manager on Linux or Windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/systempackageprovider/yum(_:))*