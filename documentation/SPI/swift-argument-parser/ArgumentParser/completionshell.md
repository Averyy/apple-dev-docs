---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionshell"
framework: "swift-argument-parser/ArgumentParser"
---

# CompletionShell

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A shell for which the parser can generate a completion script.

## Declaration

```swift
struct CompletionShell
```

## Topics

### Initializers
- [init?(rawValue: String)](./completionshell/init%28rawvalue%29.md)
  Creates a new instance from the given string.
### Instance Properties
- [var rawValue: String](./completionshell/rawvalue.md)
### Type Properties
- [static var allCases: [CompletionShell]](./completionshell/allcases.md)
  An array of all supported shells for completion scripts.
- [static var bash: CompletionShell](./completionshell/bash.md)
  An instance representing `bash`.
- [static var fish: CompletionShell](./completionshell/fish.md)
  An instance representing `fish`.
- [static var requesting: CompletionShell?](./completionshell/requesting.md)
  The shell for which completions will be or are being requested.
- [static var requestingVersion: String?](./completionshell/requestingversion.md)
  The shell version for which completions will be or are being requested.
- [static var zsh: CompletionShell](./completionshell/zsh.md)
  An instance representing `zsh`.
### Type Methods
- [static func autodetected() -> CompletionShell?](./completionshell/autodetected%28%29.md)
  Returns an instance representing the current shell, if recognized.
### Default Implementations
- [Equatable Implementations](./completionshell/equatable-implementations.md)
- [RawRepresentable Implementations](./completionshell/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Generating Completion Scripts
- [static func completionScript(for: CompletionShell) -> String](./parsablearguments/completionscript%28for%29.md)
  Returns a shell completion script for the specified shell.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionshell)*