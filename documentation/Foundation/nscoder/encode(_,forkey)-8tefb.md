# encode(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes a given Core Media time mapping structure and associates it with a specified key.

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
func encode(_ timeMapping: CMTimeMapping, forKey key: String)
```

```objc
- (void) encodeCMTimeMapping:(CMTimeMapping) timeMapping forKey:(NSString *) key;
```

## Parameters

- `timeMapping`: A `CMTimeMapping` structure.
- `key`: The key with which to associate `timeMapping` in the archive.

## See Also

### Related Documentation
- [func decodeTimeMapping(forKey: String) -> CMTimeMapping](./decodetimemapping%28forkey%29.md)
  Returns the Core Media time mapping structure associated with a given key.
### Encoding Core Media Time Structures
- [func encode(CMTime, forKey: String)](./encode%28_,forkey%29-6wbby.md)
  Encodes a given Core Media time structure and associates it with a specified key.
- [func encode(CMTimeRange, forKey: String)](./encode%28_,forkey%29-46lo8.md)
  Encodes a given Core Media time range structure and associates it with a specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-8tefb)*