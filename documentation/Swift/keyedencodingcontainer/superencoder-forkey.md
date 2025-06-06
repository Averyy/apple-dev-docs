# superEncoder(forKey:)

**Framework**: Swift  
**Kind**: method

Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.

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
mutating func superEncoder(forKey key: KeyedEncodingContainer<K>.Key) -> any Encoder
```

#### Return Value

A new encoder to pass to `super.encode(to:)`.

## Parameters

- `key`: The key to encode   for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer/superencoder(forkey:))*