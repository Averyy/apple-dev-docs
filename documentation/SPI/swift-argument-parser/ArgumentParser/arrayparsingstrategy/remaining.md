---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/remaining"
framework: "swift-argument-parser/ArgumentParser"
---

# remaining

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Parse all remaining arguments into an array.

## Declaration

```swift
static var remaining: ArrayParsingStrategy { get }
```

## Discussion

`.remaining` can be used for capturing pass-through flags. For example, for a parsable type defined as `@Option(parsing: .remaining) var passthrough: [String]`:

```
$ cmd --passthrough --foo 1 --bar 2 -xvf
------------
options.passthrough == ["--foo", "1", "--bar", "2", "-xvf"]
```

> **Note**: This will read all inputs following the option without attempting to do any parsing. This is usually *not* what users would expect. Use with caution.

Consider using a trailing `@Argument` instead and letting users explicitly turn off parsing through the terminator `--`. That is the more common approach. For example:

```swift
struct Options: ParsableArguments {
    @Option var title: String
    @Argument var remainder: [String]
}
```

would parse the input `--title Foo -- Bar --baz` such that the `remainder` would hold the value `["Bar", "--baz"]`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/arrayparsingstrategy/remaining)*