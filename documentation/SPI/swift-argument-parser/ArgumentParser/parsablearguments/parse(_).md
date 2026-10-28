---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/parse(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# parse(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Parses a new instance of this type from command-line arguments.

## Declaration

```swift
static func parse(_ arguments: [String]? = nil) throws -> Self
```

## Mentions

- [Manual Parsing and Testing](../manualparsing.md)

## Return Value

A new instance of this type.

## Discussion

> **Throws**: If parsing failed or arguments contains a help request.

## Parameters

- `arguments`: An array of arguments to use for parsing. If `arguments` is `nil`, this uses the program’s command-line arguments.

## See Also

### Parsing a Type
- [static func parseOrExit([String]?) -> Self](./parseorexit%28_%29.md)
  Parses a new instance of this type from command-line arguments or exits with a relevant message.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/parse(_:))*