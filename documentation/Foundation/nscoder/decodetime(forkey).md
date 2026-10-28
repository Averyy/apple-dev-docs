# decodeTime(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the Core Media time structure associated with a given key.

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
func decodeTime(forKey key: String) -> CMTime
```

```objc
- (CMTime) decodeCMTimeForKey:(NSString *) key;
```

## Return Value

The `CMTime` structure associated with `key` in the archive.

## Parameters

- `key`: The key for a `CMTime` structure encoded in the receiver.

## See Also

### Related Documentation
- [func encode(CMTime, forKey: String)](./encode%28_,forkey%29-6wbby.md)
  Encodes a given Core Media time structure and associates it with a specified key.
### Decoding Core Media Time Structures
- [func decodeTimeRange(forKey: String) -> CMTimeRange](./decodetimerange%28forkey%29.md)
  Returns the Core Media time range structure associated with a given key.
- [func decodeTimeMapping(forKey: String) -> CMTimeMapping](./decodetimemapping%28forkey%29.md)
  Returns the Core Media time mapping structure associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetime(forkey:))*