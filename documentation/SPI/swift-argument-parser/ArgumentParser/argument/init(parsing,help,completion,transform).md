---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(parsing:help:completion:transform:)"
framework: "swift-argument-parser/ArgumentParser"
---

# init(parsing:help:completion:transform:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a property with no default value that reads an array from zero or more arguments, parsing each element with the given closure.

## Declaration

```swift
@preconcurrency
init<T>(parsing parsingStrategy: ArgumentArrayParsingStrategy = .remaining, help: ArgumentHelp? = nil, completion: CompletionKind? = nil, transform: @escaping @Sendable (String) throws -> T) where Value == [T]
```

#### Discussion

This method is called to initialize an array `Argument` with no default value such as:

```swift
@Argument(transform: baz)
var foo: [String]
```

## Parameters

- `parsingStrategy`: The behavior to use when parsing multiple values from the command-line arguments.
- `help`: Information about how to use this argument.
- `completion`: Kind of completion provided to the user for this option.
- `transform`: A closure that converts a string into this property’s element type or throws an error.

## See Also

### Array Arguments
- [init<T>(parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28parsing,help,completion%29.md)
  Creates a property with no default value that reads an array from zero or more arguments.
- [init<T>(wrappedValue: [T], parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28wrappedvalue,parsing,help,completion%29.md)
  Creates a property that reads an array from zero or more arguments.
- [init<T>(wrappedValue: [T], parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./init%28wrappedvalue,parsing,help,completion,transform%29.md)
  Creates a property that reads an array from zero or more arguments, parsing each element with the given closure.
- [struct ArgumentArrayParsingStrategy](../argumentarrayparsingstrategy.md)
  The strategy to use when parsing multiple values from positional arguments into an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(parsing:help:completion:transform:))*