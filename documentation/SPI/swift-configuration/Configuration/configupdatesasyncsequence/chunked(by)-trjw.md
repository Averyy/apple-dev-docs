---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(by:)-trjw"
framework: "swift-configuration/Configuration"
---

# chunked(by:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.chunked(by:)`.

**Availability**:
- iOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
func chunked<C>(by timer: AsyncTimerSequence<C>) -> AsyncChunksOfCountOrSignalSequence<Self, [Self.Element], AsyncTimerSequence<C>> where Self : Sendable, C : Clock, Self.Element : Sendable
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/chunked(by:)-trjw)*