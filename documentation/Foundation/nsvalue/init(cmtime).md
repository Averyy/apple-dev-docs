# init(CMTime:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified CoreMedia time structure.

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
init(CMTime time: CMTime)
```

```swift
init(time: CMTime)
```

```objc
+ (NSValue *) valueWithCMTime:(CMTime) time;
```

#### Return Value

A new value object that contains the media time information.

## Parameters

- `time`: The value for the new object.

## See Also

### Related Documentation
- [struct CMTime](../../CoreMedia/cmtime.md)
  A structure that represents time.
### Working with Media Time Values
- [init(CMTimeRange: CMTimeRange)](./init%28cmtimerange%29.md)
  Creates a new value object containing the specified CoreMedia time range structure.
- [init(CMTimeMapping: CMTimeMapping)](./init%28cmtimemapping%29.md)
  Creates a new value object containing the specified CoreMedia time mapping structure.
- [var timeValue: CMTime](./timevalue.md)
  The CoreMedia time structure representation of the value.
- [var timeRangeValue: CMTimeRange](./timerangevalue.md)
  The CoreMedia time range structure representation of the value.
- [var timeMappingValue: CMTimeMapping](./timemappingvalue.md)
  The CoreMedia time mapping structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(cmtime:))*