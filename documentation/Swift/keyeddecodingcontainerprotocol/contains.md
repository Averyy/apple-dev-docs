# contains(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether the decoder contains a value associated with the given key.

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
func contains(_ key: Self.Key) -> Bool
```

#### Return Value

Whether the `Decoder` has an entry for the given key.

#### Discussion

The value associated with `key` may be a null value as appropriate for the data format.

## Parameters

- `key`: The key to search for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyeddecodingcontainerprotocol/contains(_:))*