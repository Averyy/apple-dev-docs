# container(keyedBy:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns an encoding container appropriate for holding multiple values keyed by the given key type.

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
func container<Key>(keyedBy type: Key.Type) -> KeyedEncodingContainer<Key> where Key : CodingKey
```

#### Return Value

A new keyed encoding container.

#### Discussion

You must use only one kind of top-level encoding container. This method must not be called after a call to `unkeyedContainer()` or after encoding a value through a call to `singleValueContainer()`

## Parameters

- `type`: The key type to use for the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encoder/container(keyedby:))*