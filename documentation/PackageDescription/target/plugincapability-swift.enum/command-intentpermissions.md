# Target.PluginCapability.command(intent:permissions:)

**Framework**: PackageDescription  
**Kind**: case

Specifies that the plug-in provides a user command capability.

**Availability**:
- SwiftPM 5.6+

## Declaration

```swift
case command(intent: PluginCommandIntent, permissions: [PluginPermission] = [])
```

#### Discussion

Plug-ins that specify a `command` capability define commands that can run using the SwiftPM command line interface, or in an IDE that supports Swift packages. You can invoke the command manually on one or more targets in a package.

```swift
swift package <verb>
```

The package can specify the  used to invoke the command.

## Parameters

- `intent`: The semantic intent of the plug-in; either one of the predefined intents,   or a custom intent.
- `permissions`: Any permissions needed by the command plug-in. This affects what the   sandbox in which the plug-in is run allows. Some permissions may require   user approval.

## See Also

- [static func buildTool() -> Target.PluginCapability](target/plugincapability-swift.enum/buildtool.md)
  The plug-in is a build tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugincapability-swift.enum/command(intent:permissions:))*