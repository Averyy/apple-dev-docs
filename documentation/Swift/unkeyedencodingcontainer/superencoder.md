# superEncoder()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes a nested container and returns an `Encoder` instance for encoding `super` into that container.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func superEncoder() -> any Encoder
```

#### Return Value

A new encoder to pass to `super.encode(to:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/superencoder())*