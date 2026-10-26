---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugincontexterror/toolnotfound(name:)"
framework: "Swift-Org/PackagePlugin"
---

# PluginContextError.toolNotFound(name:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

Could not find a tool with the given name.

## Declaration

```swift
case toolNotFound(name: String)
```

#### Discussion

This could be either because it doesn’t exist, or because the plugin doesn’t have a dependency on it.

## See Also

### Errors from the Plugin Context
- [case productNotFound(name: String, package: Package)](./productnotfound%28name,package%29.md)
  Could not find a product with the given name.
- [case targetNotFound(name: String, package: Package)](./targetnotfound%28name,package%29.md)
  Could not find a target with the given name.
- [PluginContextError.toolNotSupportedOnTargetPlatform(name:)](./toolnotsupportedontargetplatform%28name%29.md)
  The tool is not supported on the target platform


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugincontexterror/toolnotfound(name:))*