---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy"
framework: "swift-argument-parser/ArgumentParser"
---

# ArrayParsingStrategy

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

The strategy to use when parsing multiple values from `@Option` arguments into an array.

## Declaration

```swift
struct ArrayParsingStrategy
```

## Topics

### Type Properties
- [static var remaining: ArrayParsingStrategy](./arrayparsingstrategy/remaining.md)
  Parse all remaining arguments into an array.
- [static var singleValue: ArrayParsingStrategy](./arrayparsingstrategy/singlevalue.md)
  Parse one value per option, joining multiple into an array.
- [static var unconditionalSingleValue: ArrayParsingStrategy](./arrayparsingstrategy/unconditionalsinglevalue.md)
  Parse the value immediately after the option while allowing repeating options, joining multiple into an array.
- [static var upToNextOption: ArrayParsingStrategy](./arrayparsingstrategy/uptonextoption.md)
  Parse all values up to the next option.
### Default Implementations
- [Equatable Implementations](./arrayparsingstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Array Options
- [init<T>(name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28name,parsing,help,completion%29-238hg.md)
  Creates a required array property that reads its values from zero or more labeled options.
- [init<T>(name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28name,parsing,help,completion,transform%29-74hnp.md)
  Creates a required array property that reads its values from zero or more labeled options, parsing each element with the given closure.
- [init<T>(wrappedValue: [T], name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./option/init%28wrappedvalue,name,parsing,help,completion%29-1dtbf.md)
  Creates an array property that reads its values from zero or more labeled options.
- [init<T>(wrappedValue: [T], name: NameSpecification, parsing: ArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./option/init%28wrappedvalue,name,parsing,help,completion,transform%29-1kpto.md)
  Creates an array property that reads its values from zero or more labeled options, parsing each element with the given closure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy)*