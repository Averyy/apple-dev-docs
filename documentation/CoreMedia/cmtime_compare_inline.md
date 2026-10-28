# CMTIME_COMPARE_INLINE

**Framework**: Core Media  
**Kind**: macro  
**Role**: Macro

Returns a Boolean value that indicates whether the specified comparison is true.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define CMTIME_COMPARE_INLINE(time1, comparator, time2)
```

## Discussion

The following code demonstrates how to use this macro to determine if the first time is less than or equal to the second time:

```objc
CMTIME_COMPARE_INLINE(time1, <=, time2)
```

## See Also

### Comparing Times
- [func CMTimeCompare(CMTime, CMTime) -> Int32](./cmtimecompare%28_,_%29.md)
  Returns the numerical relationship of two times.
- [func CMTimeMaximum(CMTime, CMTime) -> CMTime](./cmtimemaximum%28_,_%29.md)
  Returns the greater of two time values.
- [func CMTimeMinimum(CMTime, CMTime) -> CMTime](./cmtimeminimum%28_,_%29.md)
  Returns the lesser of two time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime_compare_inline)*