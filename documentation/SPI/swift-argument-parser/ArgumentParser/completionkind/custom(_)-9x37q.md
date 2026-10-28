---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/custom(_:)-9x37q"
framework: "swift-argument-parser/ArgumentParser"
---

# custom(_:)

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: method  
**Role**: Type Method

Generate completions using the given async closure.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
static func custom(_ completion: @Sendable @escaping ([String], Int, String) async -> [String]) -> CompletionKind
```

## Discussion

The same as `custom(@Sendable @escaping ([String], Int, String) -> [String])`, except that the closure is asynchronous.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/completionkind/custom(_:)-9x37q)*