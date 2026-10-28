---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionshell/requestingversion"
framework: "swift-argument-parser/ArgumentParser"
---

# requestingVersion

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

The shell version for which completions will be or are being requested.

## Declaration

```swift
static var requestingVersion: String? { get }
```

## Discussion

`CompletionShell.requestingVersion` is non-`nil` only while generating a shell completion script or while a Swift custom completion function is running (that is, while `customCompletion` from `@Option(completion: .custom(customCompletion))` executes).


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionshell/requestingversion)*