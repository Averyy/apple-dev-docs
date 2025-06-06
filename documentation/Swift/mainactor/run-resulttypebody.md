# run(resultType:body:)

**Framework**: Swift  
**Kind**: method

Execute the given body closure on the main actor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func run<T>(resultType: T.Type = T.self, body: @MainActor () throws -> T) async rethrows -> T where T : Sendable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mainactor/run(resulttype:body:))*