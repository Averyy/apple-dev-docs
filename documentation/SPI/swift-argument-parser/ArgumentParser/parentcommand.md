---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parentcommand"
framework: "swift-argument-parser/ArgumentParser"
---

# ParentCommand

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A wrapper that adds a reference to a parent command.

## Declaration

```swift
@propertyWrapper
struct ParentCommand<Value> where Value : ParsableCommand
```

## Overview

Use the `@ParentCommand` wrapper to gain access to a parent command’s state.

The arguments, options, and flags in a `@ParentCommand` type are omitted from the help screen for the including child command, and only appear in the parent’s help screen. To include the help in both screens, use the [`OptionGroup`](./optiongroup.md) wrapper instead.

```swift
struct SuperCommand: ParsableCommand {
    static let configuration = CommandConfiguration(
        subcommands: [SubCommand.self]
    )

    @Flag(name: .shortAndLong)
    var verbose: Bool = false
}

struct SubCommand: ParsableCommand {
    @ParentCommand var parent: SuperCommand

    mutating func run() throws {
        if self.parent.verbose {
            print("Verbose")
        }
    }
}
```

## Topics

### Initializers
- [init()](./parentcommand/init%28%29.md)
### Instance Properties
- [var wrappedValue: Value](./parentcommand/wrappedvalue.md)
### Default Implementations
- [CustomStringConvertible Implementations](./parentcommand/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Decodable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parentcommand)*