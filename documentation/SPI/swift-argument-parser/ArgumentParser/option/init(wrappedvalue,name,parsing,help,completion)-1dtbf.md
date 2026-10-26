---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(wrappedvalue:name:parsing:help:completion:)-1dtbf"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:name:parsing:help:completion:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates an array property that reads its values from zero or more labeled options.

## Declaration

```swift
init<T>(wrappedValue: [T], name: NameSpecification = .long, parsing parsingStrategy: ArrayParsingStrategy = .singleValue, help: ArgumentHelp? = nil, completion: CompletionKind? = nil) where Value == [T], T : ExpressibleByArgument
```

#### Discussion

This initializer is used when you declare an `@Option`-attributed array property with a default value:

```swift
@Option(name: .customLong("char"))
var chars: [Character] = []
```

If the element type conforms to `ExpressibleByArgument` and has enumerable value descriptions (via `defaultValueDescription`), the help output will display each possible value with its description, similar to single enumerable options.

## Parameters

- `wrappedValue`: A default value to use for this property, provided implicitly by the compiler during property wrapper initialization. If this initial value is non-empty, elements passed from the command line are appended to the original contents.
- `name`: A specification for what names are allowed for this option.
- `parsingStrategy`: The behavior to use when parsing the elements for this option.
- `help`: Information about how to use this option.
- `completion`: The type of command-line completion provided for this option.

## See Also

### Array Options
- [init<T>(name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./init%28name,parsing,help,completion%29-238hg.md)
  Creates a required array property that reads its values from zero or more labeled options.
- [init<T>(name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./init%28name,parsing,help,completion,transform%29-74hnp.md)
  Creates a required array property that reads its values from zero or more labeled options, parsing each element with the given closure.
- [init<T>(wrappedValue: [T], name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./init%28wrappedvalue,name,parsing,help,completion,transform%29-1kpto.md)
  Creates an array property that reads its values from zero or more labeled options, parsing each element with the given closure.
- [struct ArrayParsingStrategy](../arrayparsingstrategy.md)
  The strategy to use when parsing multiple values from `@Option` arguments into an array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/option/init(wrappedvalue:name:parsing:help:completion:)-1dtbf)*