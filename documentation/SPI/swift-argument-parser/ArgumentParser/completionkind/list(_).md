---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/list(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# list(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

The completion candidates are the strings in the given array.

## Declaration

```swift
static func list(_ words: [String]) -> CompletionKind
```

## Discussion

Completion candidates are interpreted by the requesting shell as literals. They must be neither escaped nor quoted; Swift Argument Parser escapes or quotes them as necessary for the requesting shell.

The completion candidates are included in a completion script when it is generated.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/list(_:))*