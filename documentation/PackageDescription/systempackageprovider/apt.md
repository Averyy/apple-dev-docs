# apt(_:)

**Framework**: PackageDescription  
**Kind**: method

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

- [static func brew([String]) -> SystemPackageProvider](systempackageprovider/brew(_:).md)
  Creates a system package provider with a list of installable packages for people who use the HomeBrew package manager on macOS.
- [static func nuget([String]) -> SystemPackageProvider](systempackageprovider/nuget(_:).md)
  Creates a system package provider with a list of installable packages for users of the NuGet package manager on Linux or Windows.
- [static func yum([String]) -> SystemPackageProvider](systempackageprovider/yum(_:).md)
  Creates a system package provider with a list of installable packages for users of the yum package manager on Red Hat Enterprise Linux or CentOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/systempackageprovider/apt(_:))*