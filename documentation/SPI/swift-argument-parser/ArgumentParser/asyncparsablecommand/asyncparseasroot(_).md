---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/asyncparseasroot(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# asyncParseAsRoot(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Parses an instance of this type, or one of its subcommands, from command-line arguments.

**Availability**:
- iOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
static func asyncParseAsRoot(_ arguments: [String]? = nil) async throws -> any ParsableCommand
```

#### Return Value

A new instance of this type, one of its subcommands, or a command type internal to the `ArgumentParser` library.

#### Discussion

> **Throws**: If parsing fails.

## Parameters

- `arguments`: An array of arguments to use for parsing. If `arguments` is `nil`, this uses the program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/asyncparseasroot(_:))*