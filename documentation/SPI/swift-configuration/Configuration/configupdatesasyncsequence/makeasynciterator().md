---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/makeasynciterator()"
framework: "swift-configuration/Configuration"
---

# makeAsyncIterator()

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.makeAsyncIterator()`.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func makeAsyncIterator() -> some AsyncIteratorProtocol<Element, Failure>
```

Available when `Element` conforms to `Sendable` and `Failure` conforms to `Error`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/makeasynciterator())*