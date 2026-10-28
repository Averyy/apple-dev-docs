---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/main()"
framework: "swift-argument-parser/ArgumentParser"
---

# main()

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Executes this command, or one of its subcommands, with the program’s command-line arguments.

## Declaration

```swift
static func main()
```

## Discussion

Instead of calling this method directly, you can add `@main` to the root command for your command-line tool.

This method parses an instance of this type, one of its subcommands, or another built-in `ParsableCommand` type, from command-line arguments, and then calls its `run()` method, exiting with a relevant error message if necessary.

## See Also

### Starting the Program
- [static func main([String]?)](./main%28_%29.md)
  Executes this command, or one of its subcommands, with the given arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/main())*