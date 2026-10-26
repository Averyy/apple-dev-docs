---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/exit(witherror:)"
framework: "swift-argument-parser/ArgumentParser"
---

# exit(withError:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Terminates execution with a message and exit code that is appropriate for the given error.

## Declaration

```swift
static func exit(withError error: (any Error)? = nil) -> Never
```

## Mentions

- [Manual Parsing and Testing](../manualparsing.md)

#### Discussion

If the `error` parameter is `nil`, this method prints nothing and exits with code `EXIT_SUCCESS`. If `error` represents a help request or another `CleanExit` error, this method prints help information and exits with code `EXIT_SUCCESS`. Otherwise, this method prints a relevant error message and exits with code `EX_USAGE` or `EXIT_FAILURE`.

## Parameters

- `error`: The error to use when exiting, if any.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/exit(witherror:))*