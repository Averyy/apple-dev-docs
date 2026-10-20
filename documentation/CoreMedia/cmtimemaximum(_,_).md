# CMTimeMaximum(_:_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns the greater of two time values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimeMaximum(_ time1: CMTime, _ time2: CMTime) -> CMTime
```

```c
extern CMTime CMTimeMaximum(CMTime time1, CMTime time2);
```

#### Return Value

The greater of the two times.

## Parameters

- `time1`: A time value.
- `time2`: Another time value.

## See Also

### Comparing Times
- [func CMTimeCompare(CMTime, CMTime) -> Int32](./cmtimecompare%28_,_%29.md)
  Returns the numerical relationship of two times.
- [func CMTimeMinimum(CMTime, CMTime) -> CMTime](./cmtimeminimum%28_,_%29.md)
  Returns the lesser of two time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimemaximum(_:_:))*