---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/defaultasflagparsingstrategy/next"
framework: "swift-argument-parser/ArgumentParser"
---

# next

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse the input after the option and expect it to be a value.

## Declaration

```swift
static var next: DefaultAsFlagParsingStrategy { get }
```

## Discussion

For inputs such as `--foo foo`, this would parse `foo` as the value. However, the input `--foo --bar foo bar` would result in an error. Even though two values are provided, they don’t succeed each option. Parsing would result in an error such as the following:

```
Error: Missing value for '--foo <foo>'
Usage: command [--foo <foo>]
```

When used with `defaultAsFlag`, if no value is found, the default flag value is used.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/defaultasflagparsingstrategy/next)*