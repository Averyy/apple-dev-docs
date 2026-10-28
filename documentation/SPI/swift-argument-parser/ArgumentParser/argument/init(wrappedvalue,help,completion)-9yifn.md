---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:help:completion:)-9yifn"
framework: "swift-argument-parser/ArgumentParser"
---

# init(wrappedValue:help:completion:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: init  
**Role**: Initializer

Creates a property with a default value provided by standard Swift default value syntax.

## Declaration

```swift
init(wrappedValue: Value, help: ArgumentHelp? = nil, completion: CompletionKind? = nil)
```

Available when `Value` conforms to `ExpressibleByArgument`.

## Discussion

This method is called to initialize an `Argument` with a default value such as:

```swift
@Argument var foo: String = "bar"
```

## Parameters

- `wrappedValue`: A default value to use for this property, provided implicitly by the compiler during property wrapper initialization.
- `help`: Information about how to use this argument.
- `completion`: Kind of completion provided to the user for this option.

## See Also

### Single Arguments
- [init(help: ArgumentHelp?, completion: CompletionKind?)](./init%28help,completion%29-6pqzn.md)
  Creates a property with no default value.
- [init<T>(help: ArgumentHelp?, completion: CompletionKind?)](./init%28help,completion%29-4p94d.md)
  Creates an optional property that reads its value from an argument.
- [init(help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> Value)](./init%28help,completion,transform%29-3fjtc.md)
  Creates a property with no default value, parsing with the given closure.
- [init<T>(help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> T)](./init%28help,completion,transform%29-7yn32.md)
  Creates an optional property that reads its value from an argument.
- [init(wrappedValue: Value, help: ArgumentHelp?, completion: CompletionKind?, transform: @Sendable (String) throws -> Value)](./init%28wrappedvalue,help,completion,transform%29-667t1.md)
  Creates a property with a default value provided by standard Swift default value syntax, parsing with the given closure.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argument/init(wrappedvalue:help:completion:)-9yifn)*