# keySpace(forIdentifier:)

**Framework**: AVFoundation  
**Kind**: method

Returns a metadata key space for the specified identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func keySpace(forIdentifier identifier: AVMetadataIdentifier) -> AVMetadataKeySpace?
```

#### Return Value

A metadata key space.

## Parameters

- `identifier`: The metadata identifier.

## See Also

- [class func identifier(forKey: Any, keySpace: AVMetadataKeySpace) -> AVMetadataIdentifier?](avmetadataitem/identifier(forkey:keyspace:).md)
  Returns a metadata identifier for the specified key and key space.
- [class func key(forIdentifier: AVMetadataIdentifier) -> Any?](avmetadataitem/key(foridentifier:).md)
  Returns a metadata key for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/keyspace(foridentifier:))*