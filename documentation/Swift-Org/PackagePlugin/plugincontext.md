---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugincontext"
framework: "Swift-Org/PackagePlugin"
---

# PluginContext

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.

## Declaration

```swift
struct PluginContext
```

## Topics

### Inspecting the Context
- [let pluginWorkDirectoryURL: URL](./plugincontext/pluginworkdirectoryurl.md)
  The URL of a writable directory into which the plugin or the build commands it constructs can write anything it wants.
- [func tool(named: String) throws -> Tool](./plugincontext/tool%28named%29.md)
  Looks up and returns the path of a named command line executable.
- [let package: Package](./plugincontext/package.md)
  Information about the package the plugin works on.
- [PluginContext.Tool](./plugincontext/tool.md)
  Information about a particular tool that is available to a plugin.
- [let pluginWorkDirectory: Path](./plugincontext/pluginworkdirectory.md)
  The path of a writable directory into which the plugin or the build commands can write files.

## See Also

### Implementing Command Plugins
- [protocol CommandPlugin](./commandplugin.md)
  The plugin protocol that defines functionality for all plugins that have a command capability.
- [protocol Plugin](./plugin.md)
  A protocol that defines functionality common to all package manger plugins.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugincontext)*