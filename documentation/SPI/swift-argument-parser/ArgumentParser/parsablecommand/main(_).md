---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/main(_:)"
framework: "swift-argument-parser/ArgumentParser"
---

# main(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Executes this command, or one of its subcommands, with the given arguments.

## Declaration

```swift
static func main(_ arguments: [String]?)
```

#### Discussion

This method parses an instance of this type, one of its subcommands, or another built-in `ParsableCommand` type, from command-line arguments, and then calls its `run()` method, exiting with a relevant error message if necessary.

## Parameters

- `arguments`: An array of arguments to use for parsing. If `arguments` is `nil`, this uses the program’s command-line arguments.

## See Also

### Starting the Program
- [static func main()](./main%28%29.md)
  Executes this command, or one of its subcommands, with the program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/main(_:))*