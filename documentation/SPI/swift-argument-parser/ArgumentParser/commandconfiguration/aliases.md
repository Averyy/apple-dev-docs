---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/aliases"
framework: "swift-argument-parser/ArgumentParser"
---

# aliases

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Instance Property

An array of aliases for the command’s name.

## Declaration

```swift
var aliases: [String]
```

## Discussion

All of the aliases MUST not match the actual command’s name, whether that be the derived name if `commandName` is not provided, or `commandName` itself if provided.

## See Also

### Defining Command Properties
- [var commandName: String?](./commandname.md)
  The name of the command to use on the command line.
- [var version: String](./version.md)
  Version information for this command.
- [var shouldDisplay: Bool](./shoulddisplay.md)
  A Boolean value indicating whether this command should be shown in the extended help display.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/aliases)*