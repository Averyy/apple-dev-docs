---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/run()"
framework: "swift-argument-parser/ArgumentParser"
---

# run()

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The behavior or functionality of this command.

**Availability**:
- iOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
mutating func run() async throws
```

#### Discussion

Implement this method in your `ParsableCommand`-conforming type with the functionality that this command represents.

This method has a default implementation that prints the help screen for this command.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/asyncparsablecommand/run())*