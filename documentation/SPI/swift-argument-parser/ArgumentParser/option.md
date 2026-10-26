---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option"
framework: "swift-argument-parser/ArgumentParser"
---

# Option

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A property wrapper that represents a command-line option.

## Declaration

```swift
@propertyWrapper
struct Option<Value>
```

## Mentions

- [Declaring Arguments, Options, and Flags](./declaringarguments.md)

#### Overview

Use the `@Option` wrapper to define a property of your custom command as a command-line option. An *option* is a named value passed to a command-line tool, like `--configuration debug`. Options can be specified in any order.

An option can have a default value specified as part of its declaration; options with optional `Value` types implicitly have `nil` as their default value. Options that are neither declared as `Optional` nor given a default value are required for users of your command-line tool.

For example, the following program defines three options:

```swift
@main
struct Greet: ParsableCommand {
    @Option var greeting = "Hello"
    @Option var age: Int? = nil
    @Option var name: String

    mutating func run() {
        print("\(greeting) \(name)!")
        if let age {
            print("Congrats on making it to the ripe old age of \(age)!")
        }
    }
}
```

`greeting` has a default value of `"Hello"`, which can be overridden by providing a different string as an argument, while `age` defaults to `nil`. `name` is a required option because it is non-`nil` and has no default value.

```
$ greet --name Alicia
Hello Alicia!
$ greet --age 28 --name Seungchin --greeting Hi
Hi Seungchin!
Congrats on making it to the ripe old age of 28!
```

## Topics

### Single-Value Options
- [init(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28name,parsing,help,completion%29-4yske.md)
  Creates a required property that reads its value from a labeled option.
- [init<T>(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28name,parsing,help,completion%29-7slrf.md)
  Creates an optional property that reads its value from a labeled option.
- [init(wrappedValue: Value, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28wrappedvalue,name,parsing,help,completion%29-7ilku.md)
  Creates a property with a default value that reads its value from a labeled option.
- [init(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> Value)](./option/init%28name,parsing,help,completion,transform%29-2wf44.md)
  Creates a required property that reads its value from a labeled option, parsing with the given closure.
- [init<T>(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28name,parsing,help,completion,transform%29-25g7b.md)
  Creates an optional property that reads its value from a labeled option, parsing with the given closure.
- [init(wrappedValue: Value, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> Value)](./option/init%28wrappedvalue,name,parsing,help,completion,transform%29-2llve.md)
  Creates a property with a default value that reads its value from a labeled option, parsing with the given closure.
- [struct SingleValueParsingStrategy](./singlevalueparsingstrategy.md)
  The strategy to use when parsing a single value from `@Option` arguments.
### Array Options
- [init<T>(name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28name,parsing,help,completion%29-238hg.md)
  Creates a required array property that reads its values from zero or more labeled options.
- [init<T>(name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28name,parsing,help,completion,transform%29-74hnp.md)
  Creates a required array property that reads its values from zero or more labeled options, parsing each element with the given closure.
- [init<T>(wrappedValue: [T], name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28wrappedvalue,name,parsing,help,completion%29-1dtbf.md)
  Creates an array property that reads its values from zero or more labeled options.
- [init<T>(wrappedValue: [T], name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28wrappedvalue,name,parsing,help,completion,transform%29-1kpto.md)
  Creates an array property that reads its values from zero or more labeled options, parsing each element with the given closure.
- [struct ArrayParsingStrategy](./arrayparsingstrategy.md)
  The strategy to use when parsing multiple values from `@Option` arguments into an array.
### Infrequently Used APIs
- [var wrappedValue: Value](./option/wrappedvalue.md)
  The value presented by this property wrapper.
### Initializers
- [init<T>(name: NameSpecification, defaultAsFlag: T, parsing: DefaultAsFlagParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28name,defaultasflag,parsing,help,completion%29.md)
  Creates an optional property that reads its value from a labeled option, with a default value when the flag is provided without a value.
- [init<T>(name: NameSpecification, defaultAsFlag: T, parsing: DefaultAsFlagParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28name,defaultasflag,parsing,help,completion,transform%29.md)
  Creates an optional property that reads its value from a labeled option, parsing with the given closure, with a default value when the flag is provided without a value.
- [init<T>(wrappedValue: _OptionalNilComparisonType, name: NameSpecification, defaultAsFlag: T, parsing: DefaultAsFlagParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28wrappedvalue,name,defaultasflag,parsing,help,completion%29.md)
  Creates an optional property that reads its value from a labeled option, with a default value when the flag is provided without a value.
- [init<T>(wrappedValue: _OptionalNilComparisonType, name: NameSpecification, defaultAsFlag: T, parsing: DefaultAsFlagParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28wrappedvalue,name,defaultasflag,parsing,help,completion,transform%29.md)
  Creates an optional property that reads its value from a labeled option, parsing with the given closure, with a default value when the flag is provided without a value.
- [init<T>(wrappedValue: _OptionalNilComparisonType, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28wrappedvalue,name,parsing,help,completion%29-24mra.md)
  Creates an optional property that reads its value from a labeled option, with an explicit `nil` default.
- [init<T>(wrappedValue: _OptionalNilComparisonType, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28wrappedvalue,name,parsing,help,completion,transform%29-75p6e.md)
  Creates an optional property that reads its value from a labeled option, parsing with the given closure, with an explicit `nil` default.
### Default Implementations
- [CustomStringConvertible Implementations](./option/customstringconvertible-implementations.md)

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
- [struct Flag](./flag.md)
  A property wrapper that represents a command-line flag.
- [struct OptionGroup](./optiongroup.md)
  A wrapper that transparently includes a parsable type.
- [protocol ParsableArguments](./parsablearguments.md)
  A type that can be parsed from a program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option)*