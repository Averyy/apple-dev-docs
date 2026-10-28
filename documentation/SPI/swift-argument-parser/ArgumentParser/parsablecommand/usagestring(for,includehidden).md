---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/usagestring(for:includehidden:)"
framework: "swift-argument-parser/ArgumentParser"
---

# usageString(for:includeHidden:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns the usage text for the given subcommand of this command.

## Declaration

```swift
static func usageString(for subcommand: ParsableCommand.Type, includeHidden: Bool = false) -> String
```

## Return Value

The usage text for this type.

## Parameters

- `subcommand`: The subcommand to generate the help screen for. `subcommand` must be declared in the subcommand tree of this command.
- `includeHidden`: Include hidden help information in the generated message.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/usagestring(for:includehidden:))*