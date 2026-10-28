---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/singlevalue"
framework: "swift-argument-parser/ArgumentParser"
---

# singleValue

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse one value per option, joining multiple into an array.

## Declaration

```swift
static var singleValue: ArrayParsingStrategy { get }
```

## Discussion

For example, for a parsable type with a property defined as `@Option(parsing: .singleValue) var read: [String]`, the input `--read foo --read bar` would result in the array `["foo", "bar"]`. The same would be true for the input `--read=foo --read=bar`.

> **Note**: This follows the default behavior of differentiating between values and options. As such, the value for this option will be the next value (non-option) in the input. For the above example, the input `--read --name Foo Bar` would parse `Foo` into `read` (and `Bar` into `name`).


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/singlevalue)*