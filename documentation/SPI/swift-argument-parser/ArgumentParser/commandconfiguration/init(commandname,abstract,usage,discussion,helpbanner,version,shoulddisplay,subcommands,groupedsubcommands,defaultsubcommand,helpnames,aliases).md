---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/init(commandname:abstract:usage:discussion:helpbanner:version:shoulddisplay:subcommands:groupedsubcommands:defaultsubcommand:helpnames:aliases:)"
framework: "swift-argument-parser/ArgumentParser"
---

# init(commandName:abstract:usage:discussion:helpBanner:version:shouldDisplay:subcommands:groupedSubcommands:defaultSubcommand:helpNames:aliases:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates the configuration for a command.

## Declaration

```swift
init(commandName: String? = nil, abstract: String = "", usage: String? = nil, discussion: String = "", helpBanner: String? = nil, version: String = "", shouldDisplay: Bool = true, subcommands ungroupedSubcommands: [ParsableCommand.Type] = [], groupedSubcommands: [CommandGroup] = [], defaultSubcommand: ParsableCommand.Type? = nil, helpNames: NameSpecification? = nil, aliases: [String] = [])
```

## Parameters

- `commandName`: The name of the command to use on the command line. If `commandName` is `nil`, the command name is derived by converting the name of the command type to hyphen-separated lowercase words.
- `abstract`: A one-line description of the command.
- `usage`: A custom usage description for the command. When you provide a non-`nil` string, the argument parser uses `usage` instead of automatically generating a usage description. Passing an empty string hides the usage string altogether.
- `discussion`: A longer description of the command.
- `helpBanner`: A banner shown at the top of the help display for this command and, unless overridden, all of its subcommands. When `helpBanner` is `nil`, the banner is inherited from the nearest ancestor command that specifies one. Pass the empty string to suppress an inherited banner.
- `version`: The version number for this command. When you provide a non-empty string, the argument parser prints it if the user provides a `--version` flag.
- `shouldDisplay`: A Boolean value indicating whether the command should be shown in the extended help display.
- `ungroupedSubcommands`: An array of the types that define subcommands for the command that are not part of any command group.
- `groupedSubcommands`: An array of command groups, each of which defines subcommands that are part of that logical group.
- `defaultSubcommand`: The default command type to run if no subcommand is given.
- `helpNames`: The flag names to use for requesting help, when combined with a simulated Boolean property named `help`. If `helpNames` is `nil`, the names are inherited from the parent command, if any, or are `-h` and `--help`.
- `aliases`: An array of aliases for the command’s name. All of the aliases MUST not match the actual command name, whether that be the derived name if `commandName` is not provided, or `commandName` itself if provided.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/init(commandname:abstract:usage:discussion:helpbanner:version:shoulddisplay:subcommands:groupedsubcommands:defaultsubcommand:helpnames:aliases:))*