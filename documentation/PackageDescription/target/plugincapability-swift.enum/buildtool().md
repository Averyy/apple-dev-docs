# buildTool()

**Framework**: PackageDescription  
**Kind**: method  
**Role**: Type Method

The plug-in is a build tool.

**Availability**:
- SwiftPM 5.5+

## Declaration

```swift
static func buildTool() -> Target.PluginCapability
```

#### Return Value

A plug-in capability that defines a build tool.

#### Discussion

The plug-in to apply to each target that uses it, and creates commands that run before or during the build of the target.

## See Also

### Creating a Plugin Capability
- [case command(intent: PluginCommandIntent, permissions: [PluginPermission])](./command%28intent,permissions%29.md)
  Specifies that the plug-in provides a user command capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugincapability-swift.enum/buildtool())*