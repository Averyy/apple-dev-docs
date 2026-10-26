---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/message(for:)"
framework: "swift-argument-parser/ArgumentParser"
---

# message(for:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns a brief message for the given error.

## Declaration

```swift
static func message(for error: any Error) -> String
```

#### Return Value

A message that can be displayed to the user.

## Parameters

- `error`: An error to generate a message for.

## See Also

### Handling Errors
- [static func fullMessage(for: any Error, columns: Int?) -> String](./fullmessage%28for,columns%29.md)
  Returns a full message for the given error, including usage information, if appropriate.
- [static func exitCode(for: any Error) -> ExitCode](./exitcode%28for%29.md)
  Returns the exit code for the given error.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/message(for:))*