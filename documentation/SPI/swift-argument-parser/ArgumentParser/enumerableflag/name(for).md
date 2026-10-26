---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/name(for:)"
framework: "swift-argument-parser/ArgumentParser"
---

# name(for:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Returns the name specification to use for the given flag.

## Declaration

```swift
static func name(for value: Self) -> NameSpecification
```

#### Discussion

The default implementation for this method always returns `.long`. Implement this method for your custom `EnumerableFlag` type to provide different name specifications for different cases.

## Default Implementations

### EnumerableFlag Implementations
- [static func name(for: Self) -> NameSpecification](./name%28for%29-4ofoj.md)
  Returns the name specification to use for the given flag.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/name(for:))*