---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/asyncparse(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# asyncParse(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Parses a new instance of this type from command-line arguments.

**Availability**:
- iOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
static func asyncParse(_ arguments: [String]? = nil) async throws -> Self
```

#### Return Value

A new instance of this type.

#### Discussion

> **Throws**: If parsing failed or arguments contains a help request.

## Parameters

- `arguments`: An array of arguments to use for parsing. If `arguments` is `nil`, this uses the program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/asyncparse(_:))*