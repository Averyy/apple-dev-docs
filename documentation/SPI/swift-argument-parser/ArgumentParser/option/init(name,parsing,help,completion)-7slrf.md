---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(name:parsing:help:completion:)-7slrf"
framework: "swift-argument-parser/ArgumentParser"
---

# init(name:parsing:help:completion:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates an optional property that reads its value from a labeled option.

## Declaration

```swift
init<T>(name: NameSpecification = .long, parsing parsingStrategy: SingleValueParsingStrategy = .next, help: ArgumentHelp? = nil, completion: CompletionKind? = nil) where Value == T?, T : ExpressibleByArgument
```

## Discussion

This initializer is used when you declare an `@Option`-attributed property with an optional type and no default value:

```swift
@Option var count: Int?
```

## Parameters

- `name`: A specification for what names are allowed for this option.
- `parsingStrategy`: The behavior to use when looking for this option’s value.
- `help`: Information about how to use this option.
- `completion`: The type of command-line completion provided for this option.

## See Also

### Single-Value Options
- [init(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28name,parsing,help,completion%29-4yske.md)
  Creates a required property that reads its value from a labeled option.
- [init(wrappedValue: Value, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28wrappedvalue,name,parsing,help,completion%29-7ilku.md)
  Creates a property with a default value that reads its value from a labeled option.
- [init(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> Value)](./init%28name,parsing,help,completion,transform%29-2wf44.md)
  Creates a required property that reads its value from a labeled option, parsing with the given closure.
- [init<T>(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./init%28name,parsing,help,completion,transform%29-25g7b.md)
  Creates an optional property that reads its value from a labeled option, parsing with the given closure.
- [init(wrappedValue: Value, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> Value)](./init%28wrappedvalue,name,parsing,help,completion,transform%29-2llve.md)
  Creates a property with a default value that reads its value from a labeled option, parsing with the given closure.
- [struct SingleValueParsingStrategy](../singlevalueparsingstrategy.md)
  The strategy to use when parsing a single value from `@Option` arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(name:parsing:help:completion:)-7slrf)*