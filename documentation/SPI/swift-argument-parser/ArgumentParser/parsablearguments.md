---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments"
framework: "swift-argument-parser/ArgumentParser"
---

# ParsableArguments

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: protocol  
**Role**: Protocol

A type that can be parsed from a program’s command-line arguments.

## Declaration

```swift
protocol ParsableArguments : _SendableMetatype, Decodable
```

## Mentions

- [Defining Commands and Subcommands](./commandsandsubcommands.md)
- [Customizing Help](./customizinghelp.md)
- [Manual Parsing and Testing](./manualparsing.md)
- [Providing Custom Validation](./validation.md)

#### Overview

When you implement a `ParsableArguments` type, all properties must be declared with one of the four property wrappers provided by the `ArgumentParser` library.

## Topics

### Handling Validation
- [func validate() throws](./parsablearguments/validate%28%29.md)
  Validates the properties of the instance after parsing.
### Parsing a Type
- [static func parse([String]?) throws -> Self](./parsablearguments/parse%28_%29.md)
  Parses a new instance of this type from command-line arguments.
- [static func parseOrExit([String]?) -> Self](./parsablearguments/parseorexit%28_%29.md)
  Parses a new instance of this type from command-line arguments or exits with a relevant message.
### Exiting a Program
- [static func exit(withError: (any Error)?) -> Never](./parsablearguments/exit%28witherror%29.md)
  Terminates execution with a message and exit code that is appropriate for the given error.
### Generating Help Text
- [static func helpMessage(includeHidden: Bool, columns: Int?) -> String](./parsablearguments/helpmessage%28includehidden,columns%29.md)
  Returns the text of the help screen for this type.
### Handling Errors
- [static func message(for: any Error) -> String](./parsablearguments/message%28for%29.md)
  Returns a brief message for the given error.
- [static func fullMessage(for: any Error, columns: Int?) -> String](./parsablearguments/fullmessage%28for,columns%29.md)
  Returns a full message for the given error, including usage information, if appropriate.
- [static func exitCode(for: any Error) -> ExitCode](./parsablearguments/exitcode%28for%29.md)
  Returns the exit code for the given error.
### Generating Completion Scripts
- [static func completionScript(for: CompletionShell) -> String](./parsablearguments/completionscript%28for%29.md)
  Returns a shell completion script for the specified shell.
- [struct CompletionShell](./completionshell.md)
  A shell for which the parser can generate a completion script.
### Infrequently Used APIs
- [init()](./parsablearguments/init%28%29.md)
  Creates an instance of this parsable type using the definitions given by each property’s wrapper.
### Type Methods
- [static func helpMessage(columns: Int?) -> String](./parsablearguments/helpmessage%28columns%29.md)
  Returns the text of the help screen for this type.
- [static func usageString(includeHidden: Bool) -> String](./parsablearguments/usagestring%28includehidden%29.md)
  Returns the usage text for this type.

## Relationships

### Inherits From
- Swift.Decodable
- Swift.SendableMetatype
### Inherited By
- [AsyncParsableCommand](./asyncparsablecommand.md)
- [ParsableCommand](./parsablecommand.md)

## See Also

### Arguments, Options, and Flags
- [Declaring Arguments, Options, and Flags](./declaringarguments.md)
  Use the `@Argument`, `@Option` and `@Flag` property wrappers to declare the command-line interface for your command.
- [struct Argument](./argument.md)
  A property wrapper that represents a positional command-line argument.
- [struct Option](./option.md)
  A property wrapper that represents a command-line option.
- [struct Flag](./flag.md)
  A property wrapper that represents a command-line flag.
- [struct OptionGroup](./optiongroup.md)
  A wrapper that transparently includes a parsable type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments)*