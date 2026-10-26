---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flaginversion/prefixedenabledisable"
framework: "swift-argument-parser/ArgumentParser"
---

# prefixedEnableDisable

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Uses matching flags with `enable-` and `disable-` prefixes.

## Declaration

```swift
static var prefixedEnableDisable: FlagInversion { get }
```

#### Discussion

For example, the `extraOutput` property in this declaration is set to `true` when a user provides `--enable-extra-output` and to `false` when the user provides `--disable-extra-output`:

```
@Flag(inversion: .prefixedEnableDisable)
var extraOutput: Bool
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flaginversion/prefixedenabledisable)*