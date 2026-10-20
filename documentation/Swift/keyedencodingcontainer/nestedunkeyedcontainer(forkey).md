# nestedUnkeyedContainer(forKey:)

**Framework**: Swift  
**Kind**: method

Stores an unkeyed encoding container for the given key and returns it.

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
mutating func nestedUnkeyedContainer(forKey key: KeyedEncodingContainer<K>.Key) -> any UnkeyedEncodingContainer
```

#### Return Value

A new unkeyed encoding container.

## Parameters

- `key`: The key to encode the container for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainer/nestedunkeyedcontainer(forkey:))*