---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/defaultasflagparsingstrategy"
framework: "swift-argument-parser/ArgumentParser"
---

# DefaultAsFlagParsingStrategy

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: struct  
**Role**: Structure

The strategy to use when parsing a single value from `@Option` arguments with `defaultAsFlag`.

## Declaration

```swift
struct DefaultAsFlagParsingStrategy
```

#### Overview

This is a subset of `SingleValueParsingStrategy` that excludes strategies incompatible with default-as-flag behavior.

## Topics

### Type Properties
- [static var next: DefaultAsFlagParsingStrategy](./defaultasflagparsingstrategy/next.md)
  Parse the input after the option and expect it to be a value.
- [static var scanningForValue: DefaultAsFlagParsingStrategy](./defaultasflagparsingstrategy/scanningforvalue.md)
  Parse the next input, as long as that input can’t be interpreted as an option or flag.
### Default Implementations
- [Equatable Implementations](./defaultasflagparsingstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/defaultasflagparsingstrategy)*