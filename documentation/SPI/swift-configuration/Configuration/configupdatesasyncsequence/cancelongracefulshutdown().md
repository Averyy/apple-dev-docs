---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/cancelongracefulshutdown()"
framework: "swift-configuration/Configuration"
---

# cancelOnGracefulShutdown()

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.cancelOnGracefulShutdown()`.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func cancelOnGracefulShutdown() -> AsyncCancelOnGracefulShutdownSequence<Self>
```

Available when `Self` conforms to `Sendable` and `Element` conforms to `Sendable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/cancelongracefulshutdown())*