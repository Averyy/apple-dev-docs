---
url: "https://docs.swift.org/latest/documentation/packageplugin"
framework: "Swift-Org/PackagePlugin"
---

# PackagePlugin

**Framework**: Swift-Org/PackagePlugin  
**Kind**: module

Create plugins that extend the Swift Package Manager.

## Overview

Build tool plugins generate source files as part of a build, or perform other actions at the start of every build. The package manager invokes build tool plugins before a package is built in order to construct command invocations to run as part of the build. Command plugins provide actions that users can perform at any time and aren’t associated with a build.

Read [Writing a build tool plugin](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/WritingBuildToolPlugin) to learn how to create build tool plugins, or [Writing a command plugin](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/WritingCommandPlugin) to learn how to create command plugins.

## Topics

### Implementing Command Plugins
- [protocol CommandPlugin](./commandplugin.md)
  The plugin protocol that defines functionality for all plugins that have a command capability.
- [struct PluginContext](./plugincontext.md)
  A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.
- [protocol Plugin](./plugin.md)
  A protocol that defines functionality common to all package manger plugins.
### Extracting Arguments
- [struct ArgumentExtractor](./argumentextractor.md)
  A rudimentary helper for extracting options and flags from a list of strings that represent command line arguments.
### Implementing Build Plugins
- [protocol BuildToolPlugin](./buildtoolplugin.md)
  The plugin protocol that defines functionality for all plugins having a buildTool capability.
- [struct PluginContext](./plugincontext.md)
  A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.
- [protocol Target](./target.md)
  A single target defined in a package.
- [enum Command](./command.md)
  A command to run during the build.
### Interacting with Package Manager
- [struct PackageManager](./packagemanager.md)
  Provides specialized information and services from the Swift Package Manager or an IDE that supports Swift packages.
- [enum PackageManagerProxyError](./packagemanagerproxyerror.md)
  Errors from methods using the package manager.
### Inspecting the Package Representation
- [struct Package](./package.md)
  A single package in a graph of packages.
- [struct ToolsVersion](./toolsversion.md)
  A version of Swift package manager on whose semantics a package relies.
- [enum PackageOrigin](./packageorigin.md)
  The origin of a package.
- [struct PackageDependency](./packagedependency.md)
  A resolved dependency of a package.
- [protocol Product](./product.md)
  A single product defined in a package.
- [struct ExecutableProduct](./executableproduct.md)
  An executable product defined in a package.
- [struct LibraryProduct](./libraryproduct.md)
  A library product defined in a package.
### Inspecting Package Targets
- [protocol Target](./target.md)
  A single target defined in a package.
- [enum TargetDependency](./targetdependency.md)
  A dependency of a target on a product or on another target.
- [protocol SourceModuleTarget](./sourcemoduletarget.md)
  A target consisting of a source code module.
- [enum ModuleKind](./modulekind.md)
  The kind of module.
- [struct SwiftSourceModuleTarget](./swiftsourcemoduletarget.md)
  A target consisting of a source code module compiled using Swift.
- [struct ClangSourceModuleTarget](./clangsourcemoduletarget.md)
  A target consisting of a source code module compiled using Clang.
- [struct BinaryArtifactTarget](./binaryartifacttarget.md)
  A target describing an artifact that is distributed as a binary.
- [struct SystemLibraryTarget](./systemlibrarytarget.md)
  A target describing a system library that is expected to be present on the host system.
### Inspecting Package Files
- [struct FileList](./filelist.md)
  Provides information about a list of files.
- [struct File](./file.md)
  Information about a single file in a FileList.
- [enum FileType](./filetype.md)
  Information about the type of a file.
- [struct Path](./path.md)
  A simple representation of a path in the file system.
- [struct PathList](./pathlist.md)
  Provides information about a list of paths.
### Plugin Diagnostics and Errors
- [struct Diagnostics](./diagnostics.md)
  Emits errors, warnings, and remarks to show as a result of running the plugin.
- [enum PluginContextError](./plugincontexterror.md)
  Errors thrown while a plugin operates.
- [enum PluginDeserializationError](./plugindeserializationerror.md)
  Errors thrown while loading a plugin.
### Extended Modules
- [Swift](./swift.md)


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin)*