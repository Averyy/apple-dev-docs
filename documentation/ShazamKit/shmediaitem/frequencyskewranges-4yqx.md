# frequencySkewRanges

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

An array of ranges that indicate the frequency skews in the reference signature that this media item describes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, strong, readonly, nonnull) NSArray<SHRange *> * frequencySkewRanges;
```

*macOS*

```objc
@property (atomic, strong, readonly, nonnull) NSArray<SHRange *> * frequencySkewRanges;
```

## See Also

### Working with media item properties
- [subscript(SHMediaItemProperty) -> Any](./subscript%28_%29.md)
  Accesses the property for the specified key for reading.
- [- valueForProperty:](./valueforproperty_.md)
  Accesses the property for the specified key for reading.
- [struct SHMediaItemProperty](../shmediaitemproperty.md)
  Constants for the media item property names.
- [timeRanges](./timeranges-43654.md)
  An array of ranges that indicate the offsets within the reference signature that this media item describes.
- [SHRange](../shrange.md)
  A half-open interval from a lower bound up to, but not including, an upper bound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shmediaitem/frequencyskewranges-4yqx)*