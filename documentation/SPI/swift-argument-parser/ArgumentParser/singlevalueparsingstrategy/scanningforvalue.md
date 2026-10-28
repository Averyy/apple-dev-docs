---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/singlevalueparsingstrategy/scanningforvalue"
framework: "swift-argument-parser/ArgumentParser"
---

# scanningForValue

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse the next input, as long as that input can’t be interpreted as an option or flag.

## Declaration

```swift
static var scanningForValue: SingleValueParsingStrategy { get }
```

## Discussion

> **Note**: This will skip other options and *read ahead* in the input to find the next available value. This may be *unexpected* for users. Use with caution.

For example, if `--foo` takes a value, then the input `--foo --bar bar` would be parsed such that the value `bar` is used for `--foo`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/singlevalueparsingstrategy/scanningforvalue)*