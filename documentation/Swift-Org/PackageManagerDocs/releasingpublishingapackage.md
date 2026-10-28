---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/releasingpublishingapackage"
framework: "Swift-Org/PackageManagerDocs"
---

# Releasing and publishing a Swift package

**Framework**: Swift-Org/PackageManagerDocs  
**Role**: Article

Share a specific version of your package.

## Overview

Swift Package Manager expects a package to be remotely shared as a single Git repository, with a tag that conforms to a full semantic version, and a `Package.swift` manifest in the root of the repository.

To publish a package that is hosted in a Git repository, create and push a semantic version tag. Swift package manager expects the tag to be a full semantic version, that includes major, minor, and patch versions in the tag.

The following commands illustrate adding a tag `1.0.0` and pushing those tags to the remote repository:

```bash
$ git tag 1.0.0
$ git push origin --tags
```

> ⚠️ **Warning**: A tag in the form of `1.0` isn’t recognized by Swift Package Manager as a complete semantic version. Include all three integers reflecting the major, minor, and patch version information.

With the tag in place, other packages can depend on the package you tagged through your source repository. An example of a published package can be found at [github.com/apple/example-package-playingcard](https://github.com/apple/example-package-playingcard/) with multiple releases available.

To read more about adding a dependency to your package, read [Adding dependencies to a Swift package](./addingdependencies.md).

## See Also

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
- [Generating Software Bill of Materials (SBOM)](./generatingsboms.md)
  Create an inventory of components and dependencies using SBOM documents.
- [Continuous Integration Workflows](./continuousintegration.md)
  Build Swift packages with an existing continuous integration setup and prepare apps that consume package dependencies within an existing CI pipeline.
- [Using shell completion scripts](./usingshellcompletion.md)
  Customize your shell to automatically complete swift package commands.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/releasingpublishingapackage)*