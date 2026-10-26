---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/singlevalueparsingstrategy"
framework: "swift-argument-parser/ArgumentParser"
---

# SingleValueParsingStrategy

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

The strategy to use when parsing a single value from `@Option` arguments.

## Declaration

```swift
struct SingleValueParsingStrategy
```

#### Overview

> **See Also**: [`ArrayParsingStrategy`](./arrayparsingstrategy.md)

## Topics

### Type Properties
- [static var next: SingleValueParsingStrategy](./singlevalueparsingstrategy/next.md)
  Parse the input after the option and expect it to be a value.
- [static var scanningForValue: SingleValueParsingStrategy](./singlevalueparsingstrategy/scanningforvalue.md)
  Parse the next input, as long as that input can’t be interpreted as an option or flag.
- [static var unconditional: SingleValueParsingStrategy](./singlevalueparsingstrategy/unconditional.md)
  Parse the next input, even if it could be interpreted as an option or flag.
### Default Implementations
- [Equatable Implementations](./singlevalueparsingstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Single-Value Options
- [init(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28name,parsing,help,completion%29-4yske.md)
  Creates a required property that reads its value from a labeled option.
- [init<T>(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28name,parsing,help,completion%29-7slrf.md)
  Creates an optional property that reads its value from a labeled option.
- [init(wrappedValue: Value, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28wrappedvalue,name,parsing,help,completion%29-7ilku.md)
  Creates a property with a default value that reads its value from a labeled option.
- [init(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> Value)](./option/init%28name,parsing,help,completion,transform%29-2wf44.md)
  Creates a required property that reads its value from a labeled option, parsing with the given closure.
- [init<T>(name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28name,parsing,help,completion,transform%29-25g7b.md)
  Creates an optional property that reads its value from a labeled option, parsing with the given closure.
- [init(wrappedValue: Value, name: NameSpecification, parsing: SingleValueParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> Value)](./option/init%28wrappedvalue,name,parsing,help,completion,transform%29-2llve.md)
  Creates a property with a default value that reads its value from a labeled option, parsing with the given closure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/singlevalueparsingstrategy)*