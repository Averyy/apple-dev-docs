---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/fullmessage(for:columns:)"
framework: "swift-argument-parser/ArgumentParser"
---

# fullMessage(for:columns:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns a full message for the given error, including usage information, if appropriate.

## Declaration

```swift
static func fullMessage(for error: any Error, columns: Int? = nil) -> String
```

#### Return Value

A message that can be displayed to the user.

## Parameters

- `error`: An error to generate a message for.
- `columns`: The column width to use when wrapping long line in the help screen. If `columns` is `nil`, uses the current terminal width, or a default value of `80` if the terminal width is not available.

## See Also

### Handling Errors
- [static func message(for: any Error) -> String](./message%28for%29.md)
  Returns a brief message for the given error.
- [static func exitCode(for: any Error) -> ExitCode](./exitcode%28for%29.md)
  Returns the exit code for the given error.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/fullmessage(for:columns:))*