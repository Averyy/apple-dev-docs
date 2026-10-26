---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/cleanexit/helprequest(_:)-773ef"
framework: "swift-argument-parser/ArgumentParser"
---

# helpRequest(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Treat this error as a help request and display the full help message.

## Declaration

```swift
static func helpRequest(_ command: (any ParsableCommand.Type)? = nil) -> CleanExit
```

#### Return Value

A throwable CleanExit error.

#### Discussion

You can use this case to simulate the user specifying one of the help flags or subcommands.

## Parameters

- `command`: The command type to offer help for, if different from the root command.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/cleanexit/helprequest(_:)-773ef)*