---
url: "https://docs.swift.org/latest/documentation/packageplugin/buildtoolplugin"
framework: "Swift-Org/PackagePlugin"
---

# BuildToolPlugin

**Framework**: Swift-Org/PackagePlugin  
**Kind**: protocol  
**Role**: Protocol

The plugin protocol that defines functionality for all plugins having a buildTool capability.

## Declaration

```swift
protocol BuildToolPlugin : Plugin
```

## Topics

### Creating a Build Tool Plugin
- [func createBuildCommands(context: PluginContext, target: Target) async throws -> [Command]](./buildtoolplugin/createbuildcommands%28context,target%29.md)
  Invoked by the package manager to create build commands for a particular target.

## Relationships

### Inherits From
- [Plugin](./plugin.md)

## See Also

### Implementing Build Plugins
- [struct PluginContext](./plugincontext.md)
  A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.
- [protocol Target](./target.md)
  A single target defined in a package.
- [enum Command](./command.md)
  A command to run during the build.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/buildtoolplugin)*