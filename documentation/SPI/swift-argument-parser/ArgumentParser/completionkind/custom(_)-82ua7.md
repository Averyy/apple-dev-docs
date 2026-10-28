---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/custom(_:)-82ua7"
framework: "swift-argument-parser/ArgumentParser"
---

# custom(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Deprecated; only kept for backwards compatibility.

> **Deprecated**: Provide a three-parameter closure instead. See custom(@Sendable @escaping ([String], Int, String) -> [String]).

## Declaration

```swift
@preconcurrency
static func custom(_ completion: @Sendable @escaping ([String]) -> [String]) -> CompletionKind
```

## Discussion

The same as `custom(@Sendable @escaping ([String], Int, String) -> [String])`, except that the last two closure arguments are not supplied.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/custom(_:)-82ua7)*