---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/settingswifttoolsversion"
framework: "Swift-Org/PackageManagerDocs"
---

# Setting the Swift tools version

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Define the minimum version of the swift compiler required for your package.

#### Overview

The tools version declares the minimum version of the Swift compiler required to use the package, as well as how parse the `Package.swift` manifest. When you create a new package using [swift package init](./packageinit.md), the minimum version is set automatically to the current version. The version is specified on the first line of the manifest with the comment `// swift-tools-version:` and the version for the Swift compiler. The version is a semantic version, with the exception that a patch version is inferred to be `0` if you don’t specify it.

For example, the following line asserts the package requires the Swift compiler version 6.1 or later:

```swift
// swift-tools-version:6.1
```

##### Resolving dependencies with different tools versions

When resolving package dependencies, if the tools version of a dependency is greater than the version in use, that version of the dependency is ineligible and dependency resolution continues with evaluating the next-best version.

If no tools version of a dependency, which otherwise meets the package version requirements, supports the version of the Swift tools in use, the package manager presents a dependency resolution error. For more information on providing package manifests for specific Swift versions, see [Packaging based on the version of Swift](./swiftversionspecificpackaging.md).

##### Adjusting the tools version.

Edit the `Package.swift` to adjust the version, or use [swift package tools-version](./packagetoolsversion.md) to report or set the the tools version.

## See Also

### Building Packages
- [Creating a Swift package](./creatingswiftpackage.md)
  Bundle executable or shareable code into a standalone Swift package.
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


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/settingswifttoolsversion)*