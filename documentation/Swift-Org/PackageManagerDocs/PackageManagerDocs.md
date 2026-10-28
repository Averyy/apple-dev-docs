---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs"
framework: "Swift-Org/PackageManagerDocs"
---

# Swift Package Manager

**Framework**: Swift-Org/PackageManagerDocs  
**Kind**: module

Organize, manage, and edit Swift packages.

## Overview

The Swift Package Manager lets you share your code as a package, depend on and use other shared packages, as well as build, test, document, and run your code.

> **Note**: Swift Package Manager [introduced the Swift Build build system as a preview](./swiftbuildpreview.md) in Swift 6.3, and [adopted it as the default build system ](./api-6.4.md) in Swift 6.4.

## Topics

### Essentials
- [Getting Started](./gettingstarted.md)
  Learn to create and use Swift packages.
- [Introducing Packages](./introducingpackages.md)
  Learn to create and use a Swift package.
- [Package Security](./packagesecurity.md)
  Learn about the security features that the package manager implements.
### Building Packages
- [Creating a Swift package](./creatingswiftpackage.md)
  Bundle executable or shareable code into a standalone Swift package.
- [Setting the Swift tools version](./settingswifttoolsversion.md)
  Define the minimum version of the swift compiler required for your package.
- [Using build configurations](./usingbuildconfigurations.md)
  Control the build configuration for your app or package.
- [Packaging based on the version of Swift](./swiftversionspecificpackaging.md)
  Provide a package manifest for a specific version of Swift.
- [Bundling resources with a Swift package](./bundlingresources.md)
  Add resource files to your Swift package and access them in your code.
- [Releasing and publishing a Swift package](./releasingpublishingapackage.md)
  Share a specific version of your package.
- [Generating Software Bill of Materials (SBOM)](./generatingsboms.md)
  Create an inventory of components and dependencies using SBOM documents.
- [Continuous Integration Workflows](./continuousintegration.md)
  Build Swift packages with an existing continuous integration setup and prepare apps that consume package dependencies within an existing CI pipeline.
- [Using shell completion scripts](./usingshellcompletion.md)
  Customize your shell to automatically complete swift package commands.
### Depedencies
- [Adding dependencies to a Swift package](./addingdependencies.md)
  Use other Swift packages, system libraries, or binary dependencies in your package.
- [Using a package registry](./usingswiftpackageregistry.md)
  Configure and use a package registry for Swift Package Manager.
- [Bundling resources with a Swift package](./bundlingresources.md)
  Add resource files to your Swift package and access them in your code.
### Targets
- [Creating C language targets](./creatingclanguagetargets.md)
  Include C language code as a target in your Swift package.
- [Creating Module Maps](./modulemaps.md)
  Define how C and C++ headers are exposed to Swift for system library targets, precompiled libraries, or C Language targets.
- [Module Aliasing](./modulealiasing.md)
  Create aliased names for modules to avoid collisions between targets in your package or its dependencies.
### Sharing Packages
- [Releasing and publishing a Swift package](./releasingpublishingapackage.md)
  Share a specific version of your package.
- [Package Collections](./packagecollections.md)
  Learn to create, publish and use Swift package collections.
### Extending Package Manager
- [Plugins](./plugins.md)
  Extend package manager functionality with build or command plugins.
- [Swift Package Manager as a library](./swiftpmasalibrary.md)
  Include Swift Package Manager as a dependency in your Swift package.
### Swift Commands
- [swift build](./swiftbuild.md)
  Build sources into binary products.
- [swift test](./swifttest.md)
  Build and run tests.
- [swift package](./swiftpackagecommands.md)
  Subcommands to update and inspect your Swift package.
- [swift sdk](./swiftsdkcommands.md)
  Perform operations on Swift SDKs.
- [swift package-registry](./swiftpackageregistrycommands.md)
  Interact with package registry and manage related configuration.
- [swift package-collection](./swiftpackagecollectioncommands.md)
  Interact with package collections.
- [swift run](./swiftrun.md)
  Build and run an executable product.
### Design
- [Swift Package Registry Service Specification](./registryserverspecification.md)
  Learn about the specification for SwiftPM’s registry service.
### Releases
- [Release Notes](./releasenotes.md)
### Articles
- [[6.3] Preview the Swift Build System Integration](./swiftbuildpreview.md)
  Understand, use, and preview the next-generation build system for Package Manager.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs)*