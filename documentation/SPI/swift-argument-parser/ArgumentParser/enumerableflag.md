---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag"
framework: "swift-argument-parser/ArgumentParser"
---

# EnumerableFlag

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: protocol  
**Role**: Protocol

A type that represents the different possible flags to be used by a `@Flag` property.

## Declaration

```swift
protocol EnumerableFlag : CaseIterable, Equatable
```

## Mentions

- [Declaring Arguments, Options, and Flags](./declaringarguments.md)

## Overview

For example, the `Size` enumeration declared here can be used as the type of a `@Flag` property:

```swift
enum Size: String, EnumerableFlag {
    case small, medium, large, extraLarge
}

struct Example: ParsableCommand {
    @Flag var sizes: [Size]

    mutating func run() {
        print(sizes)
    }
}
```

By default, each case name is converted to a flag by using the `.long` name specification, so a user can call `example` like this:

```
$ example --small --large
[.small, .large]
```

Provide alternative or additional name specifications for each case by implementing the `name(for:)` static method on your `EnumerableFlag` type.

```swift
extension Size {
    static func name(for value: Self) -> NameSpecification {
        switch value {
        case .extraLarge:
            return [.customShort("x"), .long]
        default:
            return .shortAndLong
        }
    }
}
```

With this extension, a user can use short or long versions of the flags:

```
$ example -s -l -x --medium
[.small, .large, .extraLarge, .medium]
```

## Topics

### Instance Properties
- [var description: String](./enumerableflag/description.md)
### Type Methods
- [static func help(for: Self) -> ArgumentHelp?](./enumerableflag/help%28for%29.md)
  Returns the help information to show for the given flag.
- [static func name(for: Self) -> NameSpecification](./enumerableflag/name%28for%29.md)
  Returns the name specification to use for the given flag.

## Relationships

### Inherits From
- Swift.CaseIterable
- Swift.Equatable

## See Also

### Custom Types
- [protocol ExpressibleByArgument](./expressiblebyargument.md)
  A type that can be expressed as a command-line argument.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag)*