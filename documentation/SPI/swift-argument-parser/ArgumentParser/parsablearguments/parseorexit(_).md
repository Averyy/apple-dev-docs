---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/parseorexit(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# parseOrExit(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Parses a new instance of this type from command-line arguments or exits with a relevant message.

## Declaration

```swift
static func parseOrExit(_ arguments: [String]? = nil) -> Self
```

## Mentions

- [Manual Parsing and Testing](../manualparsing.md)

## Return Value

An instance of `Self` parsable properties populated with the provided argument values.

## Parameters

- `arguments`: An array of arguments to use for parsing. If `arguments` is `nil`, this uses the program’s command-line arguments.

## See Also

### Parsing a Type
- [static func parse([String]?) throws -> Self](./parse%28_%29.md)
  Parses a new instance of this type from command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablearguments/parseorexit(_:))*