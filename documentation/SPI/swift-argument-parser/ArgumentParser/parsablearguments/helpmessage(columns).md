---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/helpmessage(columns:)"
framework: "swift-argument-parser/ArgumentParser"
---

# helpMessage(columns:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns the text of the help screen for this type.

> **Deprecated**: Use helpMessage(includeHidden:columns:) instead.

## Declaration

```swift
static func helpMessage(columns: Int?) -> String
```

## Return Value

The full help screen for this type.

## Parameters

- `columns`: The column width to use when wrapping long line in the help screen. If `columns` is `nil`, uses the current terminal width, or a default value of `80` if the terminal width is not available.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/helpmessage(columns:))*