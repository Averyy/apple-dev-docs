---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/share(bufferingpolicy:)"
framework: "swift-configuration/Configuration"
---

# share(bufferingPolicy:)

**Framework**: swift-configuration/Configuration  
**Kind**: method  
**Role**: Instance Method

Inherited from `AsyncSequence.share(bufferingPolicy:)`.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func share(bufferingPolicy: AsyncBufferSequencePolicy = .bounded(1)) -> some Sendable & AsyncSequence<Self.Element, Self.Failure>
```

Available when `Self` conforms to `SendableMetatype`, `AsyncIterator` conforms to `SendableMetatype`, and `Element` conforms to `Sendable`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/share(bufferingpolicy:))*