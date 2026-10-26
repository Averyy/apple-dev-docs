---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag"
framework: "swift-argument-parser/ArgumentParser"
---

# Flag

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A property wrapper that represents a command-line flag.

## Declaration

```swift
@propertyWrapper
struct Flag<Value>
```

## Mentions

- [Declaring Arguments, Options, and Flags](./declaringarguments.md)

#### Overview

Use the `@Flag` wrapper to define a property of your custom type as a command-line flag. A *flag* is a dash-prefixed label that can be provided on the command line, such as `-d` and `--debug`.

For example, the following program declares a flag that lets a user indicate that seconds should be included when printing the time.

```swift
@main
struct Time: ParsableCommand {
    @Flag var includeSeconds = false

    mutating func run() {
        if includeSeconds {
            print(Date.now.formatted(.dateTime.hour().minute().second()))
        } else {
            print(Date.now.formatted(.dateTime.hour().minute()))
        }
    }
}
```

`includeSeconds` has a default value of `false`, but becomes `true` if `--include-seconds` is provided on the command line.

```
$ time
11:09 AM
$ time --include-seconds
11:09:15 AM
```

A flag can have a value that is a `Bool`, an `Int`, or any `EnumerableFlag` type. When using an `EnumerableFlag` type as a flag, the individual cases form the flags that are used on the command line.

```
@main
struct Math: ParsableCommand {
    enum Operation: EnumerableFlag {
        case add
        case multiply
    }

    @Flag var operation: Operation

    mutating func run() {
        print("Time to \(operation)!")
    }
}
```

Instead of using the name of the `operation` property as the flag in this case, the two cases of the `Operation` enumeration become valid flags. The `operation` property is neither optional nor given a default value, so one of the two flags is required.

```
$ math --add
Time to add!
$ math
Error: Missing one of: '--add', '--multiply'
```

## Topics

### Boolean Flags
- [init(wrappedValue: Bool, name: NameSpecification, help: ArgumentHelp?)](./flag/init%28wrappedvalue,name,help%29.md)
  Creates a Boolean property with default value provided by standard Swift default value syntax that reads its value from the presence of a flag.
### Boolean Flags with Inversions
- [init(wrappedValue: Bool, name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28wrappedvalue,name,inversion,exclusivity,help%29.md)
  Creates a Boolean property with default value provided by standard Swift default value syntax that reads its value from the presence of one or more inverted flags.
- [init(name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28name,inversion,exclusivity,help%29-12okg.md)
  Creates a Boolean property with no default value that reads its value from the presence of one or more inverted flags.
- [init(name: NameSpecification, inversion: FlagInversion, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28name,inversion,exclusivity,help%29-1h8f7.md)
  Creates a Boolean property that reads its value from the presence of one or more inverted flags.
- [struct FlagInversion](./flaginversion.md)
  The options for converting a Boolean flag into a `true`/`false` pair.
### Counted Flags
- [init(name: NameSpecification, help: ArgumentHelp?)](./flag/init%28name,help%29.md)
  Creates an integer property that gets its value from the number of times a flag appears.
### Custom Enumerable Flags
- [init<Element>(help: ArgumentHelp?)](./flag/init%28help%29.md)
  Creates an array property with no default value that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.
- [init<Element>(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28exclusivity,help%29-38n7u.md)
  Creates a property that gets its value from the presence of a flag, where the allowed flags are defined by an `EnumerableFlag` type.
- [init(exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28exclusivity,help%29-5fggj.md)
  Creates a property with no default value that gets its value from the presence of a flag.
- [init(wrappedValue: Value, exclusivity: FlagExclusivity, help: ArgumentHelp?)](./flag/init%28wrappedvalue,exclusivity,help%29.md)
  Creates a property with a default value provided by standard Swift default value syntax that gets its value from the presence of a flag.
- [init<Element>(wrappedValue: [Element], help: ArgumentHelp?)](./flag/init%28wrappedvalue,help%29.md)
  Creates an array property that gets its values from the presence of zero or more flags, where the allowed flags are defined by an `EnumerableFlag` type.
### Infrequently Used APIs
- [var wrappedValue: Value](./flag/wrappedvalue.md)
  The value presented by this property wrapper.
### Supporting Types
- [struct FlagExclusivity](./flagexclusivity.md)
  The options for treating enumeration-based flags as exclusive.
### Default Implementations
- [CustomStringConvertible Implementations](./flag/customstringconvertible-implementations.md)

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
- [struct OptionGroup](./optiongroup.md)
  A wrapper that transparently includes a parsable type.
- [protocol ParsableArguments](./parsablearguments.md)
  A type that can be parsed from a program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flag)*