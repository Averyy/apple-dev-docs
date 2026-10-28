---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/subcommands"
framework: "swift-argument-parser/ArgumentParser"
---

# subcommands

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Instance Property

An array of the types that define subcommands for this command.

## Declaration

```swift
var subcommands: [ParsableCommand.Type] { get set }
```

## Discussion

This property “flattens” the grouping structure of the subcommands. Use ‘ungroupedSubcommands’ to access ‘groupedSubcommands’ to retain the grouping structure.

## See Also

### Declaring Subcommands
- [var defaultSubcommand: ParsableCommand.Type?](./defaultsubcommand.md)
  The default command type to run if no subcommand is given.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/subcommands)*