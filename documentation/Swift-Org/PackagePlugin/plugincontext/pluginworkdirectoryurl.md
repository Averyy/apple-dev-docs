---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugincontext/pluginworkdirectoryurl"
framework: "Swift-Org/PackagePlugin"
---

# pluginWorkDirectoryURL

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The URL of a writable directory into which the plugin or the build commands it constructs can write anything it wants.

**Availability**:
- SwiftPM 6.0+

## Declaration

```swift
let pluginWorkDirectoryURL: URL
```

## Discussion

This could include generated source files to processed further, as well as any caches used by the build tool or the plugin. The plugin is in complete control of what is written under this directory, and the package manager preserves the contents between builds.

A plugin may create a separate subdirectory for each command it creates, with the command configured to write its output to that directory. The plugin may also create other directories for cache files and other file system content that either it or the command will need.

## See Also

### Inspecting the Context
- [func tool(named: String) throws -> Tool](./tool%28named%29.md)
  Looks up and returns the path of a named command line executable.
- [let package: Package](./package.md)
  Information about the package the plugin works on.
- [PluginContext.Tool](./tool.md)
  Information about a particular tool that is available to a plugin.
- [let pluginWorkDirectory: Path](./pluginworkdirectory.md)
  The path of a writable directory into which the plugin or the build commands can write files.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugincontext/pluginworkdirectoryurl)*