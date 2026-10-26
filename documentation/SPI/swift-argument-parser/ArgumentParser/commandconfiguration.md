---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration"
framework: "swift-argument-parser/ArgumentParser"
---

# CommandConfiguration

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

The configuration for a command.

## Declaration

```swift
struct CommandConfiguration
```

## Mentions

- [Customizing Help for Commands](./customizingcommandhelp.md)

## Topics

### Creating a Configuration
- [init(commandName: String?, abstract: String, usage: String?, discussion: String, helpBanner: String?, version: String, shouldDisplay: Bool, subcommands: [any ParsableCommand.Type], groupedSubcommands: [CommandGroup], defaultSubcommand: (any ParsableCommand.Type)?, helpNames: NameSpecification?, aliases: [String])](./commandconfiguration/init%28commandname,abstract,usage,discussion,helpbanner,version,shoulddisplay,subcommands,groupedsubcommands,defaultsubcommand,helpnames,aliases%29.md)
  Creates the configuration for a command.
### Customizing the Help Screen
- [var abstract: String](./commandconfiguration/abstract.md)
  A one-line description of this command.
- [var discussion: String](./commandconfiguration/discussion.md)
  A longer description of this command, to be shown in the extended help display.
- [var usage: String?](./commandconfiguration/usage.md)
  A customized usage string to be shown in the help display and error messages.
- [var helpBanner: String?](./commandconfiguration/helpbanner.md)
  A banner shown at the top of the help display for this command and, unless overridden, all of its subcommands.
- [var helpNames: NameSpecification?](./commandconfiguration/helpnames.md)
  Flag names to be used for help.
### Declaring Subcommands
- [var subcommands: [any ParsableCommand.Type]](./commandconfiguration/subcommands.md)
  An array of the types that define subcommands for this command.
- [var defaultSubcommand: (any ParsableCommand.Type)?](./commandconfiguration/defaultsubcommand.md)
  The default command type to run if no subcommand is given.
### Defining Command Properties
- [var commandName: String?](./commandconfiguration/commandname.md)
  The name of the command to use on the command line.
- [var version: String](./commandconfiguration/version.md)
  Version information for this command.
- [var shouldDisplay: Bool](./commandconfiguration/shoulddisplay.md)
  A Boolean value indicating whether this command should be shown in the extended help display.
- [var aliases: [String]](./commandconfiguration/aliases.md)
  An array of aliases for the command’s name.
### Instance Properties
- [var groupedSubcommands: [CommandGroup]](./commandconfiguration/groupedsubcommands.md)
  The list of subcommands and subcommand groups.
- [var ungroupedSubcommands: [any ParsableCommand.Type]](./commandconfiguration/ungroupedsubcommands.md)
  An array of types that define subcommands for this command and are not part of any command group.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Customizing a Command
- [static var configuration: CommandConfiguration](./parsablecommand/configuration.md)
  Configuration for this command, including subcommands and custom help text.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration)*