---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugincontexterror"
framework: "Swift-Org/PackagePlugin"
---

# PluginContextError

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

Errors thrown while a plugin operates.

## Declaration

```swift
enum PluginContextError
```

## Topics

### Errors from the Plugin Context
- [case productNotFound(name: String, package: Package)](./plugincontexterror/productnotfound%28name,package%29.md)
  Could not find a product with the given name.
- [case targetNotFound(name: String, package: Package)](./plugincontexterror/targetnotfound%28name,package%29.md)
  Could not find a target with the given name.
- [PluginContextError.toolNotFound(name:)](./plugincontexterror/toolnotfound%28name%29.md)
  Could not find a tool with the given name.
- [PluginContextError.toolNotSupportedOnTargetPlatform(name:)](./plugincontexterror/toolnotsupportedontargetplatform%28name%29.md)
  The tool is not supported on the target platform
### Default Implementations
- [CustomStringConvertible Implementations](./plugincontexterror/customstringconvertible-implementations.md)
- [Error Implementations](./plugincontexterror/error-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Error
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Plugin Diagnostics and Errors
- [struct Diagnostics](./diagnostics.md)
  Emits errors, warnings, and remarks to show as a result of running the plugin.
- [enum PluginDeserializationError](./plugindeserializationerror.md)
  Errors thrown while loading a plugin.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugincontexterror)*