---
url: "https://docs.swift.org/latest/documentation/packageplugin/commandplugin"
framework: "Swift-Org/PackagePlugin"
---

# CommandPlugin

**Framework**: Swift-Org/PackagePlugin  
**Kind**: protocol  
**Role**: Protocol

The plugin protocol that defines functionality for all plugins that have a command capability.

## Declaration

```swift
protocol CommandPlugin : Plugin
```

## Topics

### Creating a Command Plugin
- [func performCommand(context: PluginContext, arguments: [String]) async throws](./commandplugin/performcommand%28context,arguments%29.md)
  Invoked by the package manager to perform the custom actions of the command.
### Accessing the Package Manager
- [var packageManager: PackageManager](./commandplugin/packagemanager.md)
  A proxy to the Swift Package Manager or IDE hosting the command plugin, through which the plugin can ask for specialized information or actions.

## Relationships

### Inherits From
- [Plugin](./plugin.md)

## See Also

### Implementing Command Plugins
- [struct PluginContext](./plugincontext.md)
  A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.
- [protocol Plugin](./plugin.md)
  A protocol that defines functionality common to all package manger plugins.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/commandplugin)*