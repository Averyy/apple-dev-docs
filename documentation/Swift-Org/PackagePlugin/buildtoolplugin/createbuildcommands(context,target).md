---
url: "https://docs.swift.org/latest/documentation/packageplugin/buildtoolplugin/createbuildcommands(context:target:)"
framework: "Swift-Org/PackagePlugin"
---

# createBuildCommands(context:target:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked by the package manager to create build commands for a particular target.

## Declaration

```swift
func createBuildCommands(context: PluginContext, target: Target) async throws -> [Command]
```

#### Discussion

The context parameter contains information about the package and its dependencies, as well as other environmental inputs.

This function should create and return build commands or prebuild commands, configured based on the information in the context. Note that the plugin does not directly run those commands.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/buildtoolplugin/createbuildcommands(context:target:))*