---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/swiftsdkcommands"
framework: "Swift-Org/PackageManagerDocs"
---

# swift sdk

**Framework**: Swift-Org/PackageManagerDocs

Perform operations on Swift SDKs.

**Availability**:
- Swift 6.1+

## Overview

By default, Swift Package Manager compiles code for the host platform on which you run it. Swift 6.1 introduced SDKs (through [SE-0387](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0387-cross-compilation-destinations.md)) to support cross-compilation.

SDKs are tightly coupled with the toolchain used to create them. Supported SDKs are distributed by the Swift project with links on the [installation page](https://www.swift.org/install/) for macOS and Linux, and included in the distribution for Windows.

Additionally, the Swift project provides the tooling repository [swift-sdk-generator](https://github.com/swiftlang/swift-sdk-generator) that you can use to create a custom SDK for your preferred platform.

## Topics

### Installing an SDK
- [swift sdk install](./sdkinstall.md)
  Installs a given Swift SDK bundle to a location discoverable by SwiftPM.
### Listing SDKs
- [swift sdk list](./sdklist.md)
  Print a list of IDs of available Swift SDKs available on the filesystem.
### Removing an SDK
- [swift sdk remove](./sdkremove.md)
  Removes a previously installed Swift SDK bundle from the filesystem.
### Configuring an SDK
- [swift sdk configure](./sdkconfigure.md)
  Manages configuration options for installed Swift SDKs.
### Deprecated Commands
- [swift sdk configuration set](./sdkconfigurationset.md)
  Sets configuration options for installed Swift SDKs.
- [swift sdk configuration show](./sdkconfigurationshow.md)
  Prints all configuration properties currently applied to a given Swift SDK and target triple.
- [swift sdk configuration reset](./sdkconfigurationreset.md)
  Resets configuration properties currently applied to a given Swift SDK and target triple. If no specific property is specified, all of them are reset for the Swift SDK.

## See Also

### Swift Commands
- [swift build](./swiftbuild.md)
  Build sources into binary products.
- [swift test](./swifttest.md)
  Build and run tests.
- [swift package](./swiftpackagecommands.md)
  Subcommands to update and inspect your Swift package.
- [swift package-registry](./swiftpackageregistrycommands.md)
  Interact with package registry and manage related configuration.
- [swift package-collection](./swiftpackagecollectioncommands.md)
  Interact with package collections.
- [swift run](./swiftrun.md)
  Build and run an executable product.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/swiftsdkcommands)*