# encode(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Encodes a given Core Media time structure and associates it with a specified key.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func encode(_ time: CMTime, forKey key: String)
```

## Parameters

- `time`: A   structure.
- `key`: The key with which to associate   in the archive.

## See Also

- [func decodeTime(forKey: String) -> CMTime](nscoder/decodetime(forkey:).md)
  Returns the Core Media time structure associated with a given key.
- [func encode(CMTimeRange, forKey: String)](nscoder/encode(_:forkey:)-46lo8.md)
  Encodes a given Core Media time range structure and associates it with a specified key.
- [func encode(CMTimeMapping, forKey: String)](nscoder/encode(_:forkey:)-8tefb.md)
  Encodes a given Core Media time mapping structure and associates it with a specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-6wbby)*