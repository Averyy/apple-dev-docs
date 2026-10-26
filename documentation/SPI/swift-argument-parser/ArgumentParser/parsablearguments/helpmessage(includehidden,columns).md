---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/helpmessage(includehidden:columns:)"
framework: "swift-argument-parser/ArgumentParser"
---

# helpMessage(includeHidden:columns:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns the text of the help screen for this type.

## Declaration

```swift
static func helpMessage(includeHidden: Bool = false, columns: Int? = nil) -> String
```

#### Return Value

The full help screen for this type.

## Parameters

- `includeHidden`: Include hidden help information in the generated message.
- `columns`: The column width to use when wrapping long line in the help screen. If `columns` is `nil`, uses the current terminal width, or a default value of `80` if the terminal width is not available.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/helpmessage(includehidden:columns:))*