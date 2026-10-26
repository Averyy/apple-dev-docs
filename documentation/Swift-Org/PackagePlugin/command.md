---
url: "https://docs.swift.org/latest/documentation/packageplugin/command"
framework: "Swift-Org/PackagePlugin"
---

# Command

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

A command to run during the build.

## Declaration

```swift
enum Command
```

#### Overview

A command includes the executable, command lines, environment variables, initial working directory, and so on. All paths should be based on the ones that SwiftPM passes to the plugin in the target build context.

## Topics

### Types of Build Commands
- [case buildCommand(displayName: String?, executable: URL, arguments: [String], environment: [String : String], inputFiles: [URL], outputFiles: [URL])](./command/buildcommand%28displayname,executable,arguments,environment,inputfiles,outputfiles%29-swift.enum.case.md)
  Returns a command that runs when any of its output files are needed by the build and are out-of-date.
- [case prebuildCommand(displayName: String?, executable: URL, arguments: [String], environment: [String : String], outputFilesDirectory: URL)](./command/prebuildcommand%28displayname,executable,arguments,environment,outputfilesdirectory%29-swift.enum.case.md)
  Returns a command that runs unconditionally before every build.
- [static func buildCommand(displayName: String?, executable: Path, arguments: [CustomStringConvertible], environment: [String : CustomStringConvertible], inputFiles: [Path], outputFiles: [Path]) -> Command](./command/buildcommand%28displayname,executable,arguments,environment,inputfiles,outputfiles%29-swift.type.method.md)
  Returns a command that runs when any of its output files are needed by the build and are out-of-date.
- [static func prebuildCommand(displayName: String?, executable: Path, arguments: [CustomStringConvertible], environment: [String : CustomStringConvertible], outputFilesDirectory: Path) -> Command](./command/prebuildcommand%28displayname,executable,arguments,environment,outputfilesdirectory%29-swift.type.method.md)
  Returns a command that runs unconditionally before every build.

## See Also

### Implementing Build Plugins
- [protocol BuildToolPlugin](./buildtoolplugin.md)
  The plugin protocol that defines functionality for all plugins having a buildTool capability.
- [struct PluginContext](./plugincontext.md)
  A collection of information about the package on which the package manager invokes the  plugin, as well as contextual information based on the plugin’s intent and requirements.
- [protocol Target](./target.md)
  A single target defined in a package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/command)*