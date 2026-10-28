---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument"
framework: "swift-argument-parser/ArgumentParser"
---

# Argument

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A property wrapper that represents a positional command-line argument.

## Declaration

```swift
@propertyWrapper
struct Argument<Value>
```

## Mentions

- [Declaring Arguments, Options, and Flags](./declaringarguments.md)

## Overview

Use the `@Argument` wrapper to define a property of your custom command as a positional argument. A *positional argument* for a command-line tool is specified without a label and must appear in declaration order. `@Argument` properties with `Optional` type or a default value are optional for the user of your command-line tool.

For example, the following program has two positional arguments. The `name` argument is required, while `greeting` is optional because it has a default value.

```swift
@main
struct Greet: ParsableCommand {
    @Argument var name: String
    @Argument var greeting: String = "Hello"

    mutating func run() {
        print("\(greeting) \(name)!")
    }
}
```

You can call this program with just a name or with a name and a greeting. When you supply both arguments, the first argument is always treated as the name, due to the order of the property declarations.

```
$ greet Nadia
Hello Nadia!
$ greet Tamara Hi
Hi Tamara!
```

## Topics

### Single Arguments
- [init(help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28help,completion%29-6pqzn.md)
  Creates a property with no default value.
- [init<T>(help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28help,completion%29-4p94d.md)
  Creates an optional property that reads its value from an argument.
- [init(help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> Value)](./argument/init%28help,completion,transform%29-3fjtc.md)
  Creates a property with no default value, parsing with the given closure.
- [init<T>(help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./argument/init%28help,completion,transform%29-7yn32.md)
  Creates an optional property that reads its value from an argument.
- [init(wrappedValue: Value, help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28wrappedvalue,help,completion%29-9yifn.md)
  Creates a property with a default value provided by standard Swift default value syntax.
- [init(wrappedValue: Value, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> Value)](./argument/init%28wrappedvalue,help,completion,transform%29-667t1.md)
  Creates a property with a default value provided by standard Swift default value syntax, parsing with the given closure.
### Array Arguments
- [init<T>(parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28parsing,help,completion%29.md)
  Creates a property with no default value that reads an array from zero or more arguments.
- [init<T>(parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./argument/init%28parsing,help,completion,transform%29.md)
  Creates a property with no default value that reads an array from zero or more arguments, parsing each element with the given closure.
- [init<T>(wrappedValue: [T], parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28wrappedvalue,parsing,help,completion%29.md)
  Creates a property that reads an array from zero or more arguments.
- [init<T>(wrappedValue: [T], parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./argument/init%28wrappedvalue,parsing,help,completion,transform%29.md)
  Creates a property that reads an array from zero or more arguments, parsing each element with the given closure.
- [struct ArgumentArrayParsingStrategy](./argumentarrayparsingstrategy.md)
  The strategy to use when parsing multiple values from positional arguments into an array.
### Infrequently Used APIs
- [var wrappedValue: Value](./argument/wrappedvalue.md)
  The value presented by this property wrapper.
### Initializers
- [init<T>(wrappedValue: _OptionalNilComparisonType, help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28wrappedvalue,help,completion%29-1rfjo.md)
  This initializer allows a user to provide a `nil` default value for an optional `@Argument`-marked property without allowing a non-`nil` default value.
- [init<T>(wrappedValue: _OptionalNilComparisonType, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./argument/init%28wrappedvalue,help,completion,transform%29-84qu9.md)
  This initializer allows a user to provide a `nil` default value for an optional `@Argument`-marked property without allowing a non-`nil` default value.
### Default Implementations
- [CustomStringConvertible Implementations](./argument/customstringconvertible-implementations.md)

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
- [struct Option](./option.md)
  A property wrapper that represents a command-line option.
- [struct Flag](./flag.md)
  A property wrapper that represents a command-line flag.
- [struct OptionGroup](./optiongroup.md)
  A wrapper that transparently includes a parsable type.
- [protocol ParsableArguments](./parsablearguments.md)
  A type that can be parsed from a program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument)*