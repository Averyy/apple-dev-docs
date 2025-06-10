# SystemPackageProvider

**Framework**: PackageDescription  
**Kind**: enum

The system package providers that this package uses.

## Declaration

```swift
enum SystemPackageProvider
```

## Topics

### Providing Hints to Users of System Packages
- [static func apt([String]) -> SystemPackageProvider](systempackageprovider/apt(_:).md)
  Creates a system package provider with a list of installable packages for users of the apt-get package manager on Ubuntu Linux.
- [static func brew([String]) -> SystemPackageProvider](systempackageprovider/brew(_:).md)
  Creates a system package provider with a list of installable packages for people who use the HomeBrew package manager on macOS.
- [static func nuget([String]) -> SystemPackageProvider](systempackageprovider/nuget(_:).md)
  Creates a system package provider with a list of installable packages for users of the NuGet package manager on Linux or Windows.
- [static func yum([String]) -> SystemPackageProvider](systempackageprovider/yum(_:).md)
  Creates a system package provider with a list of installable packages for users of the yum package manager on Red Hat Enterprise Linux or CentOS.
### Enumeration Cases
- [SystemPackageProvider.aptItem(_:)](systempackageprovider/aptitem(_:).md)
  Packages installable by the apt-get package manager.
- [SystemPackageProvider.brewItem(_:)](systempackageprovider/brewitem(_:).md)
  Packages installable by the HomeBrew package manager.
- [SystemPackageProvider.nugetItem(_:)](systempackageprovider/nugetitem(_:).md)
  Packages installable by the NuGet package manager.
- [SystemPackageProvider.yumItem(_:)](systempackageprovider/yumitem(_:).md)
  Packages installable by the Yellowdog Updated, Modified (YUM) package manager.

## See Also

- [var pkgConfig: String?](package/pkgconfig.md)
  The name to use for C modules.
- [var providers: [SystemPackageProvider]?](package/providers.md)
  An array of providers for a system target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/systempackageprovider)*