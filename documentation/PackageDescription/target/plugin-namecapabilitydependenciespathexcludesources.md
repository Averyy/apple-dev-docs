# plugin(name:capability:dependencies:path:exclude:sources:)

**Framework**: PackageDescription  
**Kind**: method

Defines a new package plugin target.

## Declaration

```swift
static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency] = [], path: String? = nil, exclude: [String] = [], sources: [String]? = nil) -> Target
```

#### Return Value

A `Target` instance.

#### Discussion

A plugin target provides custom build commands to SwiftPM (and to any IDEs based on libSwiftPM).

The capability determines what kind of build commands it can add. Besides determining at what point in the build those commands run, the capability determines the context that is available to the plugin and the kinds of commands it can create.

In the initial version of this proposal, three capabilities are provided: prebuild, build tool, and postbuild. See the declaration of each capability under [`Target.PluginCapability`](target/plugincapability-swift.enum.md) for more information.

The package plugin itself is implemented using a Swift script that is invoked for each target that uses it. The script is invoked after the package graph has been resolved, but before the build system creates its dependency graph. It is also invoked after changes to the target or the build parameters.

Note that the role of the package plugin is only to define the commands that will run before, during, or after the build. It does not itself run those commands. The commands are defined in an IDE-neutral way, and are run as appropriate by the build system that builds the package. The extension itself is only a procedural way of generating commands and their input and output dependencies.

The package plugin may specify the executable targets or binary targets that provide the build tools that will be used by the generated commands during the build. In the initial implementation, prebuild actions can only depend on binary targets. Build tool and postbuild plugins can depend on executables as well as binary targets. This is due to how Swift Package Manager constructs its build plan.

## Parameters

- `name`: The name of the plugin target.
- `capability`: The type of capability the plugin target provides.
- `dependencies`: The plugin target’s dependencies.
- `path`: The path of the plugin target, relative to the package root.
- `exclude`: The paths to source and resource files that you want to exclude from the plug-in target.
- `sources`: The source files in the plug-in target.

## See Also

- [static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency], path: String?, exclude: [String], sources: [String]?, packageAccess: Bool) -> Target](target/plugin(name:capability:dependencies:path:exclude:sources:packageaccess:).md)
  Defines a new package plug-in target.
- [var pluginCapability: Target.PluginCapability?](target/plugincapability-swift.property.md)
  The capability provided by a package plug-in target.
- [Target.PluginCapability](target/plugincapability-swift.enum.md)
  The different types of capability that a plug-in can provide.
- [enum PluginCommandIntent](plugincommandintent.md)
  The intended use case of the command plug-in.
- [enum PluginPermission](pluginpermission.md)
  The type of permission a plug-in requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugin(name:capability:dependencies:path:exclude:sources:))*