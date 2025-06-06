# Package

**Framework**: PackageDescription  
**Kind**: class

The configuration of a Swift package.

## Declaration

```swift
final class Package
```

#### Overview

Pass configuration options as parameters to your package’s initializer statement to provide the name of the package, its targets, products, dependencies, and other configuration options.

By convention, you need to define the properties of a package in a single nested initializer statement. Don’t modify it after initialization. The following package manifest shows the initialization of a simple package object for the MyLibrary Swift package:

```swift
// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "MyLibrary",
    platforms: [
        .macOS(.v10_15),
    ],
    products: [
        .library(name: "MyLibrary", targets: ["MyLibrary"])
    ],
    dependencies: [
        .package(url: "https://url/of/another/package/named/utility", from: "1.0.0")
    ],
    targets: [
        .target(name: "MyLibrary", dependencies: ["Utility"]),
        .testTarget(name: "MyLibraryTests", dependencies: ["MyLibrary"])
    ]
)
```

In Swift tools versions earlier than 5.4, the package manifest must begin with the string `// swift-tools-version:` followed by a version number specifier. Version 5.4 and later has relaxed the whitespace requirements. The following code listing shows a few examples of valid declarations of the Swift tools version:

```swift
// swift-tools-version:3.0.2
// swift-tools-version:3.1
// swift-tools-version:4.0
// swift-tools-version:5.3
// swift-tools-version: 5.6
```

The Swift tools version declares the version of the `PackageDescription` library, the minimum version of the Swift tools and Swift language compatibility version to process the manifest, and the required minimum version of the Swift tools to use the Swift package. Each version of Swift can introduce updates to the PackageDescription framework, but the previous API version is available to packages which declare a prior tools version. This behavior means you can take advantage of new releases of Swift, the Swift tools, and the PackageDescription library, without having to update your package’s manifest or losing access to existing packages.

## Topics

### Creating a Package
- [init(name: String, defaultLocalization: LanguageTag?, platforms: [SupportedPlatform]?, pkgConfig: String?, providers: [SystemPackageProvider]?, products: [Product], dependencies: [Package.Dependency], targets: [Target], swiftLanguageVersions: [SwiftVersion]?, cLanguageStandard: CLanguageStandard?, cxxLanguageStandard: CXXLanguageStandard?)](package/init(name:defaultlocalization:platforms:pkgconfig:providers:products:dependencies:targets:swiftlanguageversions:clanguagestandard:cxxlanguagestandard:).md)
  Initializes a Swift package with configuration options you provide.
### Naming the Package
- [var name: String](package/name.md)
  The name of the Swift package.
### Localizing Package Resources
- [var defaultLocalization: LanguageTag?](package/defaultlocalization.md)
  The default localization for resources.
- [struct LanguageTag](languagetag.md)
  A wrapper around an IETF language tag.
### Configuring Products
- [var products: [Product]](package/products.md)
  The list of products that this package vends and that clients can use.
- [class Product](product.md)
  The object that defines a package product.
### Configuring Targets
- [var targets: [Target]](package/targets.md)
  The list of targets that are part of this package.
- [class Target](target.md)
  The basic building block of a Swift package.
### Declaring Supported Platforms
- [var platforms: [SupportedPlatform]?](package/platforms.md)
  The list of minimum versions for platforms supported by the package.
- [struct SupportedPlatform](supportedplatform.md)
  A platform that the Swift package supports.
- [struct Platform](platform.md)
  A platform supported by Swift Package Manager.
### Configuring System Packages
- [enum SystemPackageProvider](systempackageprovider.md)
  The system package providers that this package uses.
- [var pkgConfig: String?](package/pkgconfig.md)
  The name to use for C modules.
- [var providers: [SystemPackageProvider]?](package/providers.md)
  An array of providers for a system target.
### Declaring Package Dependencies
- [var dependencies: [Package.Dependency]](package/dependencies.md)
  The list of package dependencies.
- [Package.Dependency](package/dependency.md)
  A package dependency of a Swift package.
### Declaring Supported Languages
- [typealias SwiftVersion](swiftversion.md)
  Type alias to previous name for backward source compatibility
- [enum CLanguageStandard](clanguagestandard.md)
  The supported C language standard you use to compile C sources in the package.
- [enum CXXLanguageStandard](cxxlanguagestandard.md)
  The supported C++ language standard you use to compile C++ sources in the package.
- [var swiftLanguageVersions: [SwiftVersion]?](package/swiftlanguageversions.md)
  Legacy property name, accesses value of `swiftLanguageModes`
- [var cLanguageStandard: CLanguageStandard?](package/clanguagestandard.md)
  The C language standard to use for all C targets in this package.
- [var cxxLanguageStandard: CXXLanguageStandard?](package/cxxlanguagestandard.md)
  The C++ language standard to use for all C++ targets in this package.
### Initializers
- [init(name: String, defaultLocalization: LanguageTag?, platforms: [SupportedPlatform]?, pkgConfig: String?, providers: [SystemPackageProvider]?, products: [Product], dependencies: [Package.Dependency], targets: [Target], swiftLanguageModes: [SwiftLanguageMode]?, cLanguageStandard: CLanguageStandard?, cxxLanguageStandard: CXXLanguageStandard?)](package/init(name:defaultlocalization:platforms:pkgconfig:providers:products:dependencies:targets:swiftlanguagemodes:clanguagestandard:cxxlanguagestandard:).md)
  Initializes a Swift package with configuration options you provide.
- [init(name: String, defaultLocalization: LanguageTag?, platforms: [SupportedPlatform]?, pkgConfig: String?, providers: [SystemPackageProvider]?, products: [Product], traits: Set<Trait>, dependencies: [Package.Dependency], targets: [Target], swiftLanguageModes: [SwiftLanguageMode]?, cLanguageStandard: CLanguageStandard?, cxxLanguageStandard: CXXLanguageStandard?)](package/init(name:defaultlocalization:platforms:pkgconfig:providers:products:traits:dependencies:targets:swiftlanguagemodes:clanguagestandard:cxxlanguagestandard:).md)
  Initializes a Swift package with configuration options you provide.
- [init(name: String, pkgConfig: String?, providers: [SystemPackageProvider]?, products: [Product], dependencies: [Package.Dependency], targets: [Target], swiftLanguageVersions: [SwiftVersion]?, cLanguageStandard: CLanguageStandard?, cxxLanguageStandard: CXXLanguageStandard?)](package/init(name:pkgconfig:providers:products:dependencies:targets:swiftlanguageversions:clanguagestandard:cxxlanguagestandard:)-767rj.md)
  Initializes a Swift package with configuration options you provide.
- [init(name: String, pkgConfig: String?, providers: [SystemPackageProvider]?, products: [Product], dependencies: [Package.Dependency], targets: [Target], swiftLanguageVersions: [Int]?, cLanguageStandard: CLanguageStandard?, cxxLanguageStandard: CXXLanguageStandard?)](package/init(name:pkgconfig:providers:products:dependencies:targets:swiftlanguageversions:clanguagestandard:cxxlanguagestandard:)-7ld3y.md)
  Initializes a Swift package with configuration options you provide.
- [init(name: String, platforms: [SupportedPlatform]?, pkgConfig: String?, providers: [SystemPackageProvider]?, products: [Product], dependencies: [Package.Dependency], targets: [Target], swiftLanguageVersions: [SwiftVersion]?, cLanguageStandard: CLanguageStandard?, cxxLanguageStandard: CXXLanguageStandard?)](package/init(name:platforms:pkgconfig:providers:products:dependencies:targets:swiftlanguageversions:clanguagestandard:cxxlanguagestandard:).md)
  Initializes a Swift package with configuration options you provide.
### Instance Properties
- [var swiftLanguageModes: [SwiftLanguageMode]?](package/swiftlanguagemodes.md)
  The list of Swift language modes with which this package is compatible.
- [var traits: Set<Trait>](package/traits.md)
  The set of traits of this package.

## See Also

- [struct Context](context.md)
  The context information for a Swift package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/package)*