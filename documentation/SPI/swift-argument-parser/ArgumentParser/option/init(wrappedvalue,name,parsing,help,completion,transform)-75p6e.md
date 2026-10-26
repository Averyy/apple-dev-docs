---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(wrappedvalue:name:parsing:help:completion:transform:)-75p6e"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:name:parsing:help:completion:transform:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates an optional property that reads its value from a labeled option, parsing with the given closure, with an explicit `nil` default.

## Declaration

```swift
@preconcurrency
init<T>(wrappedValue: _OptionalNilComparisonType, name: NameSpecification = .long, parsing parsingStrategy: SingleValueParsingStrategy = .next, help: ArgumentHelp? = nil, completion: CompletionKind? = nil, transform: @escaping @Sendable (String) throws -> T) where Value == T?
```

#### Discussion

This initializer is used when you declare an `@Option`-attributed property with a transform closure and with a default value of `nil`:

```swift
@Option(transform: { $0.first ?? " " })
var char: Character? = nil
```

## Parameters

- `wrappedValue`: A default value to use for this property, provided implicitly by the compiler during property wrapper initialization.
- `name`: A specification for what names are allowed for this option.
- `parsingStrategy`: The behavior to use when looking for this option’s value.
- `help`: Information about how to use this option.
- `completion`: The type of command-line completion provided for this option.
- `transform`: A closure that converts a string into this property’s type, or else throws an error.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(wrappedvalue:name:parsing:help:completion:transform:)-75p6e)*