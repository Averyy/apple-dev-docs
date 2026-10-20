# identifier(forKey:keySpace:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a metadata identifier for the specified key and key space.

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
class func identifier(forKey key: Any, keySpace: AVMetadataKeySpace) -> AVMetadataIdentifier?
```

```objc
+ (AVMetadataIdentifier) identifierForKey:(id) key keySpace:(AVMetadataKeySpace) keySpace;
```

#### Return Value

A metadata identifier, or `nil` if no equivalent identifier exists.

## Parameters

- `key`: A key to return an identifier for.
- `keySpace`: A key space to return an identifier for.

## See Also

### Translating metadata items
- [class func key(forIdentifier: AVMetadataIdentifier) -> Any?](./key%28foridentifier%29.md)
  Returns a metadata key for the specified identifier.
- [class func keySpace(forIdentifier: AVMetadataIdentifier) -> AVMetadataKeySpace?](./keyspace%28foridentifier%29.md)
  Returns a metadata key space for the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitem/identifier(forkey:keyspace:))*