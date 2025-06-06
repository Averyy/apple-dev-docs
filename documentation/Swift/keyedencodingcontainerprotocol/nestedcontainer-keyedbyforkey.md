# nestedContainer(keyedBy:forKey:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Stores a keyed encoding container for the given key and returns it.

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
mutating func nestedContainer<NestedKey>(keyedBy keyType: NestedKey.Type, forKey key: Self.Key) -> KeyedEncodingContainer<NestedKey> where NestedKey : CodingKey
```

#### Return Value

A new keyed encoding container.

## Parameters

- `keyType`: The key type to use for the container.
- `key`: The key to encode the container for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/nestedcontainer(keyedby:forkey:))*