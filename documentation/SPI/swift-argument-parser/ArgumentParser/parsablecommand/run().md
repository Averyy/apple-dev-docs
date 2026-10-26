---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/run()"
framework: "swift-argument-parser/ArgumentParser"
---

# run()

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The behavior or functionality of this command.

## Declaration

```swift
mutating func run() throws
```

#### Discussion

Implement this method in your `ParsableCommand`-conforming type with the functionality that this command represents.

This method has a default implementation that prints the help screen for this command.

## Default Implementations

### ParsableCommand Implementations
- [func run() throws](./run%28%29-20aoy.md)
  The behavior or functionality of this command.

## See Also

### Implementing a Command’s Behavior
- [func validate() throws](../parsablearguments/validate%28%29.md)
  Validates the properties of the instance after parsing.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/parsablecommand/run())*