---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:help:completion:transform:)-84qu9"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:help:completion:transform:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

This initializer allows a user to provide a `nil` default value for an optional `@Argument`-marked property without allowing a non-`nil` default value.

## Declaration

```swift
@preconcurrency
init<T>(wrappedValue: _OptionalNilComparisonType, help: ArgumentHelp? = nil, completion: CompletionKind? = nil, transform: @Sendable @escaping (String) throws -> T) where Value == T?
```

## Parameters

- `wrappedValue`: A default value to use for this property, provided implicitly by the compiler during property wrapper initialization.
- `help`: Information about how to use this argument.
- `completion`: Kind of completion provided to the user for this option.
- `transform`: A closure that converts a string into this property’s element type or throws an error.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:help:completion:transform:)-84qu9)*