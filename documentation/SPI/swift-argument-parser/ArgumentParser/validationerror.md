---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/validationerror"
framework: "swift-argument-parser/ArgumentParser"
---

# ValidationError

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

An error type that is presented to the user as an error with parsing their command-line input.

## Declaration

```swift
struct ValidationError
```

## Mentions

- [Manual Parsing and Testing](./manualparsing.md)
- [Providing Custom Validation](./validation.md)

## Topics

### Initializers
- [init(String)](./validationerror/init%28_%29.md)
  Creates a new validation error with the given message.
### Instance Properties
- [var description: String](./validationerror/description.md)
- [var message: String](./validationerror/message.md)
  The error message represented by this instance, this string is presented to the user when a `ValidationError` is thrown from either; `run()`, `validate()` or a transform closure.
### Default Implementations
- [Error Implementations](./validationerror/error-implementations.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Validation and Errors
- [Providing Custom Validation](./validation.md)
  Provide helpful feedback to users when things go wrong.
- [struct CleanExit](./cleanexit.md)
  An error type that represents a clean (non-error state) exit of the utility.
- [struct ExitCode](./exitcode.md)
  An error type that only includes an exit code.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/validationerror)*