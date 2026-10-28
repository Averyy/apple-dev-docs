---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/exitcode"
framework: "swift-argument-parser/ArgumentParser"
---

# ExitCode

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

An error type that only includes an exit code.

## Declaration

```swift
struct ExitCode
```

## Overview

If you’re printing custom error messages yourself, you can throw this error to specify the exit code without adding any additional output to standard out or standard error.

## Topics

### Initializers
- [init(Int32)](./exitcode/init%28_%29.md)
  Creates a new `ExitCode` with the given code.
- [init(rawValue: Int32)](./exitcode/init%28rawvalue%29.md)
### Instance Properties
- [var isSuccess: Bool](./exitcode/issuccess.md)
  A Boolean value indicating whether this exit code represents the successful completion of a command.
- [var rawValue: Int32](./exitcode/rawvalue.md)
  The exit code represented by this instance.
### Type Properties
- [static let failure: ExitCode](./exitcode/failure.md)
  An exit code that indicates that the command failed.
- [static let success: ExitCode](./exitcode/success.md)
  An exit code that indicates successful completion of a command.
- [static let validationFailure: ExitCode](./exitcode/validationfailure.md)
  An exit code that indicates that the user provided invalid input.
### Default Implementations
- [Equatable Implementations](./exitcode/equatable-implementations.md)
- [Error Implementations](./exitcode/error-implementations.md)
- [RawRepresentable Implementations](./exitcode/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Error
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Validation and Errors
- [Providing Custom Validation](./validation.md)
  Provide helpful feedback to users when things go wrong.
- [struct ValidationError](./validationerror.md)
  An error type that is presented to the user as an error with parsing their command-line input.
- [struct CleanExit](./cleanexit.md)
  An error type that represents a clean (non-error state) exit of the utility.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/exitcode)*