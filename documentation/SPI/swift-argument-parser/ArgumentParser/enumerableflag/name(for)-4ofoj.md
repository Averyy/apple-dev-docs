---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/name(for:)-4ofoj"
framework: "swift-argument-parser/ArgumentParser"
---

# name(for:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Returns the name specification to use for the given flag.

## Declaration

```swift
static func name(for value: Self) -> NameSpecification
```

#### Discussion

The default implementation for this method always returns `.long`. Implement this method for your custom `EnumerableFlag` type to provide different name specifications for different cases.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/enumerableflag/name(for:)-4ofoj)*