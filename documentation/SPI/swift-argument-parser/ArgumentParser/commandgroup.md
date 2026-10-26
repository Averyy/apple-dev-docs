---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandgroup"
framework: "swift-argument-parser/ArgumentParser"
---

# CommandGroup

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

A set of commands grouped together under a common name.

## Declaration

```swift
struct CommandGroup
```

## Topics

### Initializers
- [init(name: String, subcommands: [any ParsableCommand.Type])](./commandgroup/init%28name,subcommands%29.md)
  Create a command group.
### Instance Properties
- [let name: String](./commandgroup/name.md)
  The name of the command group that will be displayed in help.
- [let subcommands: [any ParsableCommand.Type]](./commandgroup/subcommands.md)
  The list of subcommands that are part of this group.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandgroup)*