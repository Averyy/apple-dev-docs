---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/shellcommand(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# shellCommand(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

The completion candidates are specified by the `stdout` output of the given string run as a shell command when a user requests completions.

## Declaration

```swift
static func shellCommand(_ command: String) -> CompletionKind
```

## Discussion

Swift Argument Parser does not perform any escaping or quoting on the given shell command.

The given shell command is included in a completion script when it is generated.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/shellcommand(_:))*