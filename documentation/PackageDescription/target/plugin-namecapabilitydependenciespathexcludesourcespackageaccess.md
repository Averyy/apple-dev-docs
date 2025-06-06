# plugin(name:capability:dependencies:path:exclude:sources:packageAccess:)

**Framework**: PackageDescription  
**Kind**: method

Defines a new package plug-in target.

**Availability**:
- SwiftPM 5.9+

## Declaration

```swift
static func plugin(name: String, capability: Target.PluginCapability, dependencies: [Target.Dependency] = [], path: String? = nil, exclude: [String] = [], sources: [String]? = nil, packageAccess: Bool = true) -> Target
```

#### Return Value

A `Target` instance.

#### Discussion

A plug-in target provides custom build commands to SwiftPM (and to any IDEs based on libSwiftPM).

The capability determines what kind of build commands it can add. Besides determining at what point in the build those commands run, the capability determines the context that is available to the plug-in and the kinds of commands it can create.

In the initial version of this proposal, three capabilities are provided: prebuild, build tool, and postbuild. For more information, see the declaration of each capability under [`Target.PluginCapability`](target/plugincapability-swift.enum.md).

The package plug-in itself is implemented using a Swift script that is invoked for each target that uses it. The script is invoked after the package graph has been resolved, but before the build system creates its dependency graph. It’s also invoked after changes to the target or the build parameters.

Note that the role of the package plug-in is only to define the commands that run before, during, or after the build. It doesn’t run those commands itself. The commands are defined in an IDE-neutral way, and are run as appropriate by the build system that builds the package. The extension itself is only a procedural way of generating commands and their input and output dependencies.

The package plug-in may specify the executable or binary targets that provide the build tools used by the generated commands during the build. In the initial implementation, prebuild actions can only depend on binary targets. Build tool and postbuild plug-ins can depend on executables as well as binary targets. This is due to how Swift Package Manager constructs its build plan.

## Parameters

- `name`: The name of the plug-in target.
- `capability`: The type of capability the plug-in target provides.
- `dependencies`: The plug-in target’s dependencies.
- `path`: The path of the plug-in target relative to the package root.
- `exclude`: The paths to source and resource files that you want to exclude from the plug-in target.
- `sources`: The source files in the plug-in target.
- `packageAccess`: Allows access to package symbols from other targets in the package.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/target/plugin(name:capability:dependencies:path:exclude:sources:packageaccess:))*