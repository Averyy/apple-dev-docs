---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/init(_:)"
framework: "swift-configuration/Configuration"
---

# init(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: init  
**Role**: Initializer

Creates a new concrete async sequence wrapping the provided existential sequence.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ upstream: some Sendable & AsyncSequence<Element, Failure>)
```

## Parameters

- `upstream`: The async sequence to wrap.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence/init(_:))*