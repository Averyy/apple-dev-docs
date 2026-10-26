---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugindeserializationerror"
framework: "Swift-Org/PackagePlugin"
---

# PluginDeserializationError

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

Errors thrown while loading a plugin.

## Declaration

```swift
enum PluginDeserializationError
```

## Topics

### Errors while deserializing
- [PluginDeserializationError.missingBuildToolPluginProtocolConformance(protocolName:)](./plugindeserializationerror/missingbuildtoolpluginprotocolconformance%28protocolname%29.md)
  The plugin doesn’t conform to the BuildToolPlugin protocol.
- [PluginDeserializationError.missingCommandPluginProtocolConformance(protocolName:)](./plugindeserializationerror/missingcommandpluginprotocolconformance%28protocolname%29.md)
  The plugin doesn’t conform to the CommandPlugin protocol.
- [PluginDeserializationError.missingXcodeProjectPluginSupport](./plugindeserializationerror/missingxcodeprojectpluginsupport.md)
  The plugin doesn’t support Xcode
- [PluginDeserializationError.malformedInputJSON(_:)](./plugindeserializationerror/malformedinputjson%28_%29.md)
  The input JSON is malformed in some way; the message provides more details.
- [PluginDeserializationError.internalError(_:)](./plugindeserializationerror/internalerror%28_%29.md)
  An internal error of some kind; the message provides more details.
### Default Implementations
- [CustomStringConvertible Implementations](./plugindeserializationerror/customstringconvertible-implementations.md)
- [Error Implementations](./plugindeserializationerror/error-implementations.md)

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
- [enum PluginContextError](./plugincontexterror.md)
  Errors thrown while a plugin operates.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugindeserializationerror)*