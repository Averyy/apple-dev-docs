---
url: "https://docs.swift.org/latest/documentation/packagemanagerdocs/swiftpackagecommands"
framework: "Swift-Org/PackageManagerDocs"
---

# swift package

**Framework**: Swift-Org/PackageManagerDocs

Subcommands to update and inspect your Swift package.

## Overview

Overview of package manager commands here…

## Topics

### Creating packages
- [swift package init](./packageinit.md)
  Initialize a new package.
### Updating and resolving dependencies
- [swift package update](./packageupdate.md)
  Update package dependencies.
- [swift package resolve](./packageresolve.md)
  Resolve package dependencies.
### Editing packages
- [swift package add-dependency](./packageadddependency.md)
  Add a package dependency to the manifest.
- [swift package add-product](./packageaddproduct.md)
  Add a new product to the manifest.
- [swift package add-target](./packageaddtarget.md)
  Add a new target to the manifest.
- [swift package add-target-dependency](./packageaddtargetdependency.md)
  Add a new target dependency to the manifest.
- [swift package add-setting](./packageaddsetting.md)
  Add a new setting to the manifest.
- [swift package edit](./packageedit.md)
  Put a package in editable mode.
- [swift package unedit](./packageunedit.md)
  Remove a package from editable mode.
- [swift package migrate](./packagemigrate.md)
  Migrate a package or its individual targets to use the given set of features.
### Using package manager plugins
- [swift package plugin](./packageplugin.md)
  Invoke a command plugin or perform other actions on command plugins.
- [swift package diagnose-api-breaking-changes](./packagediagnoseapibreakingchange.md)
  Diagnose API-breaking changes to Swift modules in a package.
### Inspecting packages
- [swift package describe](./packagedescribe.md)
  Describe the current package.
- [swift package show-dependencies](./packageshowdependencies.md)
  Print the resolved dependency graph.
- [swift package show-executables](./packageshowexecutables.md)
  List the available executables from this package.
- [swift package show-traits](./packageshowtraits.md)
  List the available traits for a package.
- [swift package tools-version](./packagetoolsversion.md)
  Manipulate tools version of the current package.
- [swift package dump-package](./packagedumppackage.md)
  Print parsed Package.swift as JSON.
- [swift package dump-symbol-graph](./packagedumpsymbolgraph.md)
  Dump symbol graphs.
### Cleaning builds and caches
- [swift package clean](./packageclean.md)
  Delete build artifacts.
- [swift package reset](./packagereset.md)
  Reset the complete cache/build directory.
- [swift package purge-cache](./packagepurgecache.md)
  Purge the global repository cache.
### Archiving packages
- [swift package archive-source](./packagearchivesource.md)
  Create a source archive for the package.
- [swift package compute-checksum](./packagecomputechecksum.md)
  Compute the checksum for a binary artifact.
### Integrating Package Manager into your shell
- [swift package completion-tool](./packagecompletiontool.md)
  Command to generate shell completions.
### Configuring Mirrors
- [swift package config set-mirror](./packageconfigsetmirror.md)
  Set a mirror for a dependency.
- [swift package config unset-mirror](./packageconfigunsetmirror.md)
  Remove an existing mirror.
- [swift package config get-mirror](./packageconfiggetmirror.md)
  Print mirror configuration for the given package dependency.
### Generating SBOMs
- [swift.package.generate-sbom](./packagegeneratesbom.md)
  Generate a Software Bill of Materials (SBOM).
### Experimental commands
- [swift package experimental-install](./packageexperimentalinstall.md)
  Offers the ability to install executable products of the current package.
- [swift package experimental-uninstall](./packageexperimentaluninstall.md)
  Offers the ability to uninstall executable products previously installed by `swift package experimental-install`.

## See Also

### Swift Commands
- [swift build](./swiftbuild.md)
  Build sources into binary products.
- [swift test](./swifttest.md)
  Build and run tests.
- [swift sdk](./swiftsdkcommands.md)
  Perform operations on Swift SDKs.
- [swift package-registry](./swiftpackageregistrycommands.md)
  Interact with package registry and manage related configuration.
- [swift package-collection](./swiftpackagecollectioncommands.md)
  Interact with package collections.
- [swift run](./swiftrun.md)
  Build and run an executable product.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packagemanagerdocs/swiftpackagecommands)*