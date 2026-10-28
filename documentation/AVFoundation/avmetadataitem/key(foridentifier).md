# key(forIdentifier:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a metadata key for the specified identifier.

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
class func key(forIdentifier identifier: AVMetadataIdentifier) -> Any?
```

```objc
+ (id) keyForIdentifier:(AVMetadataIdentifier) identifier;
```

## Return Value

A metadata key.

## Parameters

- `identifier`: The metadata identifier.

## See Also

### Translating metadata items
- [class func identifier(forKey: Any, keySpace: AVMetadataKeySpace) -> AVMetadataIdentifier?](./identifier%28forkey,keyspace%29.md)
  Returns a metadata identifier for the specified key and key space.
- [class func keySpace(forIdentifier: AVMetadataIdentifier) -> AVMetadataKeySpace?](./keyspace%28foridentifier%29.md)
  Returns a metadata key space for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/key(foridentifier:))*