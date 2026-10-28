---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flaginversion/prefixedno"
framework: "swift-argument-parser/ArgumentParser"
---

# prefixedNo

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

Adds a matching flag with a `no-` prefix to represent `false`.

## Declaration

```swift
static var prefixedNo: FlagInversion { get }
```

## Discussion

For example, the `shouldRender` property in this declaration is set to `true` when a user provides `--render` and to `false` when the user provides `--no-render`:

```
@Flag(name: .customLong("render"), inversion: .prefixedNo)
var shouldRender: Bool
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/flaginversion/prefixedno)*