---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionshell/requesting"
framework: "swift-argument-parser/ArgumentParser"
---

# requesting

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

The shell for which completions will be or are being requested.

## Declaration

```swift
static var requesting: CompletionShell? { get }
```

## Discussion

`CompletionShell.requesting` is non-`nil` only while generating a shell completion script or while a Swift custom completion function is executing to offer completions for a word from a command line (that is, while `customCompletion` from `@Option(completion: .custom(customCompletion))` executes).


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionshell/requesting)*