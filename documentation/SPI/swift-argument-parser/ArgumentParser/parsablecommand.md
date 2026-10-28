---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand"
framework: "swift-argument-parser/ArgumentParser"
---

# ParsableCommand

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: protocol  
**Role**: Protocol

A type that can be executed as part of a nested tree of commands.

## Declaration

```swift
protocol ParsableCommand : ParsableArguments
```

## Mentions

- [Manual Parsing and Testing](./manualparsing.md)
- [Providing Custom Validation](./validation.md)

## Overview

`ParsableCommand` types are the basic building blocks for command-line tools built using `ArgumentParser`. To create a command, declare properties using the `@Argument`, `@Option`, and `@Flag` property wrappers, or include groups of options with `@OptionGroup`. Finally, implement your command’s functionality in the [`run()`](./parsablecommand/run%28%29.md) method.

```swift
@main
struct Repeat: ParsableCommand {
    @Argument(help: "The phrase to repeat.")
    var phrase: String

    @Option(help: "The number of times to repeat 'phrase'.")
    var count: Int? = nil

    mutating func run() throws {
        let repeatCount = count ?? 2
        for _ in 0..<repeatCount {
            print(phrase)
        }
    }
}
```

> **Note**: The Swift compiler uses either the type marked with `@main` or a `main.swift` file as the entry point for an executable program. You can use either one, but not both — rename your `main.swift` file to the name of the command when you add `@main`.

## Topics

### Essentials
- [Defining Commands and Subcommands](./commandsandsubcommands.md)
  Break complex command-line tools into a tree of subcommands.
- [Customizing Help for Commands](./customizingcommandhelp.md)
  Define your command’s abstract, extended discussion, or usage string, and set the flags used to invoke the help display.
### Implementing a Command’s Behavior
- [func run() throws](./parsablecommand/run%28%29.md)
  The behavior or functionality of this command.
- [func validate() throws](./parsablearguments/validate%28%29.md)
  Validates the properties of the instance after parsing.
### Customizing a Command
- [static var configuration: CommandConfiguration](./parsablecommand/configuration.md)
  Configuration for this command, including subcommands and custom help text.
- [struct CommandConfiguration](./commandconfiguration.md)
  The configuration for a command.
### Generating Help Text
- [static func helpMessage(for: ParsableCommand.Type, includeHidden: Bool, columns: Int?) -> String](./parsablecommand/helpmessage%28for,includehidden,columns%29.md)
  Returns the text of the help screen for the given subcommand of this command.
### Starting the Program
- [static func main()](./parsablecommand/main%28%29.md)
  Executes this command, or one of its subcommands, with the program’s command-line arguments.
- [static func main([String]?)](./parsablecommand/main%28_%29.md)
  Executes this command, or one of its subcommands, with the given arguments.
### Manually Parsing Input
- [static func parseAsRoot([String]?) throws -> ParsableCommand](./parsablecommand/parseasroot%28_%29.md)
  Parses an instance of this type, or one of its subcommands, from command-line arguments.
### Type Methods
- [static func helpMessage(for: ParsableCommand.Type, columns: Int?) -> String](./parsablecommand/helpmessage%28for,columns%29.md)
  Returns the text of the help screen for the given subcommand of this command.
- [static func usageString(for: ParsableCommand.Type, includeHidden: Bool) -> String](./parsablecommand/usagestring%28for,includehidden%29.md)
  Returns the usage text for the given subcommand of this command.

## Relationships

### Inherits From
- [ParsableArguments](./parsablearguments.md)
- Swift.Decodable
- Swift.SendableMetatype
### Inherited By
- [AsyncParsableCommand](./asyncparsablecommand.md)

## See Also

### Essentials
- [Using ArgumentParser Tools](./usingargumentparsertools.md)
  Learn how to provide input to command-line tools built with `ArgumentParser`.
- [Getting Started with ArgumentParser](./gettingstarted.md)
  Learn to set up and customize a simple command-line tool.
- [protocol AsyncParsableCommand](./asyncparsablecommand.md)
  A type that can be executed asynchronously, as part of a nested tree of commands.
- [Defining Commands and Subcommands](./commandsandsubcommands.md)
  Break complex command-line tools into a tree of subcommands.
- [Customizing Help for Commands](./customizingcommandhelp.md)
  Define your command’s abstract, extended discussion, or usage string, and set the flags used to invoke the help display.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand)*