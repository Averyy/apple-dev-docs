---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy"
framework: "swift-argument-parser/ArgumentParser"
---

# ArgumentArrayParsingStrategy

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

The strategy to use when parsing multiple values from positional arguments into an array.

## Declaration

```swift
struct ArgumentArrayParsingStrategy
```

## Topics

### Parsing Strategies
- [static var remaining: ArgumentArrayParsingStrategy](./argumentarrayparsingstrategy/remaining.md)
  Parse only unprefixed values from the command-line input, ignoring any inputs that have a dash prefix; this is the default strategy.
- [static var allUnrecognized: ArgumentArrayParsingStrategy](./argumentarrayparsingstrategy/allunrecognized.md)
  After parsing, capture all unrecognized inputs in this argument array.
- [static var postTerminator: ArgumentArrayParsingStrategy](./argumentarrayparsingstrategy/postterminator.md)
  Before parsing arguments, capture all inputs that follow the `--` terminator in this argument array.
- [static var captureForPassthrough: ArgumentArrayParsingStrategy](./argumentarrayparsingstrategy/captureforpassthrough.md)
  Parse all remaining inputs after parsing any known options or flags, including dash-prefixed inputs and the `--` terminator.
### Deprecated
- [static var unconditionalRemaining: ArgumentArrayParsingStrategy](./argumentarrayparsingstrategy/unconditionalremaining.md)
### Default Implementations
- [Equatable Implementations](./argumentarrayparsingstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Array Arguments
- [init<T>(parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28parsing,help,completion%29.md)
  Creates a property with no default value that reads an array from zero or more arguments.
- [init<T>(parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./argument/init%28parsing,help,completion,transform%29.md)
  Creates a property with no default value that reads an array from zero or more arguments, parsing each element with the given closure.
- [init<T>(wrappedValue: [T], parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?)](./argument/init%28wrappedvalue,parsing,help,completion%29.md)
  Creates a property that reads an array from zero or more arguments.
- [init<T>(wrappedValue: [T], parsing: ArgumentArrayParsingStrategy, help: ArgumentHelp?, completion: CompletionKind?, transform: (String) throws -> T)](./argument/init%28wrappedvalue,parsing,help,completion,transform%29.md)
  Creates a property that reads an array from zero or more arguments, parsing each element with the given closure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy)*