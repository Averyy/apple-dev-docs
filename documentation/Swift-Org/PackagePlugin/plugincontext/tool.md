---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugincontext/tool"
framework: "Swift-Org/PackagePlugin"
---

# PluginContext.Tool

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Information about a particular tool that is available to a plugin.

## Declaration

```swift
struct Tool
```

## Topics

### Instance Properties
- [let name: String](./tool/name.md)
  The name of the tool, suitable for display purposes.
- [var path: Path](./tool/path.md)
  The path of the tool in the file system.
- [let url: URL](./tool/url.md)
  The file URL of the tool in the file system.

## See Also

### Inspecting the Context
- [let pluginWorkDirectoryURL: URL](./pluginworkdirectoryurl.md)
  The URL of a writable directory into which the plugin or the build commands it constructs can write anything it wants.
- [func tool(named: String) throws -> Tool](./tool%28named%29.md)
  Looks up and returns the path of a named command line executable.
- [let package: Package](./package.md)
  Information about the package the plugin works on.
- [let pluginWorkDirectory: Path](./pluginworkdirectory.md)
  The path of a writable directory into which the plugin or the build commands can write files.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugincontext/tool)*