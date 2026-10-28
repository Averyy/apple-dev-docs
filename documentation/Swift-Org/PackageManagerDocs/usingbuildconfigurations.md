---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/usingbuildconfigurations"
framework: "Swift-Org/PackageManagerDocs"
---

# Using build configurations

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Control the build configuration for your app or package.

## Overview

Package manager supports two general build configurations: Debug (default) and Release.

### Debug

By default, running `swift build` builds the package using its debug configuration. Alternatively, you can use `swift build -c debug`. Package manager locates the build artifacts in a directory called `debug` under the `.build` folder. When building in the debug configuration, a Swift target uses the following Swift compiler flags:

- `-Onone`: Compile without any optimization.
- `-g`: Generate debug information.
- `-enable-testing`: Enable the Swift compiler’s testability feature.

A C language target in the debug configuration uses the following flags:

- `-O0`: Compile without any optimization.
- `-g`: Generate debug information.

### Release

To build in release mode, type `swift build -c release`. Package manager locates the build artifacts in a directory called `release` under the `.build` folder. When building in the release configuration, a Swift target uses the following Swift compiler flags:

- `-O`: Compile with optimizations.
- `-whole-module-optimization`: Optimize input files (per module) together instead of individually.

A C language target in the release configuration uses the following flags:

- `-O2`: Compile with optimizations.

### Additional Flags

You can pass additional flags to the C, C++, or Swift compilers in three different ways:

- Command-line flags passed to these tools: flags like `-Xcc` (for the C compiler) or `-Xswiftc` (for the Swift compiler) pass relevant flags for all targets in the manifest.
- Target-specific flags in the manifest: use options like `cSettings` or `swiftSettings` for fine-grained control of compilation flags for particular targets.
- A destination JSON file: once you have a set of working command-line flags to apply to all targets, collect them in a JSON file and pass them in through `extra-cc-flags` and `extra-swiftc-flags` with `--destination example.json`.

One difference is that C flags passed on the `-Xcc` command-line or using a manifest’s `cSettings` are supplied to the Swift compiler tool for convenience, but `extra-cc-flags` aren’t.

## See Also

### Building Packages
- [Creating a Swift package](./creatingswiftpackage.md)
  Bundle executable or shareable code into a standalone Swift package.
- [Setting the Swift tools version](./settingswifttoolsversion.md)
  Define the minimum version of the swift compiler required for your package.
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


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/usingbuildconfigurations)*