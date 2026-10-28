# subscript(_:)

**Framework**: ShazamKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the property for the specified key for reading.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
subscript(key: SHMediaItemProperty) -> Any { get }
```

```objc
- (id) objectForKeyedSubscript:(SHMediaItemProperty) key;
```

## Return Value

The value of the property; otherwise, `nil`.

## Parameters

- `key`: The key for the media item property.

## See Also

### Working with media item properties
- [struct SHMediaItemProperty](../shmediaitemproperty.md)
  Constants for the media item property names.
- [var timeRanges: [Range<TimeInterval>]](./timeranges-8msna.md)
  An array of ranges that indicate the offsets within the reference signature that this media item describes.
- [var frequencySkewRanges: [Range<Float>]](./frequencyskewranges-1j7d3.md)
  An array of ranges that indicate the frequency skews in the reference signature that this media item describes.
- [- valueForProperty:](./valueforproperty_.md)
  Accesses the property for the specified key for reading.
- [timeRanges](./timeranges-43654.md)
  An array of ranges that indicate the offsets within the reference signature that this media item describes.
- [frequencySkewRanges](./frequencyskewranges-4yqx.md)
  An array of ranges that indicate the frequency skews in the reference signature that this media item describes.
- [SHRange](../shrange.md)
  A half-open interval from a lower bound up to, but not including, an upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/subscript(_:))*