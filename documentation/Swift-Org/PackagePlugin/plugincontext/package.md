---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugincontext/package"
framework: "Swift-Org/PackagePlugin"
---

# package

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

Information about the package the plugin works on.

## Declaration

```swift
let package: Package
```

## See Also

### Inspecting the Context
- [let pluginWorkDirectoryURL: URL](./pluginworkdirectoryurl.md)
  The URL of a writable directory into which the plugin or the build commands it constructs can write anything it wants.
- [func tool(named: String) throws -> Tool](./tool%28named%29.md)
  Looks up and returns the path of a named command line executable.
- [PluginContext.Tool](./tool.md)
  Information about a particular tool that is available to a plugin.
- [let pluginWorkDirectory: Path](./pluginworkdirectory.md)
  The path of a writable directory into which the plugin or the build commands can write files.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugincontext/package)*