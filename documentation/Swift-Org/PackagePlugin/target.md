---
url: "https://docs.swift.org/latest/documentation/packageplugin/target"
framework: "Swift-Org/PackagePlugin"
---

# Target

**Framework**: Swift-Org/PackagePlugin  
**Kind**: protocol  
**Role**: Protocol

A single target defined in a package.

## Declaration

```swift
protocol Target
```

## Topics

### Inspecting a target
- [var id: ID](./target/id-swift.property.md)
  Unique identifier for the target.
- [var name: String](./target/name.md)
  The name of the target, as defined in the package manifest.
- [var directoryURL: URL](./target/directoryurl.md)
  The file URL of the target directory in the local file system.
- [var sourceModule: SourceModuleTarget?](./target/sourcemodule.md)
  Convenience accessor which casts the receiver to`SourceModuleTarget`, if possible.
- [var dependencies: [TargetDependency]](./target/dependencies.md)
  Any other targets on which this target depends, in the same order as they are specified in the package manifest.
- [var recursiveTargetDependencies: [Target]](./target/recursivetargetdependencies.md)
  The transitive closure of all the targets on which the receiver depends.
- [typealias ID](./target/id-swift.typealias.md)
  The type that represents the ID of the target.
- [var directory: Path](./target/directory.md)
  The absolute path of the target directory in the local file system.

## Relationships

### Inherited By
- [SourceModuleTarget](./sourcemoduletarget.md)
### Conforming Types
- [BinaryArtifactTarget](./binaryartifacttarget.md)
- [ClangSourceModuleTarget](./clangsourcemoduletarget.md)
- [SwiftSourceModuleTarget](./swiftsourcemoduletarget.md)
- [SystemLibraryTarget](./systemlibrarytarget.md)

## See Also

### Implementing Build Plugins
- [protocol BuildToolPlugin](./buildtoolplugin.md)
  The plugin protocol that defines functionality for all plugins having a buildTool capability.
- [struct PluginContext](./plugincontext.md)
  A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.
- [enum Command](./command.md)
  A command to run during the build.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/target)*