---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/singlevalueparsingstrategy/unconditional"
framework: "swift-argument-parser/ArgumentParser"
---

# unconditional

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse the next input, even if it could be interpreted as an option or flag.

## Declaration

```swift
static var unconditional: SingleValueParsingStrategy { get }
```

#### Discussion

For inputs such as `--foo --bar baz`, if `.unconditional` is used for `foo`, this would read `--bar` as the value for `foo` and would use `baz` as the next positional argument.

This allows reading negative numeric values or capturing flags to be passed through to another program since the leading hyphen is normally interpreted as the start of another option.

> **Note**: This is usually *not* what users would expect. Use with caution.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/singlevalueparsingstrategy/unconditional)*