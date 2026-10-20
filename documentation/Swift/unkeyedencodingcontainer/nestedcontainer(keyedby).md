# nestedContainer(keyedBy:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes a nested container keyed by the given type and returns it.

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
mutating func nestedContainer<NestedKey>(keyedBy keyType: NestedKey.Type) -> KeyedEncodingContainer<NestedKey> where NestedKey : CodingKey
```

#### Return Value

A new keyed encoding container.

## Parameters

- `keyType`: The key type to use for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/nestedcontainer(keyedby:))*