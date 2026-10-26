---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugincontext/tool(named:)"
framework: "Swift-Org/PackagePlugin"
---

# tool(named:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Looks up and returns the path of a named command line executable.

## Declaration

```swift
func tool(named name: String) throws -> Tool
```

#### Discussion

The executable must be provided by an executable target or binary target on which the package plugin target depends. This function throws an error if the tool cannot be found. The lookup is case sensitive.

## Parameters

- `name`: The name of the executable to find.

## See Also

### Inspecting the Context
- [let pluginWorkDirectoryURL: URL](./pluginworkdirectoryurl.md)
  The URL of a writable directory into which the plugin or the build commands it constructs can write anything it wants.
- [let package: Package](./package.md)
  Information about the package the plugin works on.
- [PluginContext.Tool](./tool.md)
  Information about a particular tool that is available to a plugin.
- [let pluginWorkDirectory: Path](./pluginworkdirectory.md)
  The path of a writable directory into which the plugin or the build commands can write files.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugincontext/tool(named:))*