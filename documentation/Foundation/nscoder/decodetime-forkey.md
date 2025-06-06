# decodeTime(forKey:)

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

The `CMTime` structure associated with `key` in the archive.

## Parameters

- `key`: The key for a   structure encoded in the receiver.

## See Also

- [func encode(CMTime, forKey: String)](nscoder/encode(_:forkey:)-6wbby.md)
  Encodes a given Core Media time structure and associates it with a specified key.
- [func decodeTimeRange(forKey: String) -> CMTimeRange](nscoder/decodetimerange(forkey:).md)
  Returns the Core Media time range structure associated with a given key.
- [func decodeTimeMapping(forKey: String) -> CMTimeMapping](nscoder/decodetimemapping(forkey:).md)
  Returns the Core Media time mapping structure associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodetime(forkey:))*