# SHRange

**Framework**: ShazamKit  
**Kind**: class  
**Role**: Class

A half-open interval from a lower bound up to, but not including, an upper bound.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```objc
@interface SHRange : NSObject
```

## Topics

### Creating a range
- [+ rangeWithLowerBound:upperBound:](./shrange/rangewithlowerbound_upperbound_.md)
  Creates a range with the bounds you specify.
- [- initWithLowerBound:upperBound:](./shrange/initwithlowerbound_upperbound_.md)
  Creates a range with the bounds you specify.
### Inspecting a range
- [lowerBound](./shrange/lowerbound.md)
  The range’s lower bound.
- [upperBound](./shrange/upperbound.md)
  The range’s upper bound.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Working with media item properties
- [subscript(SHMediaItemProperty) -> Any](./shmediaitem/subscript%28_%29.md)
  Accesses the property for the specified key for reading.
- [- valueForProperty:](./shmediaitem/valueforproperty_.md)
  Accesses the property for the specified key for reading.
- [struct SHMediaItemProperty](./shmediaitemproperty.md)
  Constants for the media item property names.
- [timeRanges](./shmediaitem/timeranges-43654.md)
  An array of ranges that indicate the offsets within the reference signature that this media item describes.
- [frequencySkewRanges](./shmediaitem/frequencyskewranges-4yqx.md)
  An array of ranges that indicate the frequency skews in the reference signature that this media item describes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shrange)*