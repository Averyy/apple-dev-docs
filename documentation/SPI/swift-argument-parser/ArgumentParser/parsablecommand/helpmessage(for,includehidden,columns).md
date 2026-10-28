---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/helpmessage(for:includehidden:columns:)"
framework: "swift-argument-parser/ArgumentParser"
---

# helpMessage(for:includeHidden:columns:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns the text of the help screen for the given subcommand of this command.

## Declaration

```swift
static func helpMessage(for subcommand: ParsableCommand.Type, includeHidden: Bool = false, columns: Int? = nil) -> String
```

## Return Value

The full help screen for this type.

## Parameters

- `subcommand`: The subcommand to generate the help screen for. `subcommand` must be declared in the subcommand tree of this command.
- `includeHidden`: Include hidden help information in the generated message.
- `columns`: The column width to use when wrapping long line in the help screen. If `columns` is `nil`, uses the current terminal width, or a default value of `80` if the terminal width is not available.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/helpmessage(for:includehidden:columns:))*