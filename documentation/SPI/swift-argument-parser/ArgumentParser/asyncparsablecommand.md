---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand"
framework: "swift-argument-parser/ArgumentParser"
---

# AsyncParsableCommand

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: protocol  
**Role**: Protocol

A type that can be executed asynchronously, as part of a nested tree of commands.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
protocol AsyncParsableCommand : ParsableCommand
```

## Mentions

- [Providing Custom Validation](./validation.md)

## Overview

To use `async`/`await` code in your commands’ `run()` method implementations, follow these steps:

1. For the root command in your command-line tool, declare conformance to `AsyncParsableCommand`, whether or not that command uses asynchronous code.
2. Apply the `@main` attribute to the root command. (Note: If your root command is in a `main.swift` file, rename the file to the name of the command.)
3. For any command that needs to use asynchronous code, declare conformance to `AsyncParsableCommand` and mark the `run()` method as `async`. No changes are needed for subcommands that don’t use asynchronous code.

The following example declares a `CountLines` command that uses Foundation’s asynchronous `FileHandle.AsyncBytes` to read the lines from a file:

```swift
import Foundation

@main
struct CountLines: AsyncParsableCommand {
    @Argument(transform: URL.init(fileURLWithPath:))
    var inputFile: URL

    mutating func run() async throws {
        let fileHandle = try FileHandle(forReadingFrom: inputFile)
        let lineCount = try await fileHandle.bytes.lines.reduce(into: 0) 
            { count, _ in count += 1 }
        print(lineCount)
    }
}
```

> **Note**: The Swift compiler uses either the type marked with `@main` or a `main.swift` file as the entry point for an executable program. You can use either one, but not both — rename your `main.swift` file to the name of the command when you add `@main`.

### Usage in Swift 5.5

Swift 5.5 is supported by the obsolete versions 1.1.x & 1.2.x versions of Swift Argument Parser.

In Swift 5.5, an asynchronous `@main` entry point must be declared as a separate standalone type.

Your root command cannot be designated as `@main`, unlike as described above.

Instead, use the code snippet below, replacing the `<#RootCommand#>` placeholder with the name of your own root command.

```swift
@main struct AsyncMain: AsyncMainProtocol {
    typealias Command = <#RootCommand#>
}
```

Continue to follow the other steps above to use `async`/`await` code within your commands’ `run()` methods.

## Topics

### Implementing a Command’s Behavior
- [func run() async throws](./asyncparsablecommand/run%28%29.md)
  The behavior or functionality of this command.
### Starting the Program
- [static func main() async](./asyncparsablecommand/main%28%29.md)
  Executes this command, or one of its subcommands, with the program’s command-line arguments.
- [protocol AsyncMainProtocol](./asyncmainprotocol.md)
  A type that can designate an `AsyncParsableCommand` as the program’s entry point.
### Type Methods
- [static func asyncParse([String]?) async throws -> Self](./asyncparsablecommand/asyncparse%28_%29.md)
  Parses a new instance of this type from command-line arguments.
- [static func asyncParseAsRoot([String]?) async throws -> ParsableCommand](./asyncparsablecommand/asyncparseasroot%28_%29.md)
  Parses an instance of this type, or one of its subcommands, from command-line arguments.
- [static func main([String]?) async](./asyncparsablecommand/main%28_%29.md)
  Executes this command, or one of its subcommands, with the given arguments.

## Relationships

### Inherits From
- [ParsableArguments](./parsablearguments.md)
- [ParsableCommand](./parsablecommand.md)
- Swift.Decodable
- Swift.SendableMetatype

## See Also

### Essentials
- [Using ArgumentParser Tools](./usingargumentparsertools.md)
  Learn how to provide input to command-line tools built with `ArgumentParser`.
- [Getting Started with ArgumentParser](./gettingstarted.md)
  Learn to set up and customize a simple command-line tool.
- [protocol ParsableCommand](./parsablecommand.md)
  A type that can be executed as part of a nested tree of commands.
- [Defining Commands and Subcommands](./commandsandsubcommands.md)
  Break complex command-line tools into a tree of subcommands.
- [Customizing Help for Commands](./customizingcommandhelp.md)
  Define your command’s abstract, extended discussion, or usage string, and set the flags used to invoke the help display.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand)*