---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:parsing:help:completion:)"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:parsing:help:completion:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a property that reads an array from zero or more arguments.

## Declaration

```swift
init<T>(wrappedValue: [T], parsing parsingStrategy: ArgumentArrayParsingStrategy = .remaining, help: ArgumentHelp? = nil, completion: CompletionKind? = nil) where Value == [T], T : ExpressibleByArgument
```

## Parameters

- `wrappedValue`: A default value to use for this property.
- `parsingStrategy`: The behavior to use when parsing multiple values from the command-line arguments.
- `help`: Information about how to use this argument.
- `completion`: Kind of completion provided to the user for this option.

## See Also

### Array Arguments
- [init<T>(parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28parsing,help,completion%29.md)
  Creates a property with no default value that reads an array from zero or more arguments.
- [init<T>(parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./init%28parsing,help,completion,transform%29.md)
  Creates a property with no default value that reads an array from zero or more arguments, parsing each element with the given closure.
- [init<T>(wrappedValue: [T], parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./init%28wrappedvalue,parsing,help,completion,transform%29.md)
  Creates a property that reads an array from zero or more arguments, parsing each element with the given closure.
- [struct ArgumentArrayParsingStrategy](../argumentarrayparsingstrategy.md)
  The strategy to use when parsing multiple values from positional arguments into an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:parsing:help:completion:))*