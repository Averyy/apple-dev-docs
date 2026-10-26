---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugin"
framework: "Swift-Org/PackagePlugin"
---

# Plugin

**Framework**: Swift-Org/PackagePlugin  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines functionality common to all package manger plugins.

## Declaration

```swift
protocol Plugin
```

#### Overview

For example, the way to instantiate and run a plugin.

## Topics

### Creating a plugin
- [init()](./plugin/init%28%29.md)
  Instantiates the plugin.
### Invoking a plugin
- [static func main() async throws](./plugin/main%28%29.md)
  The main entry point of the plugin.

## Relationships

### Inherited By
- [BuildToolPlugin](./buildtoolplugin.md)
- [CommandPlugin](./commandplugin.md)

## See Also

### Implementing Command Plugins
- [protocol CommandPlugin](./commandplugin.md)
  The plugin protocol that defines functionality for all plugins that have a command capability.
- [struct PluginContext](./plugincontext.md)
  A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugin)*