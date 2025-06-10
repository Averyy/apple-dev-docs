# CMTimeCompare(_:_:)

**Framework**: Core Media  
**Kind**: func

Returns the numerical relationship of two times.

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
func CMTimeCompare(_ time1: CMTime, _ time2: CMTime) -> Int32
```

#### Return Value

A numeric value that indicates the relative order of the times.

#### Discussion

This method returns the following values depending on the relationship of the time values:

- If `time1` is less than `time2`, it returns `-1`.
- If `time1` is greater than `time2`, it returns `1`.
- If `time1` and `time2` are equal, it returns `0`.

To sort numeric and nonnumeric times consistently, this call uses the following sort rules:

`-infinity < all finite values < indefinite < +infinity < invalid`

Times with numerically larger epochs are greater than those with smaller epochs. ``

> 💡 **Tip**:  You can also use the [`CMTIME_COMPARE_INLINE`](cmtime_compare_inline.md) macro to compare times. This macro results in a more readable expression because it puts the comparison operator between the operands.

## Parameters

- `time1`: A time to compare.
- `time2`: Another time to compare.

## See Also

- [func CMTimeMaximum(CMTime, CMTime) -> CMTime](cmtimemaximum(_:_:).md)
  Returns the greater of two time values.
- [func CMTimeMinimum(CMTime, CMTime) -> CMTime](cmtimeminimum(_:_:).md)
  Returns the lesser of two time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimecompare(_:_:))*