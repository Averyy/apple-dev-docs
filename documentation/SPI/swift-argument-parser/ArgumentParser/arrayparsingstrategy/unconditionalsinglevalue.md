---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/unconditionalsinglevalue"
framework: "swift-argument-parser/ArgumentParser"
---

# unconditionalSingleValue

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse the value immediately after the option while allowing repeating options, joining multiple into an array.

## Declaration

```swift
static var unconditionalSingleValue: ArrayParsingStrategy { get }
```

## Discussion

This is identical to `.singleValue` except that the value will be read from the input immediately after the option, even if it could be interpreted as an option.

For example, for a parsable type with a property defined as `@Option(parsing: .unconditionalSingleValue) var read: [String]`, the input `--read foo --read bar` would result in the array `["foo", "bar"]` – just as it would have been the case for `.singleValue`.

> **Note**: However, the input `--read --name Foo Bar --read baz` would result in `read` being set to the array `["--name", "baz"]`. This is usually *not* what users would expect. Use with caution.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/unconditionalsinglevalue)*