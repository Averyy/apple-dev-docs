---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/optiongroup"
framework: "swift-argument-parser/ArgumentParser"
---

# OptionGroup

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A wrapper that transparently includes a parsable type.

## Declaration

```swift
@propertyWrapper
struct OptionGroup<Value> where Value : ParsableArguments
```

## Mentions

- [Defining Commands and Subcommands](./commandsandsubcommands.md)

## Overview

Use an option group to include a group of options, flags, or arguments declared in a parsable type.

```swift
struct GlobalOptions: ParsableArguments {
    @Flag(name: .shortAndLong)
    var verbose: Bool = false

    @Argument var values: [Int]
}

struct Options: ParsableArguments {
    @Option var name: String
    @OptionGroup var globals: GlobalOptions
}
```

The flag and positional arguments declared as part of `GlobalOptions` are included when parsing `Options`.

## Topics

### Creating an Option Group
- [init(title: String, visibility: ArgumentVisibility)](./optiongroup/init%28title,visibility%29.md)
  Creates a property that represents another parsable type, using the specified title and visibility.
### Option Group Properties
- [var title: String](./optiongroup/title.md)
  The title to use in the help screen for this option group.
### Infrequently Used APIs
- [init()](./optiongroup/init%28%29.md)
  Creates a property that represents another parsable type.
- [var wrappedValue: Value](./optiongroup/wrappedvalue.md)
  The value presented by this property wrapper.
- [var description: String](./optiongroup/description.md)
### Default Implementations
- [CustomStringConvertible Implementations](./optiongroup/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Decodable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

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
- [protocol ParsableArguments](./parsablearguments.md)
  A type that can be parsed from a program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/optiongroup)*