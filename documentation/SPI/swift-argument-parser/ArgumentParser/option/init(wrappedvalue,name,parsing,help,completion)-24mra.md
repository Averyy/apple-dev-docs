---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(wrappedvalue:name:parsing:help:completion:)-24mra"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:name:parsing:help:completion:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates an optional property that reads its value from a labeled option, with an explicit `nil` default.

## Declaration

```swift
init<T>(wrappedValue: _OptionalNilComparisonType, name: NameSpecification = .long, parsing parsingStrategy: SingleValueParsingStrategy = .next, help: ArgumentHelp? = nil, completion: CompletionKind? = nil) where Value == T?, T : ExpressibleByArgument
```

#### Discussion

This initializer allows a user to provide a `nil` default value for an optional `@Option`-marked property:

```swift
@Option var count: Int? = nil
```

## Parameters

- `wrappedValue`: A default value to use for this property, provided implicitly by the compiler during property wrapper initialization.
- `name`: A specification for what names are allowed for this option.
- `parsingStrategy`: The behavior to use when looking for this option’s value.
- `help`: Information about how to use this option.
- `completion`: The type of command-line completion provided for this option.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(wrappedvalue:name:parsing:help:completion:)-24mra)*