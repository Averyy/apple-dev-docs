---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/cleanexit"
framework: "swift-argument-parser/ArgumentParser"
---

# CleanExit

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

An error type that represents a clean (non-error state) exit of the utility.

## Declaration

```swift
struct CleanExit
```

## Overview

Throwing a `CleanExit` instance from a `validate` or `run` method, or passing it to `exit(with:)`, exits the program with exit code `0`.

## Topics

### Instance Properties
- [var description: String](./cleanexit/description.md)
### Type Methods
- [static func helpRequest(ParsableCommand.Type?) -> CleanExit](./cleanexit/helprequest%28_%29-773ef.md)
  Treat this error as a help request and display the full help message.
- [static func helpRequest(ParsableCommand) -> CleanExit](./cleanexit/helprequest%28_%29-9qiuh.md)
  Treat this error as a help request and display the full help message.
- [static func message(String) -> CleanExit](./cleanexit/message%28_%29.md)
  Treat this error as a clean exit with the given message.
### Default Implementations
- [Error Implementations](./cleanexit/error-implementations.md)

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
- [struct ValidationError](./validationerror.md)
  An error type that is presented to the user as an error with parsing their command-line input.
- [struct ExitCode](./exitcode.md)
  An error type that only includes an exit code.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/cleanexit)*