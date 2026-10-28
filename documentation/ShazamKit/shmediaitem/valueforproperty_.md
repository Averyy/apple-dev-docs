# valueForProperty:

**Framework**: ShazamKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id) valueForProperty:(SHMediaItemProperty) property;
```

## Return Value

The value of the property; otherwise, `nil`.

## Parameters

- `property`: The key for the property.

## See Also

### Working with media item properties
- [subscript(SHMediaItemProperty) -> Any](./subscript%28_%29.md)
  Accesses the property for the specified key for reading.
- [struct SHMediaItemProperty](../shmediaitemproperty.md)
  Constants for the media item property names.
- [timeRanges](./timeranges-43654.md)
  An array of ranges that indicate the offsets within the reference signature that this media item describes.
- [frequencySkewRanges](./frequencyskewranges-4yqx.md)
  An array of ranges that indicate the frequency skews in the reference signature that this media item describes.
- [SHRange](../shrange.md)
  A half-open interval from a lower bound up to, but not including, an upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/valueforproperty:)*