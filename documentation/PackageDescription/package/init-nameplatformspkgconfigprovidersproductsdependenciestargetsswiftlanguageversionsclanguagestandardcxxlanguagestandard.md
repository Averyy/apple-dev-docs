# init(name:platforms:pkgConfig:providers:products:dependencies:targets:swiftLanguageVersions:cLanguageStandard:cxxLanguageStandard:)

**Framework**: PackageDescription  
**Kind**: init

Initializes a Swift package with configuration options you provide.

## Declaration

```swift
init(name: String, platforms: [SupportedPlatform]? = nil, pkgConfig: String? = nil, providers: [SystemPackageProvider]? = nil, products: [Product] = [], dependencies: [Package.Dependency] = [], targets: [Target] = [], swiftLanguageVersions: [SwiftVersion]? = nil, cLanguageStandard: CLanguageStandard? = nil, cxxLanguageStandard: CXXLanguageStandard? = nil)
```

## Parameters

- `name`: The name of the Swift package, or  , if you want the Swift Package Manager to deduce the   name from the package’s Git URL.
- `platforms`: The list of supported platforms that have a custom deployment target.
- `pkgConfig`: The name to use for C modules. If present, the Swift   Package Manager searches for a   file to get the   additional flags required for a system target.
- `products`: The list of products that this package makes available for clients to use.
- `dependencies`: The list of package dependencies.
- `targets`: The list of targets that are part of this package.
- `swiftLanguageVersions`: The list of Swift versions that this package is compatible with.
- `cLanguageStandard`: The C language standard to use for all C targets in this package.
- `cxxLanguageStandard`: The C++ language standard to use for all C++ targets in this package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package/init(name:platforms:pkgconfig:providers:products:dependencies:targets:swiftlanguageversions:clanguagestandard:cxxlanguagestandard:))*