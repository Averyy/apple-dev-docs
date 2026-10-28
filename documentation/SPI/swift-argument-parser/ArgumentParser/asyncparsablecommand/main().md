---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/main()"
framework: "swift-argument-parser/ArgumentParser"
---

# main()

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Executes this command, or one of its subcommands, with the program’s command-line arguments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
static func main() async
```

## Discussion

Instead of calling this method directly, you can add `@main` to the root command for your command-line tool.

This method parses an instance of this type, one of its subcommands, or another built-in `AsyncParsableCommand` type, from command-line arguments, and then calls its `run()` method, exiting with a relevant error message if necessary.

## See Also

### Starting the Program
- [protocol AsyncMainProtocol](../asyncmainprotocol.md)
  A type that can designate an `AsyncParsableCommand` as the program’s entry point.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/main())*