---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugindeserializationerror/malformedinputjson(_:)"
framework: "Swift-Org/PackagePlugin"
---

# PluginDeserializationError.malformedInputJSON(_:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

The input JSON is malformed in some way; the message provides more details.

## Declaration

```swift
case malformedInputJSON(_: String)
```

## See Also

### Errors while deserializing
- [PluginDeserializationError.missingBuildToolPluginProtocolConformance(protocolName:)](./missingbuildtoolpluginprotocolconformance%28protocolname%29.md)
  The plugin doesn’t conform to the BuildToolPlugin protocol.
- [PluginDeserializationError.missingCommandPluginProtocolConformance(protocolName:)](./missingcommandpluginprotocolconformance%28protocolname%29.md)
  The plugin doesn’t conform to the CommandPlugin protocol.
- [PluginDeserializationError.missingXcodeProjectPluginSupport](./missingxcodeprojectpluginsupport.md)
  The plugin doesn’t support Xcode
- [PluginDeserializationError.internalError(_:)](./internalerror%28_%29.md)
  An internal error of some kind; the message provides more details.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugindeserializationerror/malformedinputjson(_:))*