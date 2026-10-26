---
url: "https://docs.swift.org/latest/documentation/packageplugin/plugindeserializationerror/missingbuildtoolpluginprotocolconformance(protocolname:)"
framework: "Swift-Org/PackagePlugin"
---

# PluginDeserializationError.missingBuildToolPluginProtocolConformance(protocolName:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

The plugin doesn’t conform to the BuildToolPlugin protocol.

## Declaration

```swift
case missingBuildToolPluginProtocolConformance(protocolName: String)
```

## See Also

### Errors while deserializing
- [PluginDeserializationError.missingCommandPluginProtocolConformance(protocolName:)](./missingcommandpluginprotocolconformance%28protocolname%29.md)
  The plugin doesn’t conform to the CommandPlugin protocol.
- [PluginDeserializationError.missingXcodeProjectPluginSupport](./missingxcodeprojectpluginsupport.md)
  The plugin doesn’t support Xcode
- [PluginDeserializationError.malformedInputJSON(_:)](./malformedinputjson%28_%29.md)
  The input JSON is malformed in some way; the message provides more details.
- [PluginDeserializationError.internalError(_:)](./internalerror%28_%29.md)
  An internal error of some kind; the message provides more details.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/plugindeserializationerror/missingbuildtoolpluginprotocolconformance(protocolname:))*