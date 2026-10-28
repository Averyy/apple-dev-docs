---
url: "https://docs.swift.org/latest/documentation/packageplugin/command/prebuildcommand(displayname:executable:arguments:environment:outputfilesdirectory:)-swift.type.method"
framework: "Swift-Org/PackagePlugin"
---

# prebuildCommand(displayName:executable:arguments:environment:outputFilesDirectory:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Type Method

Returns a command that runs unconditionally before every build.

**Availability**:
- SwiftPM - Deprecated in 6.0

> **Deprecated**: Use [`Command.prebuildCommand(displayName:executable:arguments:environment:outputFilesDirectory:)`](./prebuildcommand%28displayname,executable,arguments,environment,outputfilesdirectory%29-swift.enum.case.md) instead.

## Declaration

```swift
static func prebuildCommand(displayName: String?, executable: Path, arguments: [CustomStringConvertible], environment: [String : CustomStringConvertible] = [:], outputFilesDirectory: Path) -> Command
```

## Discussion

Prebuild commands can have a significant performance impact and should only be used when there would be no way to know the list of output file paths without first reading the contents of one or more input files. Typically there is no way to determine this list without first running the command, so instead of encoding that list, the caller supplies an `outputFilesDirectory` parameter, and all files in that directory after the command runs are treated as output files.

## Parameters

- `displayName`: An optional string to show in build logs and other status areas.
- `executable`: The absolute path to the executable to invoke.
- `arguments`: The command-line arguments for the executable.
- `environment`: Any environment variable assignments visible to the executable.
- `outputFilesDirectory`: A directory into which the command writes its output files.  Any files there recognizable by their extension as source files (for example, `.swift`) are compiled into the target for which this command was generated as if in its source directory; other files are treated as resources as if explicitly listed in `Package.swift` using `.process(...)`.

## See Also

### Types of Build Commands
- [case buildCommand(displayName: String?, executable: URL, arguments: [String], environment: [String : String], inputFiles: [URL], outputFiles: [URL])](./buildcommand%28displayname,executable,arguments,environment,inputfiles,outputfiles%29-swift.enum.case.md)
  Returns a command that runs when any of its output files are needed by the build and are out-of-date.
- [case prebuildCommand(displayName: String?, executable: URL, arguments: [String], environment: [String : String], outputFilesDirectory: URL)](./prebuildcommand%28displayname,executable,arguments,environment,outputfilesdirectory%29-swift.enum.case.md)
  Returns a command that runs unconditionally before every build.
- [static func buildCommand(displayName: String?, executable: Path, arguments: [CustomStringConvertible], environment: [String : CustomStringConvertible], inputFiles: [Path], outputFiles: [Path]) -> Command](./buildcommand%28displayname,executable,arguments,environment,inputfiles,outputfiles%29-swift.type.method.md)
  Returns a command that runs when any of its output files are needed by the build and are out-of-date.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/command/prebuildcommand(displayname:executable:arguments:environment:outputfilesdirectory:)-swift.type.method)*