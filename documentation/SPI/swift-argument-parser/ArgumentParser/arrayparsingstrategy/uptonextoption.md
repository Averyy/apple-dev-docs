---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/uptonextoption"
framework: "swift-argument-parser/ArgumentParser"
---

# upToNextOption

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse all values up to the next option.

## Declaration

```swift
static var upToNextOption: ArrayParsingStrategy { get }
```

## Discussion

For example, for a parsable type with a property defined as `@Option(parsing: .upToNextOption) var files: [String]`, the input `--files foo bar` would result in the array `["foo", "bar"]`.

Parsing stops as soon as there’s another option in the input such that `--files foo bar --verbose` would also set `files` to the array `["foo", "bar"]`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/uptonextoption)*