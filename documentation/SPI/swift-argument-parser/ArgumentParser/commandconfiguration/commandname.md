---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/commandname"
framework: "swift-argument-parser/ArgumentParser"
---

# commandName

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Instance Property

The name of the command to use on the command line.

## Declaration

```swift
var commandName: String?
```

#### Discussion

If `nil`, the command name is derived by converting the name of the command type to hyphen-separated lowercase words.

## See Also

### Defining Command Properties
- [var version: String](./version.md)
  Version information for this command.
- [var shouldDisplay: Bool](./shoulddisplay.md)
  A Boolean value indicating whether this command should be shown in the extended help display.
- [var aliases: [String]](./aliases.md)
  An array of aliases for the command’s name.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/commandconfiguration/commandname)*