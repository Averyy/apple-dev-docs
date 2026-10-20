# apt(_:)

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

Creates a system package provider with a list of installable packages for users of the apt-get package manager on Ubuntu Linux.

## Declaration

```swift
static func apt(_ packages: [String]) -> SystemPackageProvider
```

#### Return Value

A package provider.

## Parameters

- `packages`: The list of package names.

## See Also

### Providing Hints to Users of System Packages
- [static func brew([String]) -> SystemPackageProvider](./brew%28_%29.md)
  Creates a system package provider with a list of installable packages for people who use the HomeBrew package manager on macOS.
- [static func nuget([String]) -> SystemPackageProvider](./nuget%28_%29.md)
  Creates a system package provider with a list of installable packages for users of the NuGet package manager on Linux or Windows.
- [static func yum([String]) -> SystemPackageProvider](./yum%28_%29.md)
  Creates a system package provider with a list of installable packages for users of the yum package manager on Red Hat Enterprise Linux or CentOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/systempackageprovider/apt(_:))*