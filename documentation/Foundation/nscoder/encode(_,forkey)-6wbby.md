# encode(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) encodeCMTime:(CMTime) time forKey:(NSString *) key;
```

## Parameters

- `time`: A `CMTime` structure.
- `key`: The key with which to associate `time` in the archive.

## See Also

### Related Documentation
- [func decodeTime(forKey: String) -> CMTime](./decodetime%28forkey%29.md)
  Returns the Core Media time structure associated with a given key.
### Encoding Core Media Time Structures
- [func encode(CMTimeRange, forKey: String)](./encode%28_,forkey%29-46lo8.md)
  Encodes a given Core Media time range structure and associates it with a specified key.
- [func encode(CMTimeMapping, forKey: String)](./encode%28_,forkey%29-8tefb.md)
  Encodes a given Core Media time mapping structure and associates it with a specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-6wbby)*