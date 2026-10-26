---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:help:completion:)-1rfjo"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:help:completion:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

This initializer allows a user to provide a `nil` default value for an optional `@Argument`-marked property without allowing a non-`nil` default value.

## Declaration

```swift
init<T>(wrappedValue: _OptionalNilComparisonType, help: ArgumentHelp? = nil, completion: CompletionKind? = nil) where Value == T?, T : ExpressibleByArgument
```

## Parameters

- `wrappedValue`: A default value to use for this property, provided implicitly by the compiler during property wrapper initialization.
- `help`: Information about how to use this argument.
- `completion`: Kind of completion provided to the user for this option.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:help:completion:)-1rfjo)*