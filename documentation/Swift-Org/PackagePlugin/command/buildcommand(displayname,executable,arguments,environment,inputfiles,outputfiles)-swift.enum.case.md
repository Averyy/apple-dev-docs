---
url: "https://docs.swift.org/latest/documentation/packageplugin/command/buildcommand(displayname:executable:arguments:environment:inputfiles:outputfiles:)-swift.enum.case"
framework: "Swift-Org/PackagePlugin"
---

# Command.buildCommand(displayName:executable:arguments:environment:inputFiles:outputFiles:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: case  
**Role**: Case

Returns a command that runs when any of its output files are needed by the build and are out-of-date.

**Availability**:
- SwiftPM 6.0+

## Declaration

```swift
case buildCommand(displayName: String?, executable: URL, arguments: [String], environment: [String : String] = [:], inputFiles: [URL] = [], outputFiles: [URL] = [])
```

## Discussion

An output file is out-of-date if it doesn’t exist, or if any input files have changed since the command was last run.

> **Note**: The paths in the list of output files may depend on the list of input file paths, but **must not** depend on reading the contents of any input files. Use a `prebuildCommand`if the functionality of your plugin requires you to read the contents of an input file.

## Parameters

- `displayName`: An optional string to show in build logs and other status areas.
- `executable`: The absolute path to the executable to invoke.
- `arguments`: The command-line arguments for the executable.
- `environment`: Any environment variable assignments visible to the executable.
- `inputFiles`: A list of files on which the contents of output files may depend. Any paths passed as `arguments` should typically be passed here as well.
- `outputFiles`: A list of files to be generated or updated by the executable. Any files recognizable by their extension as source files (for example, `.swift`) are compiled into the target for which this command was generated as if in its source directory; other files are treated as resources as if explicitly listed in `Package.swift` using `.process(...)`.

## See Also

### Types of Build Commands
- [case prebuildCommand(displayName: String?, executable: URL, arguments: [String], environment: [String : String], outputFilesDirectory: URL)](./prebuildcommand%28displayname,executable,arguments,environment,outputfilesdirectory%29-swift.enum.case.md)
  Returns a command that runs unconditionally before every build.
- [static func buildCommand(displayName: String?, executable: Path, arguments: [CustomStringConvertible], environment: [String : CustomStringConvertible], inputFiles: [Path], outputFiles: [Path]) -> Command](./buildcommand%28displayname,executable,arguments,environment,inputfiles,outputfiles%29-swift.type.method.md)
  Returns a command that runs when any of its output files are needed by the build and are out-of-date.
- [static func prebuildCommand(displayName: String?, executable: Path, arguments: [CustomStringConvertible], environment: [String : CustomStringConvertible], outputFilesDirectory: Path) -> Command](./prebuildcommand%28displayname,executable,arguments,environment,outputfilesdirectory%29-swift.type.method.md)
  Returns a command that runs unconditionally before every build.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/command/buildcommand(displayname:executable:arguments:environment:inputfiles:outputfiles:)-swift.enum.case)*