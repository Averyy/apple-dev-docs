---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncmainprotocol"
framework: "swift-argument-parser/ArgumentParser"
---

# AsyncMainProtocol

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: protocol  
**Role**: Protocol

A type that can designate an `AsyncParsableCommand` as the program’s entry point.

**Availability**:
- Swift - Deprecated in 5.6

> **Deprecated**: Use @main directly on your root `AsyncParsableCommand` type.

## Declaration

```swift
protocol AsyncMainProtocol
```

#### Overview

See the [`AsyncParsableCommand`](./asyncparsablecommand.md) documentation for usage information.

## Topics

### Associated Types
- [associatedtype Command : ParsableCommand](./asyncmainprotocol/command.md)
### Type Methods
- [static func main() async](./asyncmainprotocol/main%28%29.md)
  Executes the designated command type, or one of its subcommands, with the program’s command-line arguments.

## See Also

### Starting the Program
- [static func main() async](./asyncparsablecommand/main%28%29.md)
  Executes this command, or one of its subcommands, with the program’s command-line arguments.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncmainprotocol)*