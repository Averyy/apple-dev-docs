---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/exitcode(for:)"
framework: "swift-argument-parser/ArgumentParser"
---

# exitCode(for:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns the exit code for the given error.

## Declaration

```swift
static func exitCode(for error: Error) -> ExitCode
```

## Return Value

The exit code for `error`.

## Discussion

The returned code is the same exit code that is used if `error` is passed to `exit(withError:)`.

## Parameters

- `error`: An error to generate an exit code for.

## See Also

### Handling Errors
- [static func message(for: Error) -> String](./message%28for%29.md)
  Returns a brief message for the given error.
- [static func fullMessage(for: Error, columns: Int?) -> String](./fullmessage%28for,columns%29.md)
  Returns a full message for the given error, including usage information, if appropriate.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/exitcode(for:))*