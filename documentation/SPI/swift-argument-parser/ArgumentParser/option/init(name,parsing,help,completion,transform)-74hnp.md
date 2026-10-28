---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(name:parsing:help:completion:transform:)-74hnp"
framework: "swift-argument-parser/ArgumentParser"
---

# init(name:parsing:help:completion:transform:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a required array property that reads its values from zero or more labeled options, parsing each element with the given closure.

## Declaration

```swift
@preconcurrency
init<T>(name: NameSpecification = .long, parsing parsingStrategy: ArrayParsingStrategy = .singleValue, help: ArgumentHelp? = nil, completion: CompletionKind? = nil, transform: @Sendable @escaping (String) throws -> T) where Value == [T]
```

## Discussion

This initializer is used when you declare an `@Option`-attributed array property with a transform closure and without a default value:

```swift
@Option(name: .customLong("char"), transform: { $0.first ?? " " })
var chars: [Character]
```

## Parameters

- `name`: A specification for what names are allowed for this option.
- `parsingStrategy`: The behavior to use when parsing the elements for this option.
- `help`: Information about how to use this option.
- `completion`: The type of command-line completion provided for this option.
- `transform`: A closure that converts a string into this property’s element type, or else throws an error.

## See Also

### Array Options
- [init<T>(name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28name,parsing,help,completion%29-238hg.md)
  Creates a required array property that reads its values from zero or more labeled options.
- [init<T>(wrappedValue: [T], name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28wrappedvalue,name,parsing,help,completion%29-1dtbf.md)
  Creates an array property that reads its values from zero or more labeled options.
- [init<T>(wrappedValue: [T], name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./init%28wrappedvalue,name,parsing,help,completion,transform%29-1kpto.md)
  Creates an array property that reads its values from zero or more labeled options, parsing each element with the given closure.
- [struct ArrayParsingStrategy](../arrayparsingstrategy.md)
  The strategy to use when parsing multiple values from `@Option` arguments into an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(name:parsing:help:completion:transform:)-74hnp)*