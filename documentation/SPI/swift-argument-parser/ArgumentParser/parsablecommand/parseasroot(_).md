---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/parseasroot(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# parseAsRoot(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Parses an instance of this type, or one of its subcommands, from command-line arguments.

## Declaration

```swift
static func parseAsRoot(_ arguments: [String]? = nil) throws -> any ParsableCommand
```

## Mentions

- [Manual Parsing and Testing](../manualparsing.md)

#### Return Value

A new instance of this type, one of its subcommands, or a command type internal to the `ArgumentParser` library.

#### Discussion

> **Throws**: If parsing fails.

## Parameters

- `arguments`: An array of arguments to use for parsing. If `arguments` is `nil`, this uses the program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/parseasroot(_:))*